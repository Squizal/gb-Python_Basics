# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    result = []
    a = 0
    b = 1
    for i in range(m+1):
        if i >= n:
            result.append(b)
        a, b = b, b + a
    return result
    pass

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = origin_list[:]
    for i in range(1,len(origin_list)):
        j=i
        while (a[j]<a[j-1]) and (j>0):
            a[j],a[j-1] = a[j-1],a[j]
            j-=1
    return a
    pass

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter2_0(func, iterable):
    result=[]
    for i in iterable:
        if func(i):
            result.append(i)
    return result

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def obj(a1,a2,a3,a4):
    def point(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if a1 == a3: return False
    return point(a1,a3) == point(a2,a4)