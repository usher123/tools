# 仿照fastapi的使用风格，来编写协程任务
## Demo 
```
import time
import RARY
query = RARY.package()

****************************  demo  *************************************
@query.createTask(model="daliy")
def task_test():
    print(time.strftime("%M:%S", time.localtime()), ': test join')
    time.sleep(1)
    print(time.strftime("%M:%S", time.localtime()),  ': test close')
    return '1'

@query.createTask(model="daliy")
async def task_test1(pl=3):
    print(time.strftime("%M:%S", time.localtime()), ': test1 join')
    await asyncio.sleep(2)
    print('task_test1 default is: ', pl)
    print(time.strftime("%M:%S", time.localtime()), ': test1 close')
    return '2'

@query.createTask(model="daliy")
async def task_test2():
    print(time.strftime("%M:%S", time.localtime()), ': test2 join')
    await asyncio.sleep(1)
    print(time.strftime("%M:%S", time.localtime()), ': test2 close')
    return '3'
    
    
    
if __name__ == "__ main__":
    RARY.run()
```

```
>>> 04:55 : test1 join
>>> 04:55 : test join
>>> 04:56 : test close
>>> 04:56 : test2 join
>>> task_test1 default is:  3
>>> 04:57 : test1 close
>>> 04:57 : test2 close
```
