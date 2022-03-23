```
import RARY
query = RARY.package()

****************************  demo  *************************************
@query.createTask(model="daliy")
def task_test():
    print('test join')
    time.sleep(1)
    print('test close')
    return '1'

@query.createTask(model="daliy")
async def task_test1(pl='task_test1'):
    print('test1 join')
    await asyncio.sleep(2)
    print(pl)
    print('test1 close')
    return '2'

@query.createTask(model="daliy")
async def task_test2():
    print('test2 join')
    await asyncio.sleep(1)
    print('test2 close')
    return '3'
    
    
    
if __name__ == "__ main__":
    RARY.run()
```

