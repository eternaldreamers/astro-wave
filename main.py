import asyncio
import click
from app.modules import GUIModule, HiperEspectralModule
from app.astro_wave import AstroWave

@click.group()
def main():
   pass

@main.command()
def version():
   click.echo("1.0.0")

@main.command()
def start():
   AstroWave().run()

@main.command()
def hiperespectral():
   HiperEspectralModule().run()

@main.command()
def gui():
   GUIModule().run()

if __name__ == "__main__":
  asyncio.run(main())