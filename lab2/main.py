from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pyscreenshot as ImageGrab
import numpy as np
import cv2

def main():
    r = Rectangle("синего", 7, 7)
    c = Circle("зеленого", 7)
    s = Square("красного", 7)
    print(r)
    print(c)
    print(s)
    while True:
     screen = np.array(ImageGrab.grab(bbox=(10, 10, 300, 300))) # метод внешнего пакета Pillow
     cv2.imshow('window', screen)
     if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
if __name__ == "__main__":
    main()