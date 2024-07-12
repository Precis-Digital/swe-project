class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("constructing new instance")
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.log_file = "app.log"
        with open(self.log_file, "w") as file:
            file.write("Logger Initialized\n")

    def log(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

    def __str__(self) -> str:
        return f"Logger instance with log file: {self.log_file}"

    def __repr__(self) -> str:
        return f"<Logger(log_file={self.log_file})>"


if __name__ == "__main__":
    # First instance
    logger1 = Logger()
    logger1.log("First log message")

    # Second instance
    logger2 = Logger()
    logger2.log("Second log message")

    # Check if both instances are the same
    print(f"logger1 is logger2: {logger1 is logger2}")

    print(id(logger1))
    print(id(logger2))
