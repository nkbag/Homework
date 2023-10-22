import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
roots = np.roots([-12,0,-18,5,10,-30])
print("Корни: ", roots)

def f_prime(x):
    return -48*x**3*np.sin(np.cos(x)) + 12*x**3*np.sin(np.sin(x))*np.cos(x) - 54*x**2 + 10
inc_intervals = []
for i in range(len(roots)):
    if f_prime(roots[i]-0.01) > 0 and f_prime(roots[i]+0.01) > 0:
        x_l = roots[i]-0.01
        while f_prime(x_l) > 0:
            x_l -= 0.01
        x_r = roots[i]+0.01
        while f_prime(x_r) > 0:
            x_r += 0.01
        inc_intervals.append((x_l, x_r))
print("Интервалы, на которых функция возрастает: ", inc_intervals)

dec_intervals = []
for i in range(len(roots)):
    if f_prime(roots[i]-0.01) < 0 and f_prime(roots[i]+0.01) < 0:
        x_l = roots[i]-0.01
        while f_prime(x_l) < 0:
            x_l -= 0.01
        x_r = roots[i]+0.01
        while f_prime(x_r) < 0:
            x_r += 0.01
        dec_intervals.append((x_l, x_r))
print("Интервалы, на которых функция убывает: ", dec_intervals)

x = np.linspace(-2,2,1000)
y = f(x)
plt.plot(x, y)
plt.grid(True)
plt.show()

from scipy.optimize import minimize_scalar
res = minimize_scalar(f)
print("Вершина: (", res.x, ", ", res.fun, ")")

pos_intervals = []
prev_x = x[0]
prev_y = y[0]
for i in range(1, len(x)):
    if prev_y <= 0 and y[i] > 0:
        x_l = prev_x
        x_r = x[i]
        while abs(f((x_l + x_r) / 2)) > 0.001:
            if f((x_l + x_r) / 2) > 0:
                x_l = (x_l + x_r) / 2
            else:
                x_r = (x_l + x_r) / 2
        pos_intervals.append((x_l, x_r))
    prev_x = x[i]
    prev_y = y[i]

print("Промежутки, на которых f > 0: ", pos_intervals)

neg_intervals = []
prev_x = x[0]
prev_y = y[0]
for i in range(1, len(x)):
    if prev_y >= 0 and y[i] < 0:
        x_l = prev_x
        x_r = x[i]
        while abs(f((x_l + x_r) / 2)) > 0.001:
            if f((x_l + x_r) / 2) < 0:
                x_l = (x_l + x_r) / 2
            else:
                x_r = (x_l + x_r) / 2
        neg_intervals.append((x_l, x_r))
    prev_x = x[i]
    prev_y = y[i]

print("Промежутки, на которых f < 0: ", neg_intervals)