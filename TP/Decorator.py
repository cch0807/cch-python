def copyright(func):
    def new_func():
        print("@ asvc")
        func()

    return new_func


@copyright
def smile():
    # print("@ asvc")
    print("😊")


@copyright
def angry():
    # print("@ asvc")
    print("😣")


@copyright
def love():
    # print("@ asvc")
    print("💕")


# 재정의 할필요없이 @ 사용
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()
