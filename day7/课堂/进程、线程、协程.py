import asyncio

async def fun1():
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    print('1')
    await asyncio.sleep(1)
    return '1 finish'

async def fun2():
    print('2')
    await asyncio.sleep(2)
    return '2 finish'


async def main():
    results = await asyncio.gather(*[asyncio.create_task(fun1()), asyncio.create_task(fun2())])
    for r in results:
        print(r)

asyncio.run(main())

print("the end")
