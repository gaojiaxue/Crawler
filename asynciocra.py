##no async
# import time 

# def job(t):
#     print('Start job',t)
#     time.sleep(t)
#     print('Job',t,'takes',t,'s')

# def main():
#     [job(t)for t in range(1,3)]

# t1=time.time()
# main()
# print('No async takes time:',time.time()-t1)

##async
import asyncio
import time

async def job(t):
    print('Start job',t)
    await asyncio.sleep(t)
    print('Job ', t, ' takes ', t, ' s')


async def main(loop):               
    tasks=[loop.create_task(job(t))for t in range(1,3)]
    await asyncio.wait(tasks)

t1=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Async total time:',time.time()-t1)


