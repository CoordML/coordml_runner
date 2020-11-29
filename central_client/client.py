import aiohttp
import asyncio
from central_client.api import CentralAPI
from gpu_status import GpuStatus, GpuInfo
from collections import namedtuple
from typing import Tuple


Dependency = Tuple[str, str]
Task = namedtuple('Task', ['args', 'executable', 'meta', 'status', 'task_id'])
RunnableTask = namedtuple('RunnableTask', ['env_path', 'exp_id', 'result_parse', 'task'])
RunnableGraph = namedtuple('RunnableGraph', ['graph_id', 'nodes', 'dependencies'])


class CentralClient:
    def __init__(self, name: str, api_endpoint: str):
        self.name = name
        self.api: CentralAPI = CentralAPI(api_entry=api_endpoint)
        self.worker_id = None

    async def register(self):
        resp = await self.api.register(self.name)
        self.worker_id = resp['workerId']

    async def report_gpu(self, gpu_status: GpuInfo):
        await self.api.report_gpu(self.worker_id, gpu_status)


async def main():
    api = CentralAPI()
    worker_id = await api.register('Runner 127.0.0.1')
    status = GpuStatus().get_info()
    print(await api.report_gpu(worker_id['workerId'], status))
    print(await api.worker_list())
    print(await api.fetch_task(worker_id['workerId']))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
