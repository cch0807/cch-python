### event_loop를 위한 선수지식
# asyncio (1)

- asyncio는 async/await 구문을 사용하여 동시성 코드를 작성하는 라이브러리이다.
- asyncio는 고성능 네트워크 및 웹 서버, 데이터베이스 연결 라이브러리, 분산 작업 큐 등을 제공하는 여러 파이썬 비동기 프레임워크의 기반으로 사용된다.


# generator
- 제네레이터는 말그대로 값을 생성하는 함수이다.
- 알다시피 함수는 값을 반환한 다음 자신의 스코프를 소멸시키고, 다시 함수를 호출하면, 처음부터 다시 시작된다. 즉 한 번 실행된다.
- 제네레이터 함수는 값을 생성하고 함수의 실행을 일시 중지 할 수 있다.
- 컨트롤이 호출 스코프로 반환되며, 원하는 경우 실행을 다시 시작하여 다른 값 (있는 경우)을 얻을 수 있다.
- 일반적인 함수를 실행하면 함수의 바디가 실행되지만, 제네레이터는 함수의 객체가 반환된다.
- 제네레이터 객체는 iterator와 동일하게 __next__()메소드를 가지고 있다.
- 아래와 같이 제네레이터 함수를 작성함으로써 '메모리를 할당할 수 없는 크기의 배열을 출력'하는 경우에도 제네레이터를 사용하면 가능하게 된다.
- 제네레이터 함수는 하나의 값을 반환하는 대신 실행을 일시 중지하고 여러 값을 생성 할 수 있는 함수이다.
- 또한 호출되면 iterable처럼 작동하는 제네레이터 객체를 제공하며 반복적으로 얻을 수 있다.

```
def test():
for i in range(10):
yield i * 2
```

# coroutine
- 한번에 하나의 코드에서만 동작하며, thread와 비교되어 설명되지만 완전히 다른 동작을 한다.
- thread의 경우에는 비동기식으로 여러 thread가 한번에 동작할 수 있지만, coroutine의 경우에는 yield키워드를 통해 호출자와 피호출자 함수사이에서 이동하며 실행되는 방식이다.

- coroutine은 generator와 yield를 사용하는 것에서는 동일하지만, send()메소드를 사용하여 값을 제네레이터로 보낼 수 있다는 점에서 차이를 가진다.
- 사용 방법으로는 처음에는 코루틴 객체를 받고, next를 호출하여 yield까지 진행을 부분까지는 동일하다.

- 그 이후에는 send()메소드를 사용하여 coroutine에서 사용하는 변수에 값을 전달할 수 있다. 전달 후에는 마찬가지로 yield까지 또 진행이된 다음 값을 할당받고 yield에서 멈춘다.
- yield 뒤에는 변수가 함께와서 사용되지만, yield만 사용될 때는 입력만 받는 용도로 사용된다.

- coroutine을 실행하기 위한 caller와 callee(coroutine)간의 비동기 방식 프로그래밍의 방식으로 추가된 것은 다음과 같다.

1. coroutine에서 caller로 예외 발생 전달은 try-finally 구문으로 처리 가능
2. caller에서 coroutine으로 예외 전달은 send와 같이 throw를 사용하여 처리 가능
3. caller에서 중단 되어 있는 coroutine을 종료 시키는 close메소드 사용 가능 (내부적으로 throw 사용)

- yield from 키워드를 사용하여 subtask의 동작에서도 coroutine을 사용 가능 (coroutine내에서 coroutine을 호출)

# asyncio
- event loop방식의 비동기 프로그래밍 asyncio가 표준 라이브러리로 추가.
- event loop는 C언어에서 사용하는 것처럼 callback형식으로 사용이 가능하지만, coroutine과 함께 사용한다면 많은 이점 단일 thread에서 multi-thread를 사용하는 것과 같은 효과
- asyncio에서도 cocurrent.futures.Future과 유사한 asyncio.future를 제공한다.
- 차이점은 일반 함수가 아니라 coroutine을 전달하는 것이고, future result()함수가 blocking되지 않는다는 점(단일 thread에서 event loop로 돌기 때문)
- asyncio를 이해하는데 홍동되는 부분은 future때문.
- asyncio는 future없이도 callback만 사용이 가능하며 call_later()등의 함수를 사용하여 callback을 등록하고 사용 가능하다.
- 하지만 이것만 사용하는 경우에는 asyncio의 장점을 살릴 수 없다.
- call_later()를 사용하여 callback을 등록하면 event loop에서 적절한 시점에 callback을 호출

- coroutine은 future을 이용하여 사용된다.
- 실제적으로 future를 직접 사용하지 않고, 이를 상속받은 Task Class를 사용
- future와 task의 차이점은 future은 coroutine을 예외 처리를 위해 감싼 것이고, task는 여기에 event loop와 같이 연계

- @asyncio.coroutine을 살펴보면 함수 앞에 사용되면서 decorator역할을 한다.
- decorator도 함수이며 함수를 parameter로 받아 다시 함수를 리턴한다.
- 기존 함수를 변형하는 용도로 사용하며 함수의 입출력을 바꾸거나 trace를 하는 용도로 사용된다.

- coroutine은 일반적으로 caller에서 반복적으로 next, send를 이용하여 yield에 멈춰있는 coroutine을 재개시킨다.
- coroutine에서는 내부적으로 다른 coroutine을 호출할 수 있으며 yield from으로 중첩도 가능하다.

- send()를 반복적으로 호출하는 것을 asyncio의 event loop에서 한다고 보면 된다.
- 이렇게 되면 coroutine도 event loop에서 마치 별도의 thread에서 도는 것과 같은 동작을 수행하게 된다.
- 이들 coroutine을 event loop에서 관리하기 위해서 future를 상속받은 Task Class를 사용하는 것이다.

- 일반 callback함수는 call_later()를 이용하여 event loop에 등록하고 coroutine은 ensure_future()나 loop.create_task()를 사용하여 등록할 수 있다.
- 추가로 이전에 yield from에는 iterator, generator(coroutine)이 사용 가능 했는데, 여기에 future도 사용이 가능하도록 추가.
```
import asyncio

@asyncio.coroutine
def print_every_second_coroutine(type):
    "Print seconds"
    while True:
        for i in range(10):
            print(i, 's (coroutine {})'.format(type))
            yield from asyncio.sleep(1)
        loop = asyncio.get_event_loop()
        loop.stop()
    
def print_every_seconds_callback(i):
    print (i, 's (callback)')
    loop = asyncio.get_event_loop()
    loop.call_later(1.0, print_every_seconds_callback, i+1)

def print_every_seconds_callback_to_coroutine():
    asyncio.ensure_future(print_every_second_corouine('8'))

if __name__ == '__main__':
    loop = asyncio.get_event_loop
    loop.call_soon(print_every_seconds_callback, 0)
    loop.call_soon(print_every_seconds_callback_to_coroutine)
    asyncio.ensure_future(print_every_second_coroutine('A'))

    loop.run_forever()
    loop.close()
```

- print_every_second_coroutine()은 asyncio.ensure_future()를 이용하여 default handler에 coroutine을 등록한다.
- 이 때는 generator나 future를 등록해야 하기 때문에 print_every_second_coroutine('A')와 같이 generator를 리턴 받아서 등록한다.
- 이는 바로 event loop (loop.run_forever())에서 호출된다.

- callback은 print_every_seconds_callback 와 같이 함수 이름을 전달한다.
- 만일 함수에 parameter 전달 조건이 맞지 않는다면 functiontools.partial을 이용 할 수 있다.
- 기본적으로 one shot 이기 때문에 callback 함수에서는 call_later() 등의 method를 이용하여 반복해서 호출해준다. (여러번 등록 필요)

- print_every_seconds_callback_to_coroutine()과 같이 일반 callback 함수에서는 coroutine을 직접 호출할 수 없다.(직접 호출하려면 이 함수가 next()를 반복해서 호출하여야 하기 때문에 event loop가 blocaking 된다.)
- 대신, coroutine을 등록 하는 것과 동일하게 asyncio.ensure_future() (또는 loop.create_task())를 사용한다.

# async, await
- coroutine을 명시적으로 지정하는 async와 yield를 대체하는 await keyword.
- 이를 기존이 yield를 사용하는 generator based coroutine과 구분하기 위하여 native coroutine이라고 한다.
- 기존 generator based coroutine 은 함수 내에 yield 유무로 결정되나, native coroutine은 함수 앞에 async 키워드를 붙여서 사용한다.
- async 함수에는 기존 문법인 yield(from)을 사용할 수 없고, await를 사용한다.

# async internal
- async/await가 추가되면서 확장된 data model을 보면 다음과 같다.

- awaitable object:
    - __await__()가 구현된 객체, async def 함수를 호출하여 리턴되는 native coroutine이 awaitable 객체
    - object__await__(self)에서 iterator가 리턴되어 await에서 사용된다.
    - generator based coroutine과 유사하게 __await__()로 받은 iterator를 send()를 이용하여 반복

# async with, async for
- async with은 with다음에 클래스 인스턴스를 지정하고 as 뒤에 결과를 저장할 변수를 지정한다.
- async with으로 동작하는 클래스를 만들려면 __aenter__()과 __aexit__() method를 구현해야 한다.
- 메서드를 구현할 때는 반드시 async def를 사용하여 작성한다.

```
import asyncio

class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b # __aenter__에서 값을 반환하면 as에 지정한 변수에 들어감

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass

async def main():
    async with AsyncAdd(1, 2) as result: # async with에 클래스의 인스턴스 지정
        print(result) # 3

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

```

# 코루틴과 제네레이터, async/await 키워드
