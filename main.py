import asyncio
from app.astro_wave import setup

async def main():
   await setup()

if __name__ == "__main__":
  asyncio.run(main())