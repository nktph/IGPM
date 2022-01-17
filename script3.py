import random

import numpy
from math import *
import matplotlib.pyplot as plt

class Task:
    def __init__(self):
        self.a = 5
        self.b = 8
        self.z = 4
        self.n = 4
        self.c = [0 for element in range(self.n)]
        self.xi = self.init_Xi()
        self.fXi = self.init_fXi()
        self.matrix = self.init_Coef()
        self.xj = self.init_Xj()
        self.fXj = self.init_fXj()
        self.phiXj = self.init_phiXj()
        self.draw_task()

    def init_Xi(self):
        xi = []
        for i in range(self.n):
            xi.append(self.a + i * (self.b - self.a) / self.n)
        return xi

    def init_fXi(self):
        fXi = []
        for i in range(self.n):
            xi = self.xi[i]
            fXi.append(sqrt(xi) - pow(cos(xi), 2))
        return fXi


    def init_Coef(self):
        a = []
        for k in range(self.n):
            a.append([0 for element in range(self.n)])

        for k in range(self.n):
            a[k][0] = 1
            i = -1
            for m in range(1, self.n):
                i = i + 1
                if i == k:
                    i = i + 1
                d = self.xi[k] - self.xi[i]
                a[k][m] = a[k][m - 1] / d
                for j in range(self.n - 1, 1, -1): # n-1?
                    a[k][j] = (a[k][j - 1] - a[k][j] * self.xi[i]) / d
                a[k][0] = -1 * a[k][0] * self.xi[i] / d

        for i in range(self.n):
            self.c[i] = 0
            for k in range(self.n):
                self.c[i] = self.c[i] + a[k][i] * self.fXi[k]

        return a

    def init_Xj(self):
        xj = []
        for j in range(21):
            xj.append(self.a + j * (self.b - self.a) / 20)
        return xj

    def init_fXj(self):
        fXj = []
        for j in range(21):
            xj = self.xj[j]
            fXj.append(sqrt(xj) - pow(cos(xj), 2))
        return fXj


    def init_phiXj(self):
        phiXj = []
        for j in range(21):
            xj = self.xj[j]
            phiXj.append((self.c[0] + self.c[1] * xj + self.c[2] * pow(xj, 2) + self.c[3] * pow(xj, 3)) / 36500)
        return phiXj


    '''
    def init_phiXj(self):
        phiXj = []
        for j in range(21):
            xj = self.xj[j]
            phiXj.append(self.calculate(j))
        return phiXj
    '''


    def draw_task(self):
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()

        self.calculate_mistake()
        ax.plot(self.xj, self.fXj, self.xj, self.phiXj)
        plt.show()

    def calculate_mistake(self):
        mistake = []

        print("Погрешность вычислений:\n")
        for i in range(21):
            mistake.append(self.fXj[i] - self.phiXj[i])
            print("d_" + str(i) + " = " + str(mistake[i]))

        avg = 0
        for i in range(21):
            avg += mistake[i]
        avg /= 21
        print("\nСредняя погрешность = " + str(avg))


'''
    def calculate(self, j):
        p = 0
        for k in range (21):
            e = 1
            for i in range(21):
                if i == k:
                    continue
                e = e * (self.xj[j] - self.xj[i]) / (self.xj[k] - self.xj[i])
            p = p + e * self.xj[k]
        return p
'''

    
if __name__ == '__main__':
    task = Task()

