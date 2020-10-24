from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pyscreenshot as ImageGrab
import numpy as np

def main():
    r = Rectangle("синего", 7, 7)
    c = Circle("зеленого", 7)
    s = Square("красного", 7)
    print(r)
    print(c)
    print(s)
    screen = np.array(ImageGrab.grab(bbox=(10, 10, 20, 200)))
if __name__ == "__main__":
    main()