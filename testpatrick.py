from enum import Enum


def f(x: int = 3):
    pass

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

if __name__ == "__main__":
    c = Color.RED
    c_r, c_g, c_b = c
    c.name

    {
        Color.RED: lambda: print("..."),
        Color.GREEN: lambda: print("......"),
    }[c]()

    match c:
        case Color.RED:
            print("Het is rood!")
        case Color.GREEN:
            print("En nu groen")
        case _:
            print("En nu iets anders")

    print("hoi")