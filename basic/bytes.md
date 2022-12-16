# Bytes

- 2.x 버전의 바이트 처리가 3.x에서 약간 바뀐 점이 있어서 3.7이상의 버전에서 테스트하는걸 권장한다.

bytes 타입은 이름처럼 바이트가 나열된 형태의 자료구조를 구현하는 클래스이다.

```
>>> bs = b'abcd'
>>> bs
b'abcd'
>>> type(bs)
<class 'bytes'>
```

b 로 시작하는 문자열 표현을 사용했는데, b의 의미는 bytes로 이해하면된다.
물론 bytes를 이용해 바로 생성하는 방법도 있다.

```
>>> b = bytes(8)
>>> b
b'\x00\x00\x00\x00\x00\x00\x00\x00'
```

생성자의 첫 매개변수는 바이트 버퍼의 바이트 카운트, 즉 사이즈다.
생성된 버퍼는 모두 0으로 초기화되어 있는데, 이 bytes 타입은 수정이 불가능한 타입이다.
다르게 표현해서 Immutable 타입.

```
>>> bytes((1, 2, 3, 4))
b'\x01\x02\x03\x04'
>>> bytes([1, 2, 3, 4])
b'\x01\x02\x03\x04'
```

```
>>> b = bytes([1, 2, 3, 4])
>>> len(b)
4
>>> b[2]
3
```

# Byte Array

bytearray 타입은 이름처럼 바이트 배열(Byte Array)을 구현하는 클래스인데, bytes가 수정이 불가능한 immutable 타입인 것에 반해 이 타입은 요소 수정이 가능한 타입이다. 다르게 말해서 mutable bytes 처럼 생각할 수도 있다.

따라서 생성은 생성자를 통해서 데이터를 넘겨주면 된다.

```
>>> ba = bytearray(b'abcd)
>>> ba
bytearray(b'abcd)
```

```
>>> ba[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
```

mutable bytes라고 했으니 수정해보려했는데 에러가 발생했다.
안되는 이유는 간단하다. 'A'는 Python의 문자열 오브젝트이다. 
그리고 Byte Array는 이름처럼 바이트 단위로 액세스 해야한다.
따라서 문자열 대신 한 바이트 수치를 넣는 방식이면 수정이 될 것이다.

```
>>> ba[0] = 0x41
>>> ba
bytearray(b'Abcd')
```

0x41 즉 16진수 41은 대문자 A의 아스키 코드이다.

ord() 함수를 사용하면 더 편할 수도 있다.

```
>>> ba[1] = ord('B')
>>> ba
bytearray(b'ABcd')
>>> del(ba[4])
>>> ba
bytearray(b'ABcd')
```

# 바이트를 문자열로 바꾸기

```
>>> b = b'abcd'
>>> str(b)
"b'abcd'"
```

뭔가 되기는 되는데 원하는 것은 저게 아니다.
사실 우리가 쓰는 문자열은 유니코드 문자를 사용한다.
그래서 바이트 배열로 구성되는 C문자열을 그대로 문자열로 변환하는 것은 이상한 행위다.
다행히도 해답은 있다. 이 경우 bytes 나 bytearray 를 decode하면 다시 원래의 문자열을 얻을 수 있다.

```
b. decode()
'abcd'
```

# 한글과 바이트

한글을 쓰는 경우도 살펴보자.
한글도 binstring으로 표현하면 바로 바이트 배열로 쓸 수 있을까?

```
>>> b'한글'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
```

불행히도 그렇지 않다. 입력한 문자의 인코딩을 알려주지 않으면 바이트 버퍼로 바꿀 수 없다.
그럼 어떻게 해야할까?
다행히도 이 경우를 위해 encode()를 사용할 수 있다.

```
>>> hbuf = '한글'.encode('utf-8')
>>> hbuf
b'\xed\x95\x9c\xea\xb8\x80'
```

인코딩을 명확하게 UTF-8 이라고 알려주고 인코딩을 하면 자연스럽게 바이트 버퍼가 튀어나온다.

반대의 경우는 다음과 같다.

```
>>> hbuf.decode('utf-8')
'한글'
```