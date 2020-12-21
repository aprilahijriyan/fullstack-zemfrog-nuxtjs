import click
import os


@click.command(
    context_settings={
        "ignore_unknown_options": True
    }
)
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
def main(args):
    os.chdir("backend")
    os.system("flask " + " ".join(args))


if __name__ == "__main__":
    main()
