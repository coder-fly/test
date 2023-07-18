import asyncio
import aiohttp

class Task:
    count = 0
    async def task(self):
        async with aiohttp.ClientSession(headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/114.0.1823.43',
        }) as session:
            while True:
                try:
                    async with session.get('https://github.com/coder-fly/douyin-signature/archive/refs/heads/master.zip') as response:
                        if response.status == 429:
                            print(self.count)
                            break
                        else:
                            self.count += 1
                        if self.count / 1000 == 0:
                            print(self.count)
                        await response.read()
                except:
                    continue

    async def start(self, *args, **kwargs):
        tasks = []
        for i in range(30):
            tasks.append(asyncio.create_task(self.task()))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(Task().start())