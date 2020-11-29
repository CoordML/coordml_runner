import logging
import asyncio
from central_client.client import CentralClient
from central_client.tasks import *


logger = logging.getLogger(__name__)


class TaskRunner:
    def __init__(self, client: CentralClient, runner_config: dict):
        self.client = client
        self.max_tasks_per_gpu = runner_config['max_tasks_per_gpu']
        self.max_gpu_load = runner_config['max_gpu_load']
        self.min_gpu_mem = runner_config['min_gpu_mem']

    async def run(self):
        while True:
            await asyncio.sleep(1.0)
            tasks = await self.client.fetch_tasks()
            logger.info(f'Fetched new tasks from Central: {tasks}')
