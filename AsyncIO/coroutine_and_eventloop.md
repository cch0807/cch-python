# 핵심은 asyncio.create_task

- asyncio.create_task 는 왜 쓰는 걸까? await run_job()을 대신 쓰면 안될까?
```
간단한 await run_job()이 안되는 이유부터 설명하면, await을 붙이는 순간 run_job이 return 할 때까지 main()
이 실행권을 갖지 못하기 때문이다. 쉽게 말해서 run_job()이 8초 걸리는 job이었다면 8초가 지나서야 await asyncio.sleep(10)을 실행하게 되는 것이다. 이 때문에 해당 iteration은 총 18초가 걸리며, "10초마다 Job을 생성함" 이라는 규칙을 어기게 된다.

각 Job의 수행 시간과 상관없이 10초마다 계속 생성하려면 await와 Eventloop에 대해서 좀 더 자세히 알 필요가 있다. await은 사실 내부적으로 두 가지 동작을 한다고 볼 수 있따. 첫 번째로 await 뒤에 있는 코루틴을(좀 더 정확히는 Awaitable 객체) Eventloop에 실행해달라고 등록하고, 두 번째로 등록한 코루틴이 끝날 때 돌려받길 기대하며 실행권을 Eventloop에게 반환한다.
Eventloop은 등록한 코루틴이 종료되거나 에러가 발생한 이후에 실행권을 돌려준다. Eventloop은 이런 식으로 여러 코루틴 사이에 실행권을 주고 받으며 Cooperative multitasking을 달성하는 것이다.

지금의 경우 전자의 동작은 필요하지만, 후자의 동작은 필요가 없다. 이 때 사용할 수 있는게 바로 asyncio.create_task()이다. 해당 함수의 역할은, 파라미터로 들어오는 코루틴을 Eventloop 에 등록하고 코루틴이 끝났을 때 결과를 받아볼 수 있는 Future 객체를 반환한다. 반환되는 Future 또한 Awaitable 객체이기 때문에 await을 앞에 붙이면 Eventloop에 실행권을 넘기면서 코루틴의 종료까지 기다릴 수 있지만, 지금은 필요하지 않기 때문에 의도적으로 await 없이 넘어갔다. 그 때문에 실행권을 뺏기지 않은 채로 다음 while iteration을 위해 10초간 기다릴 수 있다.

* 사실 asyncio.create_task()가 반환하는 것은 Task 객체이고, 이 객체는 Future를 상속받기 때문에 동일하게 Awaitable하다.
```

# await 없이 run_job()만 쓰면 안될까?
```
await이 기다리는 동작을 내포하기 때문에 asyncio.create_task(run_job()) 대신 run_job()으로 변경해도 괜찮을까?

실제로 테스트해보면 RuntimeWarning: coroutine 'run_job' was never awaited이라는 warning과 함께 아무것도 출력되지 않은 것을 확인할 수 있다. 이유는 간단한데, run_job은 일반 함수가 아니라 "코루틴 함수" 이며, run_job()은 "코루틴 객체"를 생성해서 반환할 뿐 실제로 코루틴을 실행하지 않기 때문이다. run_job()은 코루틴 객체를 반환하는데, 이 객체는 generator 객체와 동이랗게 지금 실행하는 게 아니라 추후에 실행 가능한 객체이다.
또한, 앞서 설명한 것처러 코루틴을 실행하기 위해서는 Event에 등록해야 하므로 run_job()으로 코루틴 객체를 생성한다고 해서 코루틴을 실행하는게 아니다. 즉 코루틴을 실행하려면 asyncio.create_task나 await등을 Eventloop에 등록하는 것이 필수이다.

* 참고로 숫자 출력 예시 같은 표현식을 generator expression이라고 하며, 해당 표현식이 반환한 객체를 generator iterator라고 한다. 또한, generator iterator를 반환하는 함수를 generator이라고 부르며, 함수 내부에서 yield 키워드를 사용하면 자동으로 generator를 정의하는 것이 된다.
```

# 용어 정리 - 코루틴과 Future
await 키워드를 붙일 수 있는 최소 조건이 Awaitable이다. 
그래서 3가지(Coroutine, Future, Task) 모두 await으로 실행이 끝나길 기다릴 수 있다. 하지만 코루틴은 Eventloop에 등록되지 않으면 실행되지 않기 때문에, await을 붙이거나 Future나 Task로 감싸야 한다.

# 동시 실행
그렇다면 어디서 어떻게 동시 실행이 되고 있는걸까?
어디는 당연하게도 Eventloop 일 것이다. 문제는 Eventloop를 어떻게 동시 실행으로 구현하느냐이다. 이것을 이해하려면 Eventloop이 Cooperative multitasking을 하는 방식을 이해해야 한다. asyncio에 공리가 하나 있는데, "스레드당 실행 중인 Eventloop은 하나" 라는 제약조건이다. 즉, 아무리 많은 코루틴을 하나의 Eventloop에서 동시 실행해도 결국 single thread로 동작한다는 의미이다. (사실 예외가 있긴하다.) Eventloop의 구현체마다 다를 수 있지만, Cpython의 경우 내부 queue에 등록된 코루틴들을 기억하면서 한 번에 하나씩 번갈아가며 실행하고 있다. 그렇다면 어떻게 번갈아가면서 실행하길래 동시에 실행 중이라는 착각을 만들 수 있을까? 답은 await 키워드와 코루틴이라는 단어에 있다.

# 코루틴 vs 일반 함수
일반 함수는 호출될 때 stack에 올라간 후 실행권을 가지고 body를 수행한다.
수행이 끝나면 실행권을 호출한 곳으로 돌려주고 stack에서 사라진다. 하지만 코루틴은 언제든 실행권을 반환할 수 있다. 즉 일반 함수는 시작점과 반환점이 항상 처음과 끝으로 고정된 코루틴의 일종이라고 볼 수 있다.

# Eventloop가 코루틴을 실행하는 방식
앞서서 await 키워드가 실행될 때 실행권을 Eventloop에 넘긴다고 했는데, 이 때 해당 코루틴이 Suspend되면서 다른 코루틴을 마저 실행한다. OS에서 사용되는 프로세스 스케줄러와 비슷해 보이는데, 가장 큰 다른 점은 선점 여부이다. 대부분의 프로세스 스케줄러는 선점형이기 때문에 프로세스의 실행권을 뺏을 수 있지만, Eventloop은 비선점형이기 때문에 실행 중인 코루틴이 await을 사용하거나 return해서 실행권을 Eventloop에 돌려주지 않는다면 실행권을 뺏어서 다른 코루틴을 실행할 방법이 없다. 바로 이 이유 때문에 requests 같은 blocking 코드를 코루틴 내부에서 실행하지 못하도록 가이드 하는 것이다.

# 또 다른 동시 실행 방법
gather와 wait같은 함수들을 사용할 수 있따. 하지만 이 함수들은 기다릴 코루틴(혹은 future)을 파라미터로 넣어줘야하기 때문에 개수를 사전에 알고 있어야 한다는 제약이 있따. MySQL을 읽으면서 동시에 Redis를 읽을 때 같은 용례가 있을 것 같다. 각각을 코루틴으로 만들고, gather나 wait으로 모든 코루틴 종료를 기다리는 것이다. 또 as_completed()를 사용하면 여러 코루틴을 동시 실행하면서 끝나는 순서대로 결과를 받아볼 수 있다.

# Eventloop와 multi thread
사실 항상 모든 코루틴이 하나의 Eventloop에서 실행되진 않는다. '스레드당 실행 중인 Eventloop은 하나' 라는 제약이 있다는 말은, Eventloop을 하나 더 만들고 싶으면 스레드를 하나 더 만들면 된다는 의미이기도 하다. 그래서 run_coroutine_threadsafe를 사용하면 코루틴을 어떤 스레드에서 실행할지 선택할 수 있고, run_in_executor를 사용하면 Eventloop을 하나 더 만들지 않더라도 다른 스레드에서 함수를 실행 할 수 있따. 다른 스레드가 개입되고, 공유변수를 스레드에 걸쳐 사용한다면 접근제한을 고민해야 한다.
asyncio 모듈에서 제공하는 Synchronization primitive 들은 thread-safe 하지 않기 때문이다.
