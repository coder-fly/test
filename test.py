import asyncio
import aiohttp

class Task:
    count = 0
    async def task(self):
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    async with session.get('https://github.com/coder-fly/douyin-signature/archive/refs/heads/master.zip') as response:
                        if response.status == 429:
                            break
                        else:
                            self.count += 1
                        await response.read()
                except:
                    continue

    async def start(self, *args, **kwargs):
        tasks = []
        for i in range(30):
            tasks.append(asyncio.create_task(self.task()))
        await asyncio.gather(*tasks)
