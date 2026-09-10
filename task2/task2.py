import sys


def main():
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(ellipse_file, "r", encoding="utf-8") as file:
        x0, y0 = map(float, file.readline().split())
        rx, ry = map(float, file.readline().split())

    with open(points_file, "r", encoding="utf-8") as file:
        for line in file:
            x, y = map(float, line.split())

            value = ((x - x0) / rx) ** 2 + ((y - y0) / ry) ** 2

            if value == 1:
                print(0)  
            elif value < 1:
                print(1)  
            else:
                print(2)  


if __name__ == "__main__":
    main()