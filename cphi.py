import pandas as pd


def main():
    n = int(input("- Number of entrys (n) :"))
    filename = [None] * n
    data = [None] * n
    peak = [None] * n
    for i in range(n):
        filename[i] = input("* Filename n° {}: ".format(i + 1))
        data[i] = load(filename[i])
        peak[i] = get_peak(data[i])
    print(peak)


def load(filename: str):
    try:
        data = pd.read_csv(filename, header=None)
    except FileNotFoundError:
        print("Error: File not found or invalid.")
        exit()

    data.columns = ["esf", "def"]
    return data


def get_peak(data: object):
    peak = data[data["def"] == data["def"].max()]

    return (float(peak["esf"]), float(peak["def"]))


if __name__ == "__main__":
    main()
