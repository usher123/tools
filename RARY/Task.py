__all__ = 'Taskobject'

import functools
import asyncio
from .TaskQuery import TaskQuery


# class Taskmethodmeta(type):
#     func = None
#
#     def __init__(cls, *args, **kwargs):
#         super(Taskmethodmeta, cls).__init__(*args, **kwargs)
#
#     def __new__(cls, *args, **kwargs):
#         return type.__new__(cls, *args, **kwargs)
#
#     def __call__(cls, func=None, *args, **kwargs):
#         print('__call__:', func)
#         if func:
#             cls.createTask(Taskobject(func))
#         return cls.__new__(cls)


class Taskmethod():
    """
    method of task
    可以考虑用meta类，目前是用装饰器实现任务添加
    """

    def __init__(self):
        # super(Taskmethodmeta, self).__init__()
        pass

    def createTask(self, model, *args, **kwargs):
        # print(model, *args, **kwargs)
        def start(func):
            TaskQuery.add_task(Taskobject(func=func))
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                pass
            return _wrapper
        return start


class Taskobject:

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.items = func.__defaults__ if func.__defaults__ else ()
        self.Target = self.CreateAsync(*self.items)

    async def CreateAsync(self, *args, **kwargs):
        async def asyncdeal(*args, **kwargs):
            return self.func(*args, **kwargs)

        if asyncio.iscoroutinefunction(self.func):
            return await asyncio.create_task(self.func(*args, **kwargs))
        else:
            return await asyncio.create_task(asyncdeal(*args, **kwargs))