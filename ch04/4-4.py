import asyncio

async def q():
    print('Sitwel: there are no correct answers?')
    await asyncio.sleep(3)

async def a():
    print("Rogers: but it's fast!")

async def main():
    await asyncio.gather(q(), a())

asyncio.run(main())
