import time
import asyncio
import requests

async def function1():
      URL = "https://instagram.com/favicon.ico"
      response = requests.get(URL)
      open("instagram1.ico", "wb").write(response.content)
      await asyncio.sleep(1)
      print("function 1 is done")
      return "hello"

async def function2():
     URL = "https://instagram.com/favicon.ico"
     response = requests.get(URL)
     open("instagram2.ico", "wb").write(response.content)
     await asyncio.sleep(2)
     print("function 2 is done")
     
async def main():
      await function1()
      await function2()
      
    #    L = await asyncio.gather(
    #         function1(),
    #         function2(),
    #    )
    #    print(L)
    #    task1 = asyncio.create_task(function1())
    #    # await function1()
    #    await function1()
    #    await function2()
asyncio.run(main())