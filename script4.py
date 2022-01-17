import numpy
from math import *
import matplotlib.pyplot as plt

class Task:
    def __init__(self):
        self.a = 5
        self.b = 8
        self.h = [0.2, 0.1, 0.05]
        self.m = [10, 20, 40]
        self.x = self.initX()
        self.y = self.initY()
        self.derivativeFirstCustom = self.initDerivativeFirstCustom()
        self.derivativeSecondCustom = self.initDerivativeSecondCustom()
        self.derivativeFirstOrigin = self.initDerivativeFirstOrigin()
        self.derivativeSecondOrigin = self.initDerivativeSecondOrigin()
        self.differenceFirst = self.initDifferenceFirst()
        self.differenceSecond = self.initDifferenceSecond()

        self.derivative_h1 = self.initDerivative_h1()
        self.derivative_h2 = self.initDerivative_h2()
        self.derivative_h3 = self.initDerivative_h3()
        self.derivative_Origin = self.initDerivative_Origin()

        self.integralValue = self.initIntegralValue()
        self.draw_task()

    def initX(self):
        x = []
        for j in range(21):
            x.append(self.a + j * (self.b - self.a) / 20)
        return x

    def initY(self):
        y = []
        for j in range(21):
            y.append(Task.F(self.x[j]))
        return y

    @staticmethod
    def F(x):
        return sqrt(x) - pow(cos(x), 2)

    def initDerivativeFirstCustom(self):
        result = []
        for i in range(3):
            row = []
            row.append(Task.calculateDerivativeFirstCustom(self.x[0], self.h[i]))
            row.append(Task.calculateDerivativeFirstCustom(self.x[20], self.h[i]))
            result.append(row)
        return result

    @staticmethod
    def calculateDerivativeFirstCustom(x, h):
        return (Task.F(x + h) - Task.F(x - h)) / (2 * h)

    def initDerivativeSecondCustom(self):
        result = []
        for i in range(3):
            row = []
            for j in range(1, 20):
                row.append(Task.calculateDerivativeSecondCustom(self.x[j], self.h[i]))
            result.append(row)
        return result

    @staticmethod
    def calculateDerivativeSecondCustom(x, h):
        return (Task.F(x + h) - 2 * Task.F(x) + Task.F(x - h)) / (h * h)

    def initDerivativeFirstOrigin(self):
        result = []
        result.append(Task.calculateDerivativeFirstOrigin(self.x[0]))
        result.append(Task.calculateDerivativeFirstOrigin(self.x[20]))
        return result

    @staticmethod
    def calculateDerivativeFirstOrigin(x):
        return 2 * numpy.sin(x) * numpy.cos(x) + 0.5 * (1 / sqrt(x))

    def initDerivativeSecondOrigin(self):
        result = []
        for j in range(1, 20):
            result.append(Task.calculateDerivativeSecondOrigin(self.x[j]))
        return result

    @staticmethod
    def calculateDerivativeSecondOrigin(x):
        return - 2 * pow(numpy.sin(x), 2) + 2 * pow(numpy.cos(x), 2) - 0.25 * pow(x, -1.5)

    def initDifferenceFirst(self):
        result = []
        for i in range(3):
            row = []
            row.append(self.derivativeFirstOrigin[0] - self.derivativeFirstCustom[i][0])
            row.append(self.derivativeFirstOrigin[1] - self.derivativeFirstCustom[i][1])
            result.append(row)
        return result

    def initDifferenceSecond(self):
        result = []
        for i in range(3):
            row = []
            for j in range(19):
                row.append(self.derivativeSecondOrigin[j] - self.derivativeSecondCustom[i][j])
            result.append(row)
        return result

    def initIntegralValue(self):
        value = []
        for j in range(3):
            h = (self.b - self.a) / self.m[j]
            s = 0
            x = self.a + h / 2
            for i in range(self.m[j]):
                x1 = x - (h / 2) * 0.5773502692
                x2 = x + (h / 2) * 0.5773502692
                s += Task.F(x1) + Task.F(x2)
                x += h
            value.append(s * h / 2)

        print("\nИстинное значение интеграла: 6.067\n")
        print("Приближённое при m = 10: " + str(value[0]) + " (погрешность: " + str(6.067 - value[0]) + ")")
        print("Приближённое при m = 20: " + str(value[1]) + " (погрешность: " + str(6.067 - value[1]) + ")")
        print("Приближённое при m = 40: " + str(value[2]) + " (погрешность: " + str(6.067 - value[2]) + ")")

        return value

    def initDerivative_h1(self):
        value = []
        value.append(self.derivativeFirstCustom[0][0])
        for j in range(19):
            value.append(self.derivativeSecondCustom[0][j])
        value.append(self.derivativeFirstCustom[0][1])
        return value

    def initDerivative_h2(self):
        value = []
        value.append(self.derivativeFirstCustom[1][0])
        for j in range(19):
            value.append(self.derivativeSecondCustom[1][j])
        value.append(self.derivativeFirstCustom[1][1])
        return value

    def initDerivative_h3(self):
        value = []
        value.append(self.derivativeFirstCustom[2][0])
        for j in range(19):
            value.append(self.derivativeSecondCustom[2][j])
        value.append(self.derivativeFirstCustom[2][1])
        return value

    def initDerivative_Origin(self):
        value = []
        value.append(self.derivativeFirstOrigin[0])
        for j in range(19):
            value.append(self.derivativeSecondOrigin[j])
        value.append(self.derivativeFirstOrigin[1])
        return value

    def draw_task(self):
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()

        ax.plot(self.x, self.derivative_h1, self.x, self.derivative_h2, self.x, self.derivative_h3, self.x, self.derivative_Origin)
        plt.show()

if __name__ == '__main__':
    task = Task()