import asyncio
from app.astro_wave import AstroWave

async def main():
   app = AstroWave()
   app.run()

if __name__ == "__main__":
  asyncio.run(main())