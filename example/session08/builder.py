from typing import Self


class Car:
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        color: str,
        engine: str,
    ) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.color}) with {self.engine} engine"


class CarBuilder:
    def __init__(self) -> None:
        self.make: str | None = None
        self.model: str | None = None
        self.year: int | None = None
        self.color: str | None = None
        self.engine: str | None = None

    def set_make(self, make: str) -> Self:
        self.make = make
        return self

    def set_model(self, model: str) -> Self:
        self.model = model
        return self

    def set_year(self, year: int) -> Self:
        self.year = year
        return self

    def set_color(self, color: str) -> Self:
        self.color = color
        return self

    def set_engine(self, engine: str) -> Self:
        self.engine = engine
        return self

    def build(self) -> Car:
        if None in (self.make, self.model, self.year, self.color, self.engine):
            raise ValueError("All fields must be set before building the car")

        return Car(self.make, self.model, self.year, self.color, self.engine)


def main() -> None:
    builder = CarBuilder()
    car = (
        builder.set_make("Tesla")
        .set_model("Model S")
        .set_year(2021)
        .set_color("Red")
        .set_engine("Electric")
        .build()
    )

    print(car)


if __name__ == "__main__":
    main()
