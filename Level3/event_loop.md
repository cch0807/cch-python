### event_loop를 위한 선수지식
# asyncio 

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
```
코루틴(Coroutine)이란 특정 시점에 자신의 실행과 관련된 상태를 어딘간에 저장한 뒤 실행을 중단하고, 나중에 그 상태를 복원하여 실행을 재개할 수 있는 서브 루틴을 의미한다,
여기서 말하는 서브 루틴(subroutine)이란 일반적으로 우리가 알고 있는 함수를 의미 한다고 보면 된다. 즉, 코루틴은 함수 중에서도 조금 특별한 함수인 것이다.
그런데 여기서 하나 짚고 넘어가야 하는 건, 코루틴이나 서브 루틴은 Python에서만 쓰는 용어가 아닌 CS 전반에서 사용되는 용어라는 것이다.
따라서 우리는 'Python이 이러한 코루틴과 서브 루틴을 어떻게 구현하였는가'에 초점을 맞추는 것이 맞다. 
```

- Python에서 서브 루틴과 코루틴은 다음과 같이 정의된다.
- 우리가 이미 알고 있는 대로 def 키워드만을 이용하여 함수를 정의하면 서브 루틴이 되고, 앞에 async 키워드까지 붙여서 함수를 정의하면 코루틴이 된다.

```
# Subroutine (Synchronous Function)
def subroutine():
    print('subroutine')

# Coroutine (Asynchronous Function)
async def coroutine():
    print('coroutine')
```

```
그리고 async 키워드에서 알수 있듯이 코루틴은 비동기 함수라고도 한다.
비동기(Asynchronous)라는 것은 쉽게 말해서 어떠한 작업이 완료되기를 기다리지 않고, 그 시간 동안 다른 작업을 하는 것을 말한다.
일반적인 Python 프로그램은 동기(Synchronous) 함수로만 이뤄져 있기 때문에, 항상 어떠한 작업이 완료되기를 기다린 후에 그다음 작업을 진행하게 된다.
하지만 Python에서도 코루틴을 이용하면 비동기 코드를 작성할 수 있기 때문에, 코루틴을 비동기 함수라고도 부르는 것이다.
아래 그림은 동기 방식의 실행 흐름과 비동기 방식의 실행 흐름을 비교한 것이다.
```

```
사실 Python에서 코루틴은 제네레이터를 기반으로 구현된다. 즉, Python에서 코루틴은 곧 제네레이터인 것이다.
왜 제네레이터로 구현한 것일까?
그것은 제네레이터가 yield 키워드를 breakpoint로 삼아 실행이 중단 및 재개될 수 있는 특징을 가지고 있기 때문이다.
실제로 Python 3.5 이전 버전에서는 코루틴을 직접 제네레이터 기반으로 작성해야 했다. 
async 키워드는 그러한 제네레이터를 조금 더 쉽게 작성할 수 있도록 돕는 문법적인 설탕에 불과하다.
```

# 제네레이터의 실행 및 중단 (yield 키워드)
```
Caller는 제네레티어를 호출하여 제네레이터 객체(이하 gen)를 얻고, next(gen) 혹은 gen.send(값) 을 호출함으로써 해당 제네레이터를 실행한다.
그렇게 실행된 제네레이터는 yield 키워드를 마주치는 순간 자신의 실행과 관련되 상태(스택, 실행 위치 등)를 저장한 뒤 실행을 중단하고, Caller(yield 키워드의 뒤에 오는) 값을 넘겨준다.
그리고 이렇게 제어를 다시 넘겨받은 Caller가 다시 동일한 방법으로 해당 제네레이터를 실행하면, 해당 제네레이터는 아까 실행이 중단되었던 부분부터 다시 실행을 시작하게 된다.
이 때 만약 Caller가 gen.send(값)을 호출함으로써 해당 제네레이터를 사디 실행한 것이었다면, 아까 실행이 중단되었던 부분에 위치한 yield 키워드 구문의 자리에는 send() 메소드의 인자에 해당하는 값이
채워진다. 결국, yield 키워드는 제네레이터가 Caller에게 값을 넘겨주는 것이라면 gen.send(값)은 Caller가 제네레이터에게 값을 넘겨주는 것이다. 참고로, yield 키워드를 모두 소진한 제네레이터를
실행하는 경우 StopIteration 예외가 발생하며, 이 때 그 예외 객체의 value 필드에는 해당 제네레이터의 반환 값이 저장되어 있다.
```

- 따라서 제네레이터를 호출하면 제네레이터 객체(Generator Object)가 생성되어 반환되는 것처럼, 코루틴을 호출하면 제네레이터 객체와 유사한 코루틴 객체(Coroutine Object)라는 것이 생성되어 반환된다.

```
async def coroutine():
    print('coroutine')

coroutine()
# 출력 : <coroutine object async_func at 0x015A9540>
# 주의 : 'coroutine'이 출력되지는 않음(코루틴이 실행되진 않음).
```

# 제네레이터의 중첩 (yield from 키워드)
```
제네레티어가 다시 또 다른 제네레이터를 실행하는 것도 가능하다. yield from 키워드의 뒤에 또 다른 제네레이터에 해당하는 제네레이터 객체를 두면 된다.
이 구문이 의미하는 것은 현재 제네레이터의 실행을 중단하고 해당 제네레이터를 실행하라는 것이다.
그렇게 실행된 제네레이터가 어떠한 값을 yield 하면 Caller에 해당하는 제네레이터가 그 값을 받아서 그대로 yield 하는 효과를 보이며, 어떠한 값을 return 하면 Caller에 해당하는 제네레이터에서
실행이 중단되었던 부분에 위치한 yield from 키워드 구문의 자리에 그 값이 채워진다. 참고로, yield from 키워드의 뒤에는 제네레이터 객체뿐 아니라 __iter__() 메소드가 구현된 Iterable 객체라면
무엇이든지 올 수 있다. 이러한 경우에는 __iter__() 메소드를 호출하여 이터레이터 객체를 얻고 이를 통해 해당 이터레이터로부터 값을 하나씩 받는 방식으로 동작한다.
```

# 퓨처 객체(Future Object)

```
퓨처 객체는 어떠한 작업의 실행 상태 및 결과를 저장하는 객체이다. 여기서 말하는 실행 상태란 해당 작업이 진행 중인지, 취소되었는지, 종료되었는지를 말한다.
그래서 퓨처 객체는 PENDING, CANCELLED, FINISHED 의 세 가지 상태 중 하나를 가진다. 이때 작업의 완료(Done)라 함은 CANCELLED 혹은 FINISHED 상태를 가리킨다.
그리고 실행 결과라 함은 해당 작업의 결과 값 혹은 그 작업을 진행하면서 발생한 예외 객체를 말한다.
예외가 발생한 경우에도 FINISHED 상태가 된다는 것에 주의하자.

퓨처 객체의 중요한 메소드 중 하나는 add_done_callback()이다. 이 메소드를 호출하면 해당 퓨처 객체가 완료(Done)될 때 호출될 함수를 등록할 수 있다.
이 메소드는 뒤에서 이벤트 루프의 동작 원리를 설명할 때 매우 중요하므로 기억해두자.
```

# 태스크 객체(Task Object)
```
태스크(Task)는 퓨처(Future)를 상속하는 클래스이다.
즉, 태스크 객체는 기본적으로 퓨처 객체의 기능을 전부 가지고 있기 때문에, 퓨처 객체와 마찬가지로 어떠한 작업의 실행 상태 및 결과를 저장한다.
그러나 퓨처 객체와 다른 점은, 태스크 객체는 그 어떠한 작업의 실행을 개시하는 역할도 수행한다는 것이다.
이를 위해 필요한 것이 바로 코루틴 객체이다. 실제로 태스크 객체는 생성될 때 코루틴 객체를 넘겨받아 _coro 필드에 저장한다.
결국, 태스크 객체는 코루틴 객체를 갖고 있는 특별한 종류의 퓨처 객체라고 볼 수 있다.
다만, 코루틴 객체와 달리 코루틴을 호출한다고 해서 생성 및 반환되는 것은 아니며, 
태스크 객체를 생성하려면 asyncio.run() 함수 혹은 asyncio.create_task() 함수를 호출할 때 인자로 코루틴 객체를 넘겨줘야한다.

태스크 객체는 생성되는 즉시 현재의 쓰레드에 설정되어 있는 이벤트 루프에게 자신의 __step() 메소드를 호출해줄 것을 요청한다.
__step()은 자신의 코루틴 객체를 이용하여 해당 코루틴을 실행하는 메소드이다. 이것을 보고 '코루틴이 태스크로서 실행되도록 이벤트 루프에 예약을 건다'라고 표현한다.
뒤에서 알아보겠지만, asyncio.run() 함수 혹은 asyncio.create_task() 함수를 호출할 때 인자로 코루틴 객체를 넘겨주면 그 코루틴 객체로 태스크 객체가 생성되면서 해당 코루틴이 태스크로서 실행되도록 예약한다.

태스크 객체의 __step() 메소드가 호출되면 코루틴의 실행이 개시된다. 그렇게 처음 실행된 코루틴은 await 키워드를 이용하여 또 다른 코루틴을 부를 수 있고,
그 코루틴은 또다시 다른 코루틴을 부를 수도 있다. 이를 코루틴 체인(Coroutine Chain)이라고 부른다.
이처럼 하나의 태스크 객체는 현재의 태스크에 속하는 코루틴 체인의 실행을 관장하는 역할을 맡는다고 볼 수 있다.

이러한 연쇄 과정으로 코루틴을 호출하다 보면, 언젠가 Sleep 혹은 I/O 관련 코루틴(EX. asyncio.sleep() 등)을 await 하는 코드를 마주칠 수 있다.
태스크 객체는 이러한 상황을 감지하면 자신의 실행을 중단하고 이벤트 루프에게 제어를 넘긴다. 그 후 이벤트 루프는 자신에게 예약해둔 태스크들 중 우선순위가 높은 것을 적절히 선택하여 이를 실행시키게 되고,
시간이 흘러 아까 실행이 중단되었던 태스크가 다시 실행할 수 있는 상태가 되면 이 태스크는 다시 이벤트 루프에게 실행을 예약해둔다. 그러면 언젠가 이벤트 루프에 의해 다시 선택을 받아 실행할 수 있게 될 것이다.

한편, 태스크 객체가 처음 실행한 코루틴의 실행이 완료되면, 즉 해당 코루틴이 모든 yield 키워드를 소진한 상태에서 return 함으로써 StopIteration 예외가 발생하면, 그 객체로부터 반환 값을 얻어서
자기 자신(태스크 객체)의 결과 값을 업데이트한다. 이는 해당 태스크의 실행이 완료된 상황을 의미하며, 따라서 이 태스크는 이제 더 이상 이벤트 루프에 의해 실행이 예약될 수 없게 된다.
참고로 asayncio.run()함수가 실행되는 것은 이로 인해 실행된 태스크의 실행이 완료될 때까지를 의미하는 것이다.
```

# 이벤트 루프의 실행 흐름(동작 원리)
```
우선, 앞서 말했듯 코루틴을 호출하여 코루틴 객체가 생성 및 반환된다고 하여 해당 코루틴이 바로 실행되지 않는다는 것을 떠올리자.
그렇다면 코루틴을 실행시키는 코드는 무엇일까? Python에서 코루틴을 실행하는 방법은 대략 다음과 같이 세 가지이다.

1. await 키워드
2. asyncio.run() 함수
3. asyncio.create_task() 함수

이 중에서 await 키워드는 코루틴 내에서만 사용할 수 있기 때문에, 맨 처음 코루틴을 실행하는 용도로는 사용할 수 없다.
최초에 한 번 코루틴이 실행되고 나면, 그 코루틴부터 시작해서 await 키워드를 이용하여 다른 코루틴을 호출할 수는 있다.
그렇다면 남은 건 2번과 3번이다. 이들은 코루틴 바깥에서 처음으로 코루틴을 실행할 수 있는, 즉 코루틴 체인으로 들어가는 일종의 엔트리 포인트이다.

asyncio.run() 함수는 현재의 스레드에 새 이벤트 루프를 설정하고, 해당 이벤트 루프에서 인자로 넘어오는 코루틴 객체에 해당하는 코루틴을 태스크로 예약하여 실행시킨 뒤,
해당 태스크의 실행이 완료되면 이벤트 루프를 닫는 역할을 수행한다. (단, 이 함수는 3.7 버전 이상의 Python에서만 사용할 수 있다.)
```

```
loop = asyncio.get_event_loop()
loop.run_until_complete(first_coroutine())
loop.close()
```

# loop = asyncio.get_event_loop()
```
이는 현재 스레드에 설정된 이벤트 루프를 가져오는 함수이다. 그러나 만약 현재 스레드에 설정되어 있는 이벤트 루프가 없다면, 이벤트 루프를 새로 생성하여
이를 현재 스레드에 설정한 뒤 해당 이벤트 루프를 반환한다. 즉, 이 함수의 호출은 코루틴의 실행을 위해 이벤트 루프를 준비하는 과정으로 볼 수 있다.

이벤트 루프란, 무한 루프를 돌며 매 루프마다 작업(=task)을 하나씩 실행시키는 로직을 의미한다.
따라서 위에서 언급했던, 현재 스레드에 이벤트 루프를 설정한다 함은 단순히 '이벤트 루프라는 로직을 실행시킬 수 있는 객체를 생성한 것' 정도로 이해하면 된다.
이벤트 루프 객체를 이용하여 실제로 이벤트 루프를 실행시키는 것은 아래에서 설명할 run_until_complete() 메소드를 호출하는 순간부터이다.

그리고 여기서 말하는 작업이라는 것은 곧 앞서 소개했던 태스크 객체에 대응하는 태스크(Task)이다. 태스크라는 것은 하나의 코루틴에서부터 출발하는 하란의 실행 흐름으로 볼 수 있다.

아래는 이벤트 루프가 실행되는 흐름을 아주 간단하게 표현한 코드이다.
이벤트 루프 객체를 이용하여 실제로 이벤트 루프를 실행시키면 대략 이러한 코드가 실행되는 것으로 상상하면 된다.( 실제로는 훨씬 더 복잡할 것이다. )
```

```
While True:
    if task_queue:
        task_to_execute = task_queue.pop()
        task_to_execute.run()
    else:
        ehcek_is_IO_ready()
```

# loop.run_until_complete(first_coroutine())

```
앞서 생성한 이벤트 루프 객체를 이용하여 실제로 이벤트 루프를 실행시키는 함수이다.

1. 태스크의 실행(코루틴 체인의 형성)
인자로 넘어오는 코루틴 객체를 이용하여 태스크 객체를 생성하고, 그 과정에서 해당 태스크 객체가 나타내는 태스크의 실행이 이벤트 루프에 의해 즉시 예약된다.
처음에는 실행이 예약된 다른 태스크가 없기 때문에, 이벤트 루프는 이 태스크를 바로 실행할 것이다. 이 때 태스크의 실행이란, 해당 태스크 객체의 __step() 메소드를 호출하는 것을 의미한다.
이 메소드는 코루틴 객체(_coro 필드에 저장되어 있음)의 send() 메소드를 호출함으로써 해당 코루틴을 실행하는 역할을 수행한다. 
그러면 이 코루틴을 시작으로 await 키워드를 마주칠 때마다 연쇄적으로 코루틴을 호출하며 코루틴 체인을 형성하게 될 것이다.

2. 코루틴 체인의 종착점 (await {Sleep 또는 I/O 관련 코루틴 객체})
await 키워드를 통해 코루틴 체인을 형성하며 코루틴을 실행하다 보면, 언젠가 Sleep 혹은 I/O관련 코루틴(EX. asyncio.sleep() 등)을 await 하는 코드를 마주치게 될 것이다.
그런데 이러한 종류의 코루틴들은 퓨처 객체를 await 하도록 구현되어 있다.

예를 들어 I/O관련 코루틴이라고 해보자. 그러면 이 코루틴은 특정 소켓에 대해 데이터를 읽거나 쓰기 위해 해당 소켓의 상태를 검사한다.
만약 당장 읽거나 쓸 수 있는 데이터가 있다면, 단순히 yield 키워드만을 사용하여 태스크 객체의 __step() 메소드로까지 제어를 넘긴다.
그러면 태스크 객체는 바로 다시 자신의 실행을 이벤트 루프에게 예약하고 지금의 실행은 중단한 뒤 이벤트 루프에게 제어를 넘긴다.
이 때 테스크의 실행을 예약한다 함은 곧 해당 태스크 객체의 __step() 메소드를 이벤트 루프의 콜백 큐에 등록하는 것을 의미한다는 것을 기억해야한다.

그러나 보통은 당장 읽거나 쓸 수 있는 데이터가 있지 않다.
따라서 보통의 경우에는 select() 함수를 이용하여 해당 소켓을 등록해두고, 해당 소켓에 바인딩된 퓨처 객체를 새로 생성하여 await 한다.
퓨처 객체의 __await__() 메소드는 자기 자신(퓨처 객체)을 yield 하도록 구현되어 있기 때문에, 이로 인해 해당 퓨처 객체는 코루틴 체인을 따라 태스크 객체의 __step() 메소드로까지 전달될것이다.

* select() 함수 : Unix의 select() 함수를 래핑 한 Python 함수로, 특정 소켓들에 대해 데이터를 읽거나 쓸 준비가 될 때까지(원하는 시간만큼) 기다릴 수 있게 하는 Blocking 함수이다.
이는 (원하는 시간만큼) 기다린 후 데이터를 읽거나 쓸 준비가 된 소켓들을 반환한다.

Sleep 관련 코루틴의 경우, 이벤트 루프 자체의 타이머를 이용한다. 만약 asyncio.sleep(1) 이라면, 이 코루틴은 퓨처 객체를 하나 생성한 뒤 이벤트 루프에게는 1초 뒤에 해당 퓨처 객체의 결과 값을 업데이트하도록 요청한다.
그리고 그 퓨처 객체를 await 한다. 그러면 마찬가지로 해당 퓨처 객체가 코루틴 체인을 따라 테스크 객체의 __step() 메소드로까지 전달될 것이다. 그렇다면 이제 그렇게 전달된 퓨처 객체를 태스크 객체가 어떻게 처리할까?

3. 태스크 객체의 퓨처 객체 처리
태스크 객체는 yield 된 퓨처 객체를 받으면 우선 이것을 자신의 __fut_waiter 필드에 저장한다(바인딩한다). 그리고 퓨처 객체의 add_done_callback() 메소드를 호출하여, 해당 퓨처 객체가 완료 상태가 될 때 이벤트 루프에게 실행을 예약할 콜백 함수를 등록한다.
이 때 등록하는 함수는 곧 자기 자신의 __step() 메소드라고 생각해도 된다. 이러한 콜백 함수의 실행을 이벤트 루프에게 예약한다는 것은 곧 해당 태스크의 실행을 예약한다는 것과 같은 말이다.

그러고 나면 이제 태스크 객체는 자신의 실행을 중단하고 제어를 이벤트 루프에게 넘긴다.
그러면 지금과 같이 퓨처 객체에 바인딩되어 있는 태스크 객체는 더 이상 이벤트 루프에 의해 실행되지 못할 것이다.
__fut_waiter 필드의 이름이 나타내듯이, 어떠한 퓨처 객체를 기다리고 있을 때는 실행되면 안 되기 때문이다.
아무튼 그렇게 제어가 넘어가고 나면, 이벤트 루프는 다시 자신에게 실행을 예약해둔 태스크(정확히는 콜백 함수)들 중 우선순위가 높은 것을 적절히 선택하여 이를 실행시킨다.
이벤트 루프는 이러한 과정을 반복하며 여러 태스크들을 동시적으로(Concurrent, not Parallel) 실행하는 역할을 맡는다.

4. 이벤트 루프의 Polling(I/O  소켓 검사)
그런데 만약 더 이상 자신에게 실행을 예약해둔 태스크가 없게 되면, 이벤트 루프는 그 시간을 낭비하지 않고 select() 함수를 이용하여 데이터를 읽거나 쓸 준비가 된 소켓을 계속 찾는다.
만약 데이터를 읽거나 쓸 준비가 된 소켓을 찾게 되면, 그 소켓에 바인딩되어 있는 퓨처 객체의 결과 값을 업데이트해주고, 이로 인해 이 순간 아까 등록해두었던 콜백 함수의 실행이 이벤트 루프에서 예약될 것이다.
다시 강조하지만, 콜백 함수의 실행을 예약한다는 건 곧 해당 태스크의 실행을 예약한다는 말이다.

5. 태스크 객체의 실행 재개 (__step() 메소드 재실행)
그러면 이벤트 루프가 실행이 예약된 태스크를 실제로 실행시키는 과정을 한 번 살펴보자.
태스크의 실행이란 곧 해당 태스크 객체의 __step() 메소드가 호출되는 것을 의미한다.
이 메소드는 먼저 자기 자신(태스크 객체)과 퓨처 객체의 바인딩을 해제함으로써 더 이상 기다리는 퓨처 객체가 없음을 나타내도록 하고,
다시 자신의 코루틴 객체에 대해 send() 메소드를 호출함으로써 해당 코루틴의 실행을 재개하게 된다.
그러면 다시 해당 퓨처 객체의 __await()__ 메소드에서 실행이 중단되었던 부분(자기 자신을 yield 하는 부분) 까지 가게 된다.

__await()__ 메소드로까지 돌아왔을 때, 만약 I/O 관련 코루틴 때문에 기다리고 있었던 거라면 이제는 해당 소켓에 대해 데이터를 읽거나 쓸 준비가 되었다는 것이므로 해당 소켓(자기 자신에 바인딩되어 있음)에 대해 데이터를 읽거나 쓴 다음 그 값을 return 할 것이다.
반면에 Sleep 관련 코루틴 때문이었다면 바로 return 할 것이다.

6. 최초 코루틴의 Return(태스크 실행의 종료)
이러한 과정을 반복하다 보면 언젠가 태스크가 실행한 최초의 코루틴이 return 해야 하는 시점에 도달할 것이고, 이로 인해 해당 태스크 객체의 __step() 메소드에선 StopIteration 예외가 발생할 것이다.
그러면 태스크 객체는 그 예외 객체의 value 필드 값으로 자기 자신의 결과 값을 업데이트하고, 자신의 실행을 종료한다.
그러면 이 태스크는 더 이상 이벤트 루프에 의해 실행이 예약되지 않고 버려진다.
loop.run_until_complete() 함수의 실행이 끝나는 시점이 이때이다. 자신이 실행한 태스크가 종료되었기 때문이다.
그리고 그 태스크 객체의 결과 값이 곧 loop.run_until_complete() 함수의 반환 값이다.
```

# loop.close()
```
loop.run_until_complete() 함수의 실행이 끝났다는 것은 이제 해당 이벤트 루프가 실행되지 않는다는 것이다.
따라서 이벤트 루프를 닫아줘야 하는데, 이 역할을 수행하는 것이 loop.close() 함수이다.
이는 이벤트 루프에 남아 있는 모든 데이터(EX. 아직 실행이 종료되지 않은 태스크)들을 제거한다.
그래서 만약 loop.run_until_complete() 함수의 실행이 끝나고 loop.close() 에 의해 이벤트 루프까지 닫히는 시점에 여전히 실행이 완료되지 않은 태스크가 남아 있다면, 'Task was destroyed but it is pending!' 라는 워닝 메시지가 출력될 것이다.
```

# 태스크 동시 실행: asyncio.create_task() 함수
```
위에서 이벤트 루프가 태스크들을 동시적으로(Concurrent, not Parallel) 실행된다고 설명하였다.
그런데 사실 asyncio.run() 함수는 기본적으로 하나의 태스크만을 생성하여 실행한다.
따라서 코루틴 체인 과정에서 추가적인 태스크를 생성하여 실행하지 않았다면 현재의 태스크가 중단되었을 때 이벤트 루프는 실행시킬 다른 태스크가 없게 된다.
태스크가 한 개라면 동시적인(Concurrent) 실행을 하는 것이 애초에 말이 되지 않는 것이다.

* 여기서 말하는 동시 실행이란 Parallel이 아닌 Concurrent를 말한다. 즉, 엄밀한 의미의 동시가 아니라 여러 태스크들을 왔다 갔다 하며 한 스레드에서 실행하는 개념인 것이다.
따라서 총 실행 시간은 같거나 오히려 더 늘어난다(문맥 전환 비용 때문).

따라서 동시적인(Concurrent) 실행을 위해서는 asyncio.create_task() 함수를 호출함으로써 태스크를 추가로 생성하여 실행해야한다.
이 함수를 호출할 때 코루틴 객체를 인자로 넘기면, 해당 코루틴 객체를 이용하여 태스크 객체를 생성하고 이를 반환한다.
그리고 앞서 말했듯 태스크 객체가 생성되면 해당 태스크 객체가 나타내는 태스크의 실행이 이벤트 루프에 의해 즉시 예약된다(즉시 실행이 아니다).
단, 이 함수는 3.7 버전 이상의 Python에서만 사용할 수 있기 때문에, 그 이전 버전에서는 asyncio.ensure_future() 함수를 대신 사용해야 한다.

다음으로, 모든 퓨처 객체(태스크 객체 포함)들이 완료 상태가 될 때까지 기다리는 함수가 asyncio.gather()이다. 이 함수는 인자로 여러 개의 Awaitable 객체들을 받을 수 있는데, 만약 코루틴 객체를 받으면
이는 자동으로 태스크 객체로 래핑이 된다. 따라서 사실상 퓨처 객체(태스크 객체 포함)만 넘어간다고 생각해도 된다. 그리고 모든 퓨처 객체들이 완료 상태가 되면 그것들의 결과 값들을 리스트 형태로 반환한다.
그 순서는 인자로 넘긴 순서와 동일하다. 이 함수는 await 키워드의 뒤에서 호출될 수 있는 코루틴의 일종이다.

아래는 예시 코드이다.
```

```
import asyncio
import time

async def sleep(sec):
    await asyncio.sleep(sec)
    return sec

async def main():
    sec_list = [1, 2]
    tasks = [asyncio.create_task(sleep(sec)) for sec in sec_list]
    tasks_results = await asyncio.gather(*tasks)
    return tasks_results

start = time.time()

loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
loop.close()

end = time.time()

print('result : {}'.format(result))
print('total time : {0:.2f} sec'.format(end - start))

# 출력 결과
# result : [1, 2]
# total time : 2.00 sec
```

```
위 예시 코드의 실행 흐름 순서

1. loop_run_until_complete() 함수에 의해 Task 0가 실행되고, 이로 인해 main() 코루틴이 실행된다.
2. main() 코루틴은 asyncio.create_task() 함수를 통해 Task 1, Task 2 객체를 생성하고 실행을 예약한다.
3. asyncio.gather() 코루틴은 Task1 객체를 await 한다.
4. Task 0는 Task 1 객체가 완료 상태가 될 때까지 기다리도록 하고, 이벤트 루프에게 제어를 넘긴다.
5. 이벤트 루프가 Task 1을 실행한다.
6. Task 1은 sleep(1) 코루틴을 실행하고, 다시 asyncio.sleep(1) 코루틴을 실행한다.
7. asyncio.sleep(1) 코루틴은 Future 1 객체를 만들고, 1초 뒤에 Future 1 객체의 결과 값이 갱신되도록 이벤트 루프에 예약을 건 뒤, Future 1 객체를 await 한다.
8. Task 1은 Future 1 객체가 완료 상태가 될 때까지 기다리도록 하고, 이벤트 루프에게 제어를 넘긴다.
9. 이벤트 루프가 Task 2를 실행한다.
10. Task 2는 sleep(2) 코루틴을 실행하고, 다시 asyncio.sleep(2) 코루틴을 실행한다.
11. asyncio.sleep(2) 코루틴은 Future 2 객체를 만들고, 2초 뒤에 Future 2 객체의 결과 값이 갱신되도록 이벤트 루프에 예약을 건 뒤, Future 2 객체를 await 한다.
12. Task 2는 Future 2 객체가 완료 상태가 될 때까지 기다리도록 하고, 이벤트 루프에게 제어를 넘긴다.
13. 이제 이벤트 루프는 실행할 태스크가 없으므로 아무것도 하지 않는다.
14. 그러다가 1초가 지나면 이벤트 루프는 Future 1 객체의 결과 값을 갱신한다. 이로 인해 Future 1 객체가 완료 상태가 될 때까지 기다리던 Task1 의 실행이 다시 예약된다.
15. 이벤트 루프가 Task 1을 실행한다.
16. asyncio.sleep(1) 코루틴으로 돌아가서 실행이 중단되었던 부분부터 실행을 재개한다.
17. asyncio.sleep(1) 코루틴이 리턴하고, sleep(1) 코루틴도 리턴한다. 이때 반환 값은 1이다.
18. Task 1 객체의 결과 값이 1로 설정되면서 Task 1의 실행이 완료된다. 이로 인해 Task 1 객체가 완료 상태가 될 때까지 가디리던 Task 0 의 실행이 다시 예약된다.
19. 이벤트 루프가 Task 0를 실행한다.
20. asyncio.gather() 코루틴으로 돌아가서 실행이 중단되었던 부분부터 실행을 재개한다.
21. asyncio.gather() 코루틴은 Task 1 객체의 결과 값을 저장하고, Task 2 객체를 await한다.
22. Task 0는 Task 2 객체가 완료 될 때까지 기다리도록 하고, 이벤트 루프에게 제어를 넘긴다.
23. 이제 이벤트 루프는 실행할 테스크가 없으므로 아무것도 하지 않는다.
24. 그러다가 1초가 더 지나면 이벤트 루프는 Future 2 객체의 결과 값을 갱신한다. 이로 인해 Future 2 객체가 완료 될 때까지 기다리던 Task 2의 실행이 다시 예약된다.
25. 이벤트 루프가 Task 2를 실행한다.
26. asyncio.sleep(2) 코루틴으로 돌아가서 실행이 중단되었던 부분부터 실행을 재개한다.
27. asyncio.sleep(2) 코루틴이 리턴하고, sleep(2) 코루틴도 리턴한다. 이 때 반환 값은 2이다.
28. Task 2 객체의 결과 값이 2로 설정되면서 Task 2 의 실행이 완료된다. 이로 인해 Task 2 객체가 완료 상태가 될 때까지 기다리던 Task 0의 실행이 다시 예약된다.
29. 이벤트 루프가 Task 0를 실행한다.
30. asyncio.gather() 코루틴으로 돌아가서 실행이 중단되었던 부분부터 실행이 재개한다.
31. asyncio.gather() 코루틴은 [Task1 객체의 결과 값, Task 2 객체의 결과 값], 즉 [1, 2]를 리턴한다.
32. main() 코루틴도 리턴한다. 이 때 반환 값은 [1, 2]이다.
33. Task 0 객체의 결과 값이 [1, 2]로 설정되면서 Task 0의 실행이 완료된다.
34. loop.run_until_complete()의 실행이 완료되고, 이벤트 루프를 닫는다.
```
# 동기 함수를 코루틴처럼 쓰기: loop.run_in_executor() 메소드
```
우리가 지금까지 알아본 원리에 따르면, 결국 비동기 프로그래밍의 효과를 보기 위해서는 현재의 쓰레드 실행과 무관하게 다른 곳에서 어떠한 작업을 할 수 있어야 한다.
그 대표적인 예시가 Sleep 혹은 I/O 관련 코루틴이었다. Sleep의 경우에는 이벤트 루프가 자체적으로 타이머를 가지고 있기 때문에, 그리고 I/O 관련 코루틴은 CPU가 열심히 일하는 동안 I/O 장치가 일해주면 되기 때문에 현재의 실행 흐름을 Block 하지 않고 다른 작업을 먼저 할 수 있었던 것이다.

그런데 사실 Python이 가지고 있는 대부분의 API는 동기 방식으로 동작한다. 애초에 동기 방식으로 동작하도록 설계된 언어이기 때문이다.
예를 들어, asyncio.sleep() 함수가 제공되기 전에는 time.sleep() 함수를 사용했는데, 이는 현재의 실행 흐름을 Block 하는 함수였다.
그리고 requests 라이브러리가 제공하는 reqests.get(), requests.post() 등의 함수도 현재의 실행 흐름을 Block하는 함수이다.
이러한 함수들을 이용해서는 비동기 프로그래밍이 불가능할 듯하다. 비동기 프로그래밍이 가능하려면 그러한 작업을 다른 어딘가에 맡겨 놓고 퓨처 객체를 await 하면서 현재 실행 중인 태스크의 제어를 이벤트 루프에게 넘겨야 하기 때문이다.

이 때 사용하는 것이 바로 loop.run_in_executor() 메소드이다. loop는 이벤트 루프 객체이다. 어렵게 설명하면 한도 끝도 없겠지만, 간단하게 얘기해서 이 메소드는 동기 함수를 별도의 쓰레드에서 실행시킴으로써 마치 Sleep 혹은 I/O 관련 코루틴처럼 사용할 수 있게 해주는 것이다.
비동기 프로그래밍을 하려면 어떤 작업을 '다른 어딘가(=별도의 쓰레드)'에 맡겨야 하기 때문이다.
```

```
import asyncio
import time

async def sleep(sec):
    pass

async def main():
    pass

start = time.time()

loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
loop.close()

end = time.time()

print('result : {}.format(result))
print('total time : {0:.2f} sec'.format(end - start))

# 출력 결과
# result : [1, 2]
# total time : 2.03 sec
```

``` 
원래는 Blocking 함수인 time.sleep() 함수가 마치 asyncio.sleep() 함수처럼 동작할 수 있도록 하였다.
loop.run_in_executor() 메소드의 첫 번째 인자로 넘어가는 None은 실행기를 명시적으로 지정하지 않고 기본 실행기를 사용하겠다는 것인데, 직접 실행기를
지정하면 워커 쓰레드를 원하는 개수만큼 생성하는 것이 가능하다. 두 번째 인자에는 함수 이름을 넘기고, 세 번째 인자부터는 그 함수를 호출할 때 넘길 인자들을 하나씩 넘기면 된다.

* 만약 단일 코어 CPU라면 멀티 쓰레딩을 하더라도 병렬(Parallel) 실행이 불가하다. 병렬 실행을 하려면 멀티 코어여야 한다.
```

# 병렬 처리 concurrent future
```
파이썬 제약: GIL
Python은 두 개 이상의 스레드가 동시에 실행될 때 두 개 이상의 스레드가 하나의 자원을 동시에 엑세스할 때 발생할 수 있는 문제점을 방지하기 위해 GIL(Global Interpreter Lock)이라는 것을 도입했다.
즉, 스레드가 실행될 때, 프로그램 내의 리소스 전체에 락이 걸린다.
결국 Python 구현에서는 동시에 몇 개의 스레드가 실행이 되던 간에 GIL에 의해서 한 번에 하나의 스레드만 실행된다.
멀티 스레드의 경우 문맥교환(Context Switch)에 필요한 리소스까지 고려하면 단일 스레드보다 성능이 떨어지게 되는 것을 확인할 수 있다.
```

# concurrent.future 모듈
```
concurrent.futures 모듈은 별도 규격의 스레드 객체를 작성하지 않고 함수 호출을 객체화하여 다른 스레드나 다른 프로세스에서 이를 실행할 수 있게 해준다.
이 때 중심 역할을 하는 것이 Executor 클래스이다. Executor 클래스는 다시 ThreadPoolExecutor와 ProcessPoolExecutor로 나뉘는데 두 클래스의 차이는 동시성 작업을 멀티 스레드로 처리하느냐,
멀티 프로세스로 처리하느냐만 있지 거의 동일한 기능을 제공한다.
```

# future
```
executor를 이용한 동시성 처리는 호출해야 할 함수와 그에 전달될 인자들을 executor에 넘겨주는 것으로 시작되는데, executor의 해당 메소드는 다른 스레드의 리턴을 기다릴 필요가 없으므로 바로 리턴하게 된다.
이 때 리턴되는 객체가 Future 객체이며, 이 객체의 상태를 조사하여 완료 여부를 확인하거나, 해당 객체 내 작업이 완료되기를 기다리거나 혹은 미리 콜백을 넘겨놓아둘 수도 있다.
이 객체는 asyncio의 Future 클래스와 유사한 API를 가지고 있다. (둘이 호환되는 객체는 아니다.)

ex)
    1. 실행중인 병렬 작업을 취소
    2. 실행 중 여부, 완료 여부의 체크
    3. 특정 타임아웃 시간 후의 결과값 확인
    4. 완료 콜백을 추가
    5. 동기화 코드를 매우 쉽게 작성 가능

단일 스레드 비동기 코루틴을 사용하는 방식과 concurrent.futures를 이용한 병렬처리 방식은 매우 비슷한 형태로 사용 가능하다.

이 Future 클래스는 자바스크림트의 Promise API와 매우 비슷하다.
아직 완료되지 않은 (혹은 완료되었는지 당장은 모르는) 작업을 외부에서 객체로 다룰 수 있게 된다.
다음의 메소드들이 지원된다.
특히 하나의 작업에 대해서 하나 이상의 완료 콜백을 추가할 수 있다는 점이 흥미롭다.

- cancle(): 작업 취소를 시도한다. 만약 현재 실행중이고 취소가 불가능할 경우 False을 리턴한다. 작업이 취소되었다면 True가 리턴된다.
- canceled(): 취소가 완료된 작업이면 True를 리턴한다.
- done(): 작업이 완료되었고 정상적으로 종료되었다면 True를 리턴한다.
- result(): 해당 호출의 결과를 리턴한다. 만약 작업이 아직 완료되지 않았다면 최대 타임아웃시간까지 기다린다음, None을 리턴한다.
- exception(): 해당 호출이 던진 예외를 반환한다. 역시 작업이 안료되지 않았다면 타임아웃 시간까지 기다린다.
- add_done_callback(): 콜백함수를 Future 객체에 추가한다. 이 함수는 future 객체하나를 인자로 받는 함수이다. 콜백은 취소되거나 종료된 경우에 모두 호출된다.

모듈 함수(wait.as_completed)
wait: 특정한 타임아웃 시간 동안 대기한 다음, 그 시간동안 완료된 작업과 그렇지 않은 작업을 구분하는 두 개의 세트로 된 튜플을 리턴한다. result.done, result.not_done

as_completed: future의 집합을 받아서 기다리면서 하나씩 완료되는 것 순서대로 순회하면서 반복하는 반복자를 생성하는 함수이다. executor의 map과 차이점으로는 완료되는 순서대로 순회가 가능하다.
```

# executor
```
Executor 객체는 풀 기반으로 작업을 관리한다. 초기화 시에 몇 개의 worker가 사용될 것인지를 정해주면 전달되는 작업들을 큐에 넣고 worker pool에서 사용 가능한 worker로 하여금 작업을 처리하게 한다.
병렬 작업을 dispatch하며 thread나 process를 관리
Executor 객체는 컨텍스트 매니저 프로토콜을 지원하기 때문에 with 구문 내에서 사용할 수 있다.

submit(fn, *args, **kwargs)
함수 fn에 대해 주어진 인자들을 전달하여 실행할 수 있는 Future 객체를 리턴한다. 해당 함수는 호출 즉시 스케줄링된다.
```

```
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pw, 323, 1235)
    print(future.result())
```

```
map(func, *iterables, timeout=None)
일반함수 map과 동일하나, 각 호출은 병렬적으로 일어난다. 만약 타임아웃 값이 지정된 경우, 맵핑 작업이 완료되지 않은 호출이 있으면 TimeoutError가 일어난다.
타임 아웃 값을 별도로 주지 않으면 디스패치된 모든 작업들이 종료될 때까지 기다린 후 리턴한다.
타임아웃 값이 주어진 경우에는 해당 타임아웃 내에 완료되지 못한 작업이 있을 때, 예외를 일으키게 된다.

입력 데이터와 동작 함수를 짝지어서 바로 스케줄링하도록 한다. map()함수는 이터레이터를 리턴하는데, 이는 각 개별 작업이 동시에 실행 된 후, 먼저 종료된 작업부터 내놓는 리턴값을 내놓게 된다.
(결과값은 특이하게 [Futures] 타입이 아닌 결과에 대한 제네레이터이다.)
호출은 비동기적으로 발생하며, 결과값이 생성되는 순서가 반드시 호출이 시작된 순서와 동일하지는 않다.
결과 list는 iterable이 전달된 순서대로 저장 되는 것이 as_completed()와의 차이점

shutdown(wait=True)
executor에게 종료 시그널을 보낸다. 시그널을 받은 executor는 실행 중 및 대기 중인 모든 future에 대해 리소스를 정리한다.
shutdown 후에 submit이나 map을 호출하면 런타임에러가 발생한다. 만약 wait 값이 True로 정해지면 진행 및 대기중이던 작업이 종료된 후에 shutdown이 일어나고, 그 때까지 해당 함수는 리턴을 보류하게 된다.
(만약 강제 shutdown을 피하고 싶다면 with 구문 내에서 사용한다.)
```

# Executor의 구분 - 스레드 vs 프로세스

```
Executor는 멀티스레드를 쓸 것이냐, 멀티프로세스를 쓸 것이냐에 따라 ThreadPoolExecutor와 ProcessPoolExecutor로 나뉜다.
둘의 사용방법은 거의 동일하나 다음과 같은 차이가 있다.

IO기반의 작업에 대해서 대기 시간을 줄이고 리소스 사용 효율을 늘리고 싶다면 ThreadPoolExecutor를 사용한다.
예를 들어 HTTP통신을 이용하여 여러 곳을 순차적으로 접근하는 것보다, 멀티 스레드를 이용하면 전반적인 성능향상을 볼 수 있다.
CPU 부하가 많은 작업을 분산처리 하는 목적이라면 ProcessPoolExecutor를 사용한다. 
CPU 로드가 크게 걸리는 작업인 경우에는 파이썬 내에서는 GIL(Grand Interal Lock)이라는 제약이 존재하기 때문에, 멀티 스레드로는 CPU 분산 처리의 효과를 누릴 수 없다.
멀티 프로세스는 서브 프로세스와 유사하게 __main__ 스르로를 반입하는 별도의 프로세스를 가지므로, 이를 호출하는 코드는 반드시 __main__ 모듈 내에서 호출되어야 한다.
아래 코드 참조..
```
```
from concurrent import futures
import urllib.request

URLS = ['http://www.foxnews.com/,
        'http://www.cnn.com/,
        'http://some-made-up-domain.com/]

def load_url(url, timeout):
    return urllib.request.urlopen(url, timeout=timeout).read()

def main():
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = dict(
            (executor.submit(load_url, url, 60), url)
             for url in URLS)
        for future in futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                print('%r page is %d bytest' % (
                        url, len(future.result())))
            except Exception as e:
                print('%r generated an exception: %s' %(
                        url, e))

if __name__ == '__main__':
    main()
```

# 본격적인 event loop
```
asyncio에서는 coroutine과 event loop를 사용하여 비동기 프로그래밍을 지원한다.
다른 언어에서와 마찬가지로 event loop는 task들을 loop를 돌면서 하나씩 실행시키는 역할을 한다.
만약 실행된 task가 특정한 데이터를 요청하고 응답을 대기해야 한다면 이 task는 제어권을 다시 event loop에 넘겨준다.
제어권을 받은 event loop는 다음 task를 실행하게 되고, 응답을 받은 순서대로 task queue에 들어가고 재개되는 task들은 멈췄던 부분부터 다시 제어권을 가지고 작업을 마무리한다.
# 여기서 coroutine이 응답을 대기하는 상태에서 제어권을 event loop로 주는 용도로 await를 사용한다.

coroutine으로 task를 만들고, asyncio.get_event_loop()를 통해 event loop 객체를 얻어 오고, run_until_complete() method를 통해 실행시킬 수 있다.
run_until_completed()는 parameter로 Future 객체를 받는데, coroutine을 받으면 task로 실행되도록
내부적으로 설계되어 있다. task를 추가하는 방법으로는 event loop객체의 create_task() method를 이용할 수 있다.

coroutine을 실행시키는 방법으로는 다음과 같다.
- await 키워드 (coroutine내에서만 사용할 수 있으므로, 처음 coroutine을 실행하는 용도로는 사용X)
- asyncio.run(), asyncio.create_task(): 이들이 coroutine cchain으로 들어가는 일종의 entry point

asyncio.run() method는 현재 thread에서 새 event loop를 설정하고, 해당 event loop에서 인자로 넘어오는
coroutine 객체에 해당하는 task를 예약하여 실행시킨 뒤, 실행이 완료되면 event loop를 닫는 역할을 수행

asyncio.run 함수는 전달된 코루틴을 실행하고, asyncio 이벤트 루프와 비동기 제네레이터의 파이널리제이션을 관리한다.
다른 asyncio 이벤트 루프가 같은 스레드에서 실행중일 때, 이 함수를 호출할 수 없다.
이 함수는 항상 새 이벤트 루프를 만들고 끝에 이벤트 루프를 닫는다.
asyncio 프로그램의 메인 진입 지점으로 사용해야 하고, 이상적으로는 한 번만 호출해야 한다.
```

# asyncio.get_event_loop
```
현재 thread에 설정된 event loop를 가져오는 함수이다. 만약 thread에 설정된 event loop가 없다면 새로 생성하여
이를 현재 thread에 설정한 뒤 event loop를 반환한다. 이 method는 coroutine실행을 위해 event loop를 준비하는 과정 event loop를 다시 설명하면, 무한 루프를 돌며 매 루프마다 task를 하나씩 실행시키는 로직이다.

task는 하나의 coroutine에서 출발하는 하나의 실행 흐름으로 coroutine chain과 연관되어 있다.
```

# loop.run_until_completed
```
0. Task의 생성
- 고수준 asyncio.create_task()를 사용하거나 저수준 loop.create_task(), loop.ensure_future() method 사용

1. Task의 실행 (coroutine chain형성)
인자로 넘어오는 coroutine 객체를 이용하여 task객체를 생성하고, event loop에 의해 즉시 예약된다.
예약된 task가 없다면 event loop는 해당 task를 즉시 실행할 것이다. 
task의 실행이란 해당 task 객체의 __step__() method를 실행시키는 것을 의미한다.
이 method는 coroutine객체(_coro 필드에 저장)의 send() method를 호출함으로써 해당 coroutine을 실행하는
역할을 수행한다. 그러면 이 coroutine을 시작으로 await 키워드를 마주칠 때 마다 연쇄적으로 coroutine을 호출하며
coroutine chain을 형성한다.

2. coroutine chain의 종착점
await를 통해 coroutine을 실행하다 보면, sleep혹은 I/O 관련 coroutine을 await하는 코드를 마주치게 된다.
이러한 종류의 coroutine들은 Future 객체를 await하도록 구현되어 있다. (coroutine chain 끝에서 return으로 await를 안 마주칠 수도 있다. 이러한 경우 __step() method에서 StopIteration 예외 발생하면서 task 종료.)

# I/O 또는 sleep coroutine 처리 방식
예를 들어 I/O 관련 코루틴이라고 해보자. 그러면 이 코루틴은 특정 소켓에 대해 데이터를 읽거나 쓰기 위해 해당 소켓의 상태를 검사한다. 만약 당장 읽거나 쓸 수 있는 데이터가 있다면, 단순히 yield 키워드만을 사용하여 태스크 객체의 __step() 메소드로까지 제어를 넘긴다. 그러면 태스크 객체는 바로 다시 자신의 실행을 이벤트 루프에게 예약하고 지금의 실해은 중단한 뒤 이벤트 루프에게 제어를 넘긴다. 이 때 테스크의 실행을 예약한다 함은 곧 해당 태스크 객체의 __step() 메소드를 이벤트 루프의 콜백 큐에 등록하는 것을 의미한다는 것을 기억하자.

그러나 보통은 당장 읽거나 쓸 수 있는 데이터가 있지 않다.
따라서 보통의 경우에는 select() 함수를 이용하여 해당 소켓을 등록해두고, 해당 소켓에 바인딩된 퓨처 객체를 새로 생성하여 await 한다. 퓨처 객체의 __await__() 메소드는 자기 자신(퓨처 객체)을 yield 하도록 구현되어 있기 때문에, 이로 인해 해당 퓨처 객체는 코루틴 체인을 따라 태스크 객체의 __step() 메소드로까지 전달될 것이다.

* select() 함수: Unix의 select() 함수를 래핑 한 Python 함수로, 특정 소켓들에 대해 데이터를 읽거나 쓸 준비가 될 때까지 (원하는 시간만큼) 기다릴 수 있게 하는 Blocking 함수이다. 이는 (원하는 시간만큼) 기다린 후 데이터를 읽거나 쓸 준비가 된 소켓들을 반환한다.

Sleep 관련 코루틴의 경우, 이벤트 루프 자체의 타이머를 이용한다. 만약 asyncio.sleep(1) 이라면, 이 코루틴은 퓨처 객체를 하나 생성한 뒤 이벤트 루프에게는 1초 뒤에 해당 퓨처 객체의 결과 값을 업데이트하도록 요청한다. 그리고 그 퓨처 객체를 await한다. 그러면 마찬가지로 해당 퓨처 객체가 코루틴 체인을 따라 테스크 객체의 __step() 메소드로까지 전달될 것이다.
```

# Task 객체의 Future 객체 처리
```
태스크 객체는 yield 된 퓨처 객체를 받으면 우선 이것을 자신의 __fut_waiter 필드에 저장한다(바인딩한다).
그리고 퓨처 객체의 add_done_callback() 메소드를 호출하여, 해당 퓨처 객체가 완료 상태가 될 때 이벤트 루프에게
실행을 예약할 콜백 함수를 등록한다. 이 때 등록하는 함수는 곧 자기 자신의 __step() 메소드라고 생각해도 된다.
이러한 콜백 함수의 실행을 이벤트 루프에게 예약한다는 것은 곧 해당 태스크의 실행을 예약한다는 것과 같은 말이다.

그러고 나면 이제 태스크 객체는 자신이 실행을 중단하고 제어를 이벤트 루프에게 넘긴다.
그러면 지금과 같이 퓨처 객체에 바인딩되어 있는 태스크 객체는 더 이상 이벤트 루프에 의해 실행되지 못할 것이다.
__fut_waiter 필드의 이름이 나타내듯이, 어떠한 퓨처 객체를 기다리고 있을 때는 실행되면 안 되기 때문이다.
아무튼 그렇게 제어가 넘어가고 나면, 이벤트 루프는 다시 자신에게 실행을 예약해둔 태스크(정확히는 콜백 함수)들 중
우선순위가 높은 것을 적절히 선택하여 이를 실행시킨다. 이벤트 루프는 이러한 과정을 반복하며 여러 태스크들을 동시적으로(Concurrent, not Parallel) 실행하는 역할을 맡는다.
```

# Event loop의 Polling (I/O 소켓 검사)
```
그런데 만약 더 이상 자신에게 실행을 예약해둔 태스크가 없게 되면,
이벤트 루프는 그 시간을 낭비하지 않고 select() 함수를 이용하여 데이터를 읽거나 쓸 준비가 된 소켓을 계속 찾는다.
만약 데이터를 읽거나 쓸 준비가 된 소켓을 찾게 되면, 그 소켓에 바인딩되어 있는 퓨처 객체의 결과 값을 업데이트 해주고, 이로 인해 이 순간 아까 등록해두었던 콜백 함수의 실행이 이벤트 루프에서 예약될 것이다.
다시 강조하지만, 콜백 함수의 실행을 예약한다는 건 곧 해당 태스크의 실행을 예약한다는 말이다.
```

# Task 객체의 실행 재개 (__step() 메소드 재실행)
```
태스크의 실행이란 곧 해당 태스크 객체의 __step() 메소드가 호출되는 것을 의미한다.
이 메소드는 먼저 자기 자신(태스크 객체)과 퓨처 객체의 바인딩을 해제함으로써 더 이상 기다리는 퓨처 객체가 없음을 
나타내도록 하고, 다시 자신의 코루틴 객체에 대해 send() 메소드를 호출함으로써 해당 코루틴의 실행을 재개하게된다.
그러면 다시 해당 퓨처 객체의 __await()__ 메소드에서 실행이 중단되었던 부분(자기 자신을 yield 하는 부분)까지 가게 된다.

__await()__ 메소드로까지 돌아왔을 때, 만약 I/O 관련 코루틴 때문에 기다리고 있었던 거라면 이제는 해당 소켓에 대해
데이터를 읽거나 쓸 준비가 되었다는 것이므로 해당 소켓(자기 자신에 바인딩되어 있음)에 대해 데이터를 읽거나 쓴 다음 그 값을 return 할 것이다. 반면에 Sleep 관련 코루틴 때문이였다면 바로 return 할 것이다.
```

# 최초 coroutine의 return (태스크 실행의 종료)
```
이러한 과정을 반복하다 보면 언젠가 태스크가 실행한 최초의 코루틴이 return 해야 하는 시점에 도달할 것이고, 이로 인해 해당 태스크 객체의
__step() 메소드에선 StopIteration 예외가 발생할 것이다. 그러면 태스크 객체는 그 예외 객체의 value 필드 값으로 자기 자신의 결과 값을 업데이트 하고, 자신의 실행을 종료한다. 그러면 이 태스크는 더 이상 이벤트 루프에 의해 실행이 예약되지 않고 버려진다. loop.run_until_complete() 함수의 실행이 끝나는 시점이 이때이다. 자신이 실행한 태스크가 종료되었기 때문이다. 그리고 그 태스크 객체의 결과 값이 곧 loop.run_until_complete() 함수의 반환 값이다.
```

# loop.close()
```
loop.run_until_complete() 함수의 실행이 끝났다느 것은 이제 해당 이벤트 루프가 실행되지 않는다는 것이다.
따라서 이벤트 루프를 닫아줘야 하는데, 이 역할을 수행하는 것이 loop.close() 함수이다.
이는 이벤트 루프에 남아 있는 모든 데이터(EX. 아직 실행이 종료되지 않은 태스크)들을 제거한다.
그래서 만약 loop.run_until_complete() 함수의 실행이 끝나고 loop.close()에 의해 이벤트 루프까지 닫히는 시점에 여전히 실행이 완료되지
않은 태스크가 남아있다면, 'Task was destroyed but it is pending!'라는 워닝 메시지가 출력될 것이다.
```

# Task 동시 실행 - asyncio.create_task()
```
사실 asyncio.run() 함수는 기본적으로 하나의 태스크만을 생성하여 실행한다.
따라서 코루틴 체인 과정에서 추가적인 태스크를 생성하여 실행하지 않았다면 현재의 태스크가 중단되었을 때 이벤트 루프는 실행시킬 다른 태스크가 없게 된다. 태스크가 한 개라면 동시적인(Concurrent) 실행을 하는 것이 애초에 말이 되지 않는 것이다.

* 여기서 말하는 동시 실행이란 Parallel이 아닌 Concurrent를 말한다. 즉, 엄밀한 의미의 동시가 아니라 여러 태스크들을 왔다 갔다 하며
한 스레드에서 실행하는 개념인 것이다. 따라서 총 실행 시간은 같거나 오히려 늘어난다(문맥 전환 비용 때문).

따라서 동시적인(Concurrent) 실행을 위해서는 asyncio.create_task() 함수를 호출함으로써 태스크를 추가로 생성하여 실행해야 한다.
이 함수를 호출할 때 코루틴 객체를 인자로 넘기면, 해당 코루틴 객체를 이용하여 태스크 객체를 생성하고 이를 반환한다.
그리고 앞서 말했듯 태스크 객체가 생성되면 해당 태스크 객체가 나타내는 태스크의 실행이 이벤트 루프에 의해 즉시 예약된다(즉시 실행이 아니다).
예약 후에는 Task 객체를 반환한다.

다음으로, 모든 퓨처 객체(태스크 객체 포함)들이 완료 상태가 될 때까지 기다리는 함수가 asyncio.gather()이다.
이 함수는 인자로 여러 개의 Awaitable 객체들을 받을 수 있는데, 만약 코루틴 객체를 받으면 이는 자동으로 태스크 객체로 래핑이된다.
따라서 사실상 퓨처 객체(태스크 객체 포함)만 넘어간다고 생각해도 된다. 그리고 모든 퓨처 객체들이 완료 상태가 되면 그것들의 결과 값들을
리스트 형태로 반환한다.
그 순서는 인자로 넘긴 순서와 동일하다.
이 함수는 await 키워드의 뒤에서 호출될 수 있는 코루틴의 일종이다.
```