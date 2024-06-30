class WrongBaseException(BaseException):
    pass


class BasedInt:
    def __init__(self, num: int, base: int):
        if base in [-1, 0, 1]:
            raise WrongBaseException(f"Unsupported base: {base}")
        if isinstance(num, float):
            print("BasedFloat pending dev. Changing to int")
            num = int(num)
        self.b10_int = num
        self.base = base
        self.num_in_base = self.number_to_base(self.b10_int, self.base)

    @staticmethod
    def number_to_base(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    def __add__(self, other):
        accepted_instances = [int, BasedInt]
        if isinstance(other, int):
            new_b10_num = self.b10_int + other
        elif isinstance(other, BasedInt):
            new_b10_num = self.b10_int + other.b10_int
        else:
            raise TypeError(f"Unsupported operand type(s) for +. "
                            f"Only supports {accepted_instances}")
        return BasedInt(new_b10_num, self.base)

    def __sub__(self, other):
        accepted_instances = [int, BasedInt]
        if isinstance(other, int):
            new_b10_num = self.b10_int - other
        elif isinstance(other, BasedInt):
            new_b10_num = self.b10_int - other.b10_int
        else:
            raise TypeError(f"Unsupported operand type(s) for -. "
                            f"Only supports {accepted_instances}")
        return BasedInt(new_b10_num, self.base)

    def __mul__(self, other):
        accepted_instances = [int, BasedInt]
        if isinstance(other, int):
            new_b10_num = self.b10_int * other
        elif isinstance(other, BasedInt):
            new_b10_num = self.b10_int * other.b10_int
        else:
            raise TypeError(f"Unsupported operand type(s) for *. "
                            f"Only supports {accepted_instances}")
        return BasedInt(new_b10_num, self.base)

    def __truediv__(self, other):  # TODO: need to deal with floats
        accepted_instances = [int, BasedInt]
        if isinstance(other, int):
            new_b10_num = self.b10_int / other
        elif isinstance(other, BasedInt):
            new_b10_num = self.b10_int / other.b10_int
        else:
            raise TypeError(f"Unsupported operand type(s) for /. "
                            f"Only supports {accepted_instances}")
        return BasedInt(new_b10_num, self.base)

    def __floordiv__(self, other):
        accepted_instances = [int, BasedInt]
        if isinstance(other, int):
            new_b10_num = self.b10_int // other
        elif isinstance(other, BasedInt):
            new_b10_num = self.b10_int // other.b10_int
        else:
            raise TypeError(f"Unsupported operand type(s) for //. "
                            f"Only supports {accepted_instances}")
        return BasedInt(new_b10_num, self.base)

    def __repr__(self):
        return f"{self.num_in_base}_{self.base}"


if __name__ == "__main__":
    n1 = BasedInt(40, 7)
    print(n1)
    print(type(n1))
    print(n1.b10_int)
    print(n1.base)
    print(n1.num_in_base)

    print("**********")
    n2 = BasedInt(34, 12)
    print("addition")
    print(n1 + 12)
    print(n1 + n2)

    print("subtraction")
    print(n1 - 12)
    print(n1 - n2)

    print("multiplication")
    print(n1 * 12)
    print(n1 * n2)

    print("division")
    print(n1 / 12)
    print(n1 / n2)

    print("rdivision")
    print(n1 // 12)
    print(n1 // n2)
    """
    POSSIBLE USE CASES
    No issues with addition, subtraction & multiplication as
    floating points are not involved.
    Need to think of a way to do division while maintaining floating points.
    
    USE CASE A: Division with no remainders.
    1.
    [5,5]_7 / 4
    = 40 / 4
    = 10
    = [1,3]_7
    
    2.
    [5,5]_7 / 10
    = 40 / 10
    = 4
    = [4]_7
    
    3.  # ideally should be the same as above
    [5,5]_7 / [4]_7
    = 40 / 4
    = 10
    = [1,3]_7
    
    4.
    [5,5]_7 / [1,3]_7
    = 40 / 10
    = 4
    = [4]_7
    
    USE CASE B: Division with remainders.
    1.
    [5,5]_7 / 3
    = 40 / 3
    = 13.3333...
    = ?
    
    2.
    [5,5]_7 / [3]_7
    = ?
    """
