from enum import Enum
from collections import namedtuple
from typing import List
import random


class GpuStatusMode(Enum):
    FAKE = 1
    GPU_STAT = 2


GpuState = namedtuple('GpuInfo', ['name', 'memMax', 'memNow', 'load'])

GpuInfo = List[GpuState]


class GpuStatus:
    def __init__(self, mode: GpuStatusMode = GpuStatusMode.FAKE):
        self.mode = mode
        self.fake_gpu_name = 'Titan XP'
        self.fake_gpu_mem = 32.0
        self.fake_gpu_count = 8

    def _generate_fake_state(self):
        mem_load = random.random()
        load = random.random()
        return GpuState(self.fake_gpu_name, self.fake_gpu_mem, self.fake_gpu_mem * mem_load, load)

    def get_info_fake(self) -> GpuInfo:
        return [self._generate_fake_state() for _ in range(self.fake_gpu_count)]

    def get_info(self) -> GpuInfo:
        if self.mode == GpuStatusMode.FAKE:
            return self.get_info_fake()
        else:
            raise NotImplementedError
