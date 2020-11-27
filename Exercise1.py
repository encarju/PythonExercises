from math import pi;

def circle_area():
    rad = int(input('Input Radius: '))
    return pi*pow(rad,2)

if __name__ == "__main__":
    print(circle_area())