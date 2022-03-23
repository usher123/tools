from .rary import *


__all__ = (
           rary.__all__
           )






# class TaskObjectMetaclass(type):
#     def __init__(cls,
#                  task: None,
#                  *args, **kwargs):
#         super(TaskObjectMetaclass, cls).__init__(*args, **kwargs)
#         if isinstance(task, Task):
#             TaskQuery.add_task(task)