import click
import os

PLUGIN_FOLDER = os.path.join(os.path.dirname(__file__), "commands")


class MyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(PLUGIN_FOLDER):
            if filename.endswith(".py") and filename != "__init__.py":
                commands.append(filename[:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        ns = {}
        command_path = os.path.join(PLUGIN_FOLDER, name + ".py")
        with open(command_path) as file:
            command = compile(file.read(), command_path, "exec")
            eval(command, ns, ns)
        return ns["cli"]


cli = MyCLI(
    help="This tool's subcommands are loaded from a plugin folder dynamically."
)

if __name__ == "__main__":
    cli()