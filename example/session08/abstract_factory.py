import abc


class Chair(abc.ABC):
    @abc.abstractmethod
    def sit_on(self) -> None:
        pass


class Sofa(abc.ABC):
    @abc.abstractmethod
    def lie_on(self) -> None:
        pass


class ModernChair(Chair):
    def sit_on(self) -> None:
        print("Sitting on a modern chair.")


class ModernSofa(Sofa):
    def lie_on(self) -> None:
        print("Lying on a modern sofa.")


class VictorianChair(Chair):
    def sit_on(self) -> None:
        print("Sitting on a Victorian chair.")


class VictorianSofa(Sofa):
    def lie_on(self) -> None:
        print("Lying on a Victorian sofa.")


class FurnitureFactory(abc.ABC):
    @abc.abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abc.abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    chair.sit_on()
    sofa.lie_on()


if __name__ == "__main__":
    print("Modern Furniture:")
    modern_factory = ModernFurnitureFactory()
    client_code(factory=modern_factory)

    print("\nVictorian Furniture:")
    victorian_factory = VictorianFurnitureFactory()
    client_code(factory=victorian_factory)
