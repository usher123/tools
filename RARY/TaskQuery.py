__all__ = 'TaskQuery'

from . import Task
import asyncio

class TaskQuery:
    Query = set()
    asQuery = asyncio.Queue(maxsize=5)

    def __init__(self):
        pass

    @staticmethod
    def add_task(task=None):
        if isinstance(task, Task.Taskobject):
            TaskQuery.Query.add(task)

    @staticmethod
    def run_task():
        async def asyncStart():
            return await asyncio.gather(*{i.Target for i in TaskQuery.Query},
                                        return_exceptions=True
                                        )


        return asyncio.run(asyncStart())

    def lockQuery(self):
        pass
