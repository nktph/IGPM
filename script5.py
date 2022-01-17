import math
import tkinter as tk

import numpy
from math import *
import matplotlib.pyplot as plt

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

    def run(self):
        self.mainloop()

    def show_table(self, task, root):
        total_rows = len(task.x)
        total_columns = 2

        data = []
        data.append(("x", "f(x)"))
        for i in range(total_rows):
            data.append((task.x[i], task.y[i]))

        for i in range(total_rows + 1):
            for j in range(total_columns):
                self.entry = tk.Entry(root, width=20)
                self.entry.grid(row=i, column=j)
                self.entry.insert(tk.END, data[i][j])

        self.mainloop()

class Task:
    def __init__(self):
        self.a = 4
        self.b = 8
        self.e = 0.0001
        self.m = 20
        self.x = self.initX()
        self.y = self.initY()
        self.x0 = self.initX0()
        self.resultX, self.resultY = self.algorithm()
        self.printResult()

        self.draw()
    def initH(self):
        print("Введите длину диапазона:")
        return float(input())

    def printResult(self):
        last_index = len(self.resultX) - 1
        print("Найден корень:\nx = " + str(self.resultX[last_index]) + "\ny = " + str(self.resultY[last_index]))

    def algorithm(self):
        x_value = []
        y_value = []
        h = 0.01
        x0 = self.x0
        x1 = x0 - h
        x2 = x0
        x3 = x0 + h
        y1 = Task.f(x1)
        y2 = Task.f(x2)
        y3 = Task.f(x3)
        it = 0
        zm = 0
        e = self.e
        while abs(zm) > e or it < 10:
            try:
                it += 1
                z1 = x1 - x3
                z2 = x2 - x3
                r = y3
                d = z1 * z2 * (z1 - z2)
                p = ((y1 - y3) * z2 - (y2 - y3) * z1) / d
                q = -((y1 - y2) * z2 * z2 - (y2 - y3) * z1 * z1) / d
                D = pow(q * q - 4 * p * r, 0.5)
                zm1 = (-q + D) / (2 * p)
                zm2 = (-q - D) / (2 * p)
                zm = min(abs(zm1), abs(zm2))
                x1 = x2
                x2 = x3
                y1 = y2
                y2 = y3
                x3 += zm
                y3 = Task.f(x3)
                x_value.append(x3)
                y_value.append(y3)
            except ZeroDivisionError:
                x_value.append(x3)
                y_value.append(y3)
                break
            except ValueError:
                x_value.append(x3)
                y_value.append(y3)
                break
        return x_value, y_value

    def initX0(self):
        root = tk.Tk()
        app = Application(root)
        root.title("Таблица значений")
        root.geometry("300x500")
        print("Введите значение точки начального приближения:")
        app.show_table(self, root)
        return float(input())

    def initX(self):
        x = []
        h = (self.b - self.a) / self.m
        t = self.a
        while t < self.b + 0.00001:
            x.append(t)
            t += h
        return x

    def initY(self):
        y = []
        for x in self.x:
            y.append(Task.f(x))
        return y

    @staticmethod
    def f(x):
        return sqrt(x) - pow(math.cos(x), 2) - 2

    def draw(self):
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()

        ax.plot(self.x, self.y, self.resultX, self.resultY)
        plt.show()

if __name__ == '__main__':
    task = Task()