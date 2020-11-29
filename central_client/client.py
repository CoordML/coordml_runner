import aiohttp
import asyncio
from central_client.api import CentralAPI
from central_client.tasks import *
from gpu_status import GpuStatus, GpuInfo


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

    async def fetch_tasks(self) -> List[RunnableGraph]:
        resp = await self.api.fetch_task(self.worker_id)
        return [parse_runnable_graph(x) for x in resp['tasks']]


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
