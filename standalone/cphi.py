import pandas as pd
import numpy as np


def main():
    n = int(input("- Number of entrys (n): "))

    filename = [None] * n
    radial_stress = [None] * n
    test = [None] * n

    for i in range(n):
        filename[i] = input("* Filename n° {}: ".format(i + 1))
        radial_stress[i] = float(
            input("* Radial stress for '{}' dataset: ".format(filename[i]))
        )

        test[i] = load_test(filename[i])

    dataset = to_dataset(test, radial_stress)

    c, phi = compute_params(dataset)

    print("* c = {:.2f}.".format(c))
    print("* phi = {:.2f}°.".format(phi))


def compute_params(dataset: object):
    raw_params = get_raw_params(dataset)
    tg_alpha, k = raw_params

    phi = np.rad2deg(np.arcsin(tg_alpha))
    c = k / np.cos(np.deg2rad(phi))

    params = (c, phi)

    return params


def get_raw_params(dataset: object):
    """
    Get the modified envelope params of the set of laboratory tests.
    """
    p_f = [None] * len(dataset)
    q_f = [None] * len(dataset)

    for i, (data, radial_stress) in enumerate(dataset):
        sigma_1 = get_peak(data)[1] + radial_stress
        sigma_3 = radial_stress

        # Use MIT convention for stress path faillure points
        p = (sigma_1 + sigma_3) / 2
        q = (sigma_1 - sigma_3) / 2
        p_f[i] = p
        q_f[i] = q

    params = np.polyfit(p_f, q_f, deg=1)

    return params


def load_test(filename: str):
    try:
        test = pd.read_csv(filename, header=None)
    except FileNotFoundError:
        print("Error: File not found or invalid.")
        exit()

    test.columns = ["esf", "def"]

    return test


def get_peak(data: object):
    peak = data[data["def"] == data["def"].max()]
    # The failure point is the first point where the maximum stress is achieve.
    peak = peak.iloc[0]

    return (peak[0], peak[1])


def to_dataset(tests: list, radial_stress: list):
    # Make a list of tuples for each test data and radial stress.
    dataset = list(zip(tests, radial_stress))
    # Sort the dataset by radial stress.
    dataset = sorted(dataset, key=lambda x: x[1])

    return dataset


if __name__ == "__main__":
    main()
