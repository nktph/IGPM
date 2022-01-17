import numpy # библиотека для работоспособности матриц

class Task:
    def __init__(self): # инициализация задания
        self.n = Task.createSize() # определение размера матрицы
        self.coefficientMatrix = Task.createCoefficientMatrix(self.n) # создание матрицы коэффициентов
        self.variableMatrix = [None for i in range(self.n)] # инициализация вектора неизвестных переменных
        self.resultMatrix = Task.createResultMatrix(self.n) # создание матрицы результатов
        self.showMatrix() # отображение матриц
        self.p, self.q, self.r, self.d = Task.createCoefficientVectors(self) # инициализация векторов коэффициентов
        self.showVectors() # отображение векторов
        self.isStable = self.checkStability() # проверка устойчивости
        self.showStability() # отображение результата проверки устойчивости
        self.ksi, self.mu = Task.createParameterVectors(self) # инициализация векторов параметров Кси и Мю

    @staticmethod
    def createSize(): # определение размера матрицы
        print("Введите размер квадратной матрицы коэффициентов: ")
        return int(input())

    @staticmethod
    def createCoefficientMatrix(n): # создание матрицы коэффициентов
        matrix = numpy.zeros((n, n)) # создание матрицы нулей с размером n строк и n столбцов
        print("\nВведите значения элементов матрицы: ")
        for i in range(n):
            print("\n\nВвод " + str(i + 1) + " строки: ")
            for j in range(n):
                matrix[i][j] = float(input()) # ввод значений

        return matrix

    @staticmethod
    def createResultMatrix(n): # создание матрицы результатов
        matrix = numpy.zeros((n, 1)) # создание матрицы нулей с размером n строк и 1 столбцом
        print("\nВведите значения матрицы результата:")
        for i in range(n):
            print("\nВвод " + str(i + 1) + " строки: ")
            matrix[i][0] = float(input()) # ввод значений

        return matrix

    def showMatrix(self): # отображение матриц
        print("\nМатрица коэффициентов:\n", self.coefficientMatrix)
        print("\nМатрица неизвестных:\n[", end='')
        for i in range(self.n):
            if i == 0:
                print("[x1.]")
            else:
                if i == (self.n - 1):
                    print('[x' + str(i + 1) +".]]")
                else:
                    print("[x" + str(i + 1) + ".]")
        print("\nМатрица результата:\n", self.resultMatrix)

    @staticmethod
    def createCoefficientVectors(obj): # инициализация вектора неизвестных переменных
        if obj.n == 1:
            return [], [obj.coefficientMatrix[0][0]], [], [] # если размер равен 1, то вернуть пустые p, r, d и заполненный q
        else:
            q = []
            p = []
            r = []
            d = []
            for i in range(obj.n): q.append(obj.coefficientMatrix[i][i]) # инициализация вектора q
            for i in range(obj.n - 1): r.append(obj.coefficientMatrix[i][i + 1]) # инициализация вектора r
            for i in range(1, obj.n):
                p.append(obj.coefficientMatrix[i][i - 1]) # инициализация вектора p
            for i in range(obj.n): d.append(obj.resultMatrix[i][0]) # инициализация вектора d
            return p, q, r, d

    def showVectors(self): # отображение векторов
        print("\nВектор p:\n", self.p)
        print("\nВектор q:\n", self.q)
        print("\nВектор r:\n", self.r)
        print("\nВектор d:\n", self.d)

    def checkStability(self): # проверка устойчивости (стр. 17, абзац 3)
        strong = [] # массив результатов проверок на строгое равенство
        weak = [] # массив результатов проверок на нестрогое равенство
        result = False

        result = abs(self.q[0]) > abs(self.r[0]) # проверка первой строки
        strong.append(result)
        weak.append(result)

        result = abs(self.q[self.n - 1]) > abs(self.p[self.n - 2]) # проверка последней строки
        strong.append(result)
        weak.append(result)

        for i in range(1, self.n - 1): # проверка остальных строк
            result = abs(self.q[i] > abs(self.p[i]) + abs(self.r[i]))
            strong.append(result)
            weak.append(result)

        for i in range(len(weak)):
            if weak[i] == False: return False

        for i in range(len(strong)):
            if strong[i] == True: return True

        return False

    def showStability(self): # отображение результата проверки устойчивости
        if self.isStable == True: print("\nУСЛОВИЕ ВЫПОЛНЕНО: Деления на ноль не произойдёт, расчёт устойчив относительно погрешностей округления!\n")
        else: print("\nУСЛОВИЕ НЕ ВЫПОЛНЕНО: Возможно деление на ноль, расчёт не устойчив относительно погрешностей округления!\n")

    @staticmethod
    def createParameterVectors(obj): # инициализация векторов Кси и Мю (стр. 17, формулы 2.8) - формулы прямого хода
        ksi = []
        mu = []
        ksi.append(-1 * obj.r[0] / obj.q[0]) # добавление Кси-1
        mu.append(obj.d[0] / obj.q[0]) # добавление Мю-1

        for i in range(1, obj.n - 1):
            ksi.append(-1 * obj.r[i] / (obj.q[i] + obj.p[i] * ksi[i - 1]))
            mu.append((obj.d[i] - obj.p[i] * mu[i - 1]) / (obj.q[i] + obj.p[i] * ksi[i - 1]))

        t = obj.n - 1
        mu.append((obj.d[t] - obj.p[t - 1] * mu[t - 1]) / (obj.q[t] + obj.p[t - 1] * ksi[t - 1]))

        return ksi, mu

    def solve(self): # решение задания (стр. 17, формулы 2.9) - формулы обратного хода
        t = self.n - 1
        self.variableMatrix[t] = (self.d[t] - self.p[t - 1] * self.mu[t - 1]) / (self.q[t] + self.p[t - 1] * self.ksi[t - 1]) # расчёт последней неизвестной

        if self.n > 1:
            for i in range(self.n - 2, -1, -1): self.variableMatrix[i] = self.ksi[i] * self.variableMatrix[i + 1] + self.mu[i] # расчёт предыдущих неизвестных

        print("Ваше решение:") # отображение ответа
        for i in range(self.n):
            print("x" + str(i + 1) + " = " + str(self.variableMatrix[i]))

    def findDiscrepancy(self): # поиск невязки (стр. 13)
        delta = -1.0
        for i in range(self.n):
            sum = 0.0
            for j in range(self.n): sum += self.coefficientMatrix[i][j] * self.variableMatrix[j]
            tmp = abs(self.resultMatrix[i][0] - sum)
            if tmp > delta: delta = tmp
        print("Невязка равна: ", str(delta))

if __name__ == '__main__':
    task = Task() # инициализация задания
    task.solve() # решение задания
    task.findDiscrepancy() # поиск невязки