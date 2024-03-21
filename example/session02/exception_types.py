base_exception: BaseException = BaseException()
keyboard_interrupt: BaseException = KeyboardInterrupt()
value_error: Exception = ValueError()


class MyException(Exception):
    pass
