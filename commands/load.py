import click
import pandas as pd


@click.command()
@click.option("-f", "--filename", help="Test data in 'csv' extension.", required=True, type=str)
def cli(filename: str):
    """: Load soil test data."""

    try:
        data = pd.read_csv(filename, header=None)
    except FileNotFoundError:
        click.echo("Error: File not found.")
        exit()
