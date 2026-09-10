import sys

def get_path(n, m):
    path = []
    current = 0

    while True:
        path.append(current + 1)

        current = (current + m - 1) % n

        if current == 0:
            break

    return path


def main():
    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])

    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])

    path1 = get_path(n1, m1)
    path2 = get_path(n2, m2)

    print("".join(map(str, path1)) + "".join(map(str, path2)))

if __name__ == "__main__":
    main()