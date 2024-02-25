import matplotlib.pyplot as plt


def plot_point(x, y):
    plt.plot(x, y, 'bo')  # 'bo' represents blue circles for plotting points


def bresenham(x1, y1, x2, y2):
    x = x1
    y = y1

    dx = x2 - x1  # difference of x
    dy = y2 - y1  # difference of y
    p = 2 * dy - dx  # initial value of decision varible

    print(f"Inital decision value, p = {p} and,")
    print(f"X = {x}, Y = {y} ; P = {p}")

    while x < x2:

        x += 1

        if p < 0:
            p += 2 * dy

        else:
            p += (2 * dy - 2 * dx)
            y += 1  # only this case y will be incremented

        print(f"X = {x}, Y = {y} ; P = {p}")
        plot_point(x, y)


a, b, c, d = map(int, input('Enter the coordinate, (x1, y1, x2, y2)').split(' '))

bresenham(a, b, c, d)
