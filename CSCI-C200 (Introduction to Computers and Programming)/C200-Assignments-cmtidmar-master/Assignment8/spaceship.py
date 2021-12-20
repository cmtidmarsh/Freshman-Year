import matplotlib.pyplot as plt


def mandelbrot(c, max_iterations):
    z = (0, 0)
    for i in range(max_iterations):
        if (z[0]*z[0] + z[1] * z[1]) > 4:
            return i
        z = (z[0]*z[0] - z[1]*z[1], z[0]*z[1] + z[1]*z[0])
        z = (z[0] + c[0], z[1] + c[1])
    return max_iterations

#-----------graph------------------------------
plt.axis([-2, 1, -1, 1])
plt.show() 