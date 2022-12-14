# 핵심은 asyncio.create_task

- asyncio.create_task 는 왜 쓰는 걸까? await run_job()을 대신 쓰면 안될까?
```
간단한 await run_job()이 안되는 이유부터 설명하면, await을 붙이는 순간 run_job이 return 할 때까지 main()
이 실행권을 갖지 못하기 때문이다. 쉽게 말해서 run_job()이 8초 걸리는 job이었다면 8초가 지나서야 await asyncio.sleep(10)을 실행하게 되는 것이다. 이 때문에 해당 iteration은 총 18초가 걸리며, "10초마다 Job을 생성함" 이라는 규칙을 어기게 된다.


```