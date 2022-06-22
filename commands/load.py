import click
import pandas as pd


@click.command()
@click.option(
    "-f", "--filename", help="Test data in 'csv' extension.", required=True, type=str
)
@click.option(
    "-r",
    "--radial-stress",
    help="Radial stress to which the soil mass is subjected.",
    required=True,
    type=float,
)
def cli(filename: str):
    """: Load soil test data."""

    try:
        data = pd.read_csv(filename, header=None)
    except FileNotFoundError:
        click.echo("Error: File not found.")
        exit()
