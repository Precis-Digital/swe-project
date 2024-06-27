def get_adder(summand1):
    def adder(summand2):
        return summand1 + summand2

    return adder


add_3 = get_adder(3)
print(add_3(5))
