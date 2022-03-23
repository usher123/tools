__all__ = 'run', 'package', 'getTask'

from . import Task
from . import TaskQuery

from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
)


class TaskObjectList:
    task: List[object]


def run() -> List[type]:
    """
    start to running task
    :return: finished object
    """
    return TaskQuery.TaskQuery.run_task()


class package(Task.Taskmethod):
    """
    package of task
    model:  模式
    """
    pass


def getTask() -> set:
    """
    返回当前task表
    """
    return TaskQuery.TaskQuery.Query