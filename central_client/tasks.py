from collections import namedtuple
from typing import Tuple, List


Dependency = Tuple[str, str]
Task = namedtuple('Task', ['args', 'executable', 'meta', 'status', 'task_id'])
RunnableTask = namedtuple('RunnableTask', ['env_path', 'exp_id', 'result_parse', 'task'])
RunnableGraph = namedtuple('RunnableGraph', ['graph_id', 'nodes', 'dependencies'])


def parse_task(obj: dict) -> Task:
    return Task(
        args=obj['args'],
        meta=obj['meta'],
        executable=obj['executable'],
        status=obj['status'],
        task_id=obj['taskId']
    )


def parse_dependencies(obj: List[dict]) -> List[Dependency]:
    return [(x[0], x[-1]) for x in obj]


def parse_runnable_task(obj: dict) -> RunnableTask:
    return RunnableTask(
        env_path=obj['envPath'],
        exp_id=obj['expId'],
        result_parse=obj['resultParse'],
        task=parse_task(obj['task'])
    )


def parse_runnable_graph(obj: dict) -> RunnableGraph:
    return RunnableGraph(
        graph_id=obj['graphId'],
        nodes=[parse_runnable_task(x) for x in obj['nodes']],
        dependencies=[parse_dependencies(x) for x in obj['dependencies']]
    )
