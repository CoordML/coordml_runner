import asyncio
from coorml_runner.gpu_report import GpuReport
from gpu_status import GpuStatus, GpuStatusMode
from central_client.client import CentralClient


class Entry:
    def __init__(self, api_endpoint: str, runner_name: str, gpu_mode: GpuStatusMode = GpuStatusMode.FAKE):
        self.client = CentralClient(name=runner_name, api_endpoint=api_endpoint)
        self.gpu_status = GpuStatus(gpu_mode)
        self.gpu_report = GpuReport(client=self.client, gpu_status=self.gpu_status)

    async def start(self):
        await self.client.register()
        print(f'Runner registered, id {self.client.worker_id}')
        gpu_report_task = asyncio.create_task(self.gpu_report.run())
        print(f'GpuReport module spawned')
        print(f'Runner started')
        await asyncio.gather(gpu_report_task)
