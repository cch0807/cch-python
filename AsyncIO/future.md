# Future란?
Future는 Python에 국한된 개념이 아니라 비동기 프로그래밍에서 널리 사용되는 개념이며, 주로 비동기 연산의 결과를 저장하는 객체를 나타낸다.
동기 함수라면 함수가 blocking 후 종료했을 때 결과를 반환하기 때문에 그 값을 사용하면 된다. 하지만 비동기 함수의 경우, 호출하는 곳에서 의도적으로 연산 종료를 기다리지 않는 이상 반환 값을 바로 받아볼 수 없다. 그래서 Future는 비동기 함수가 호출한 곳에 "지금은 반환 값이 없는데 나중에 이곳에 값을 채워줄게" 라는 목적으로 만들어서 주는 것이다.

# 꼭 Future를 알아야할까?
Future 객체를 외부에 노출하는 것은 권장되지 않기 때문에 고수준에서만 asyncio를 사용하면 Future를 만날 기회가 적다. 하지만 비동기 프로그래밍에서 중요한 개념이고, 저수준에서 asyncio를 다루려면 필수적으로 알아야 효율적인 코드를 작성할 수 있다.

# Python에서의 Future
Python에는 사실 2개의 서로 다른 Future 클래스가 있다. 하나는 concurrent.futures.Future이고, 다른 하나는 asyncio.Future이다. 이후에 등장하는 모든 Future는 후자이다. 두 클래스는 서로 다른 시기에 다른 목적을 위해 만들어졌기 때문에 서로 호환되지 않는다. 대신 asyncio.wrap_future() 를 이용하면 전자를 후자로 바꿀 수 있다.

# asyncio에서의 Future
asyncio 모듈에서 Future가 직접 노출되는 부분은 적다.
loop.create_future()와 asyncio.create_task()가 가장 흔한데, 후자는 Eventloop에 코루틴을 등록하는 역할을 하므로 실제로 조작하는 경우는 흔치 않다.

# Future의 기능
- Awaitable이기 때문에 await 키워드로 결과를 기다릴 수 있음
- done()으로 연산이 끝났는지 확인 가능
- set_result()로 연산의 결과를 지정
- cancel()로 연산 취소 가능
- add_done_callback()으로 콜백함수 등록 가능

# Future에 추가된 콜백함수는 언제 어떤 순서로 호출될까?
Future는 Eventloop에서 자신에게 최적화된 구현체를 가질 수 있기 때문에 어떤 규칙을 보장받을 순 없을 것 같다. 다만 기본 구현체는 콜백 등록에 loop.call_soon() 메소드를 사용하고 있는데, Future 실행이 끝난 이후에 다음 Eventloop iteration에 콜백 함수 실행을 등록하며, 콜백함수가 등록된 순서대로 실행을 시작할 것 같다. 결론적으로 명세상 보장받을 수 없고, 순서나 시점을 보장받아야 하는 경우 별도의 장치가 필요하다.

# async 함수(코루틴 함수)를 콜백으로 등록하고 싶으면 어떻게 해야 할까?
Future.add_done_callback()은 코루틴 함수가 아닌 일반 함수를 기대하기 때문에 코루틴 함수를 실행할 수는 없다. 대신 코루틴 실행을 Eventloop에 등록할 수는 있는데, Future.add_done_callback(lambda fut: asyncio.create_task(some_async_func(fut))) 같이 사용하면 된다.
asyncio.create_task()를 사용했기 때문에 당연하게도 코루틴이 종료되는 것을 await으로 기다릴 수 없다.

# concurrent.futures(다중 스레드, 비동기/Non-block 방식)
