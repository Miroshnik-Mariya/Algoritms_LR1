import random
import time 

print("Лабораторная работа №1 - Алгоритмы сортировки\nВариант №1\nВыполнила студентка группы 6201-020302D\nМирошник Мария\n")
print("1. Шейкер-сортировка и пирамидальная сортировка (heap_sort).\n") 

# разновидность пузырьковой сортировки (шейкерная)
def shaker_sort(array): 
    n = len(array)
    i = 0

    while True:
       flag = 0
       for j in range(i, n - 1 - i): 
          if array[j] > array[j + 1]:
              array[j], array[j + 1] = array[j + 1], array[j]
              flag = 1
       if flag == 0: # массив упорядочен
          break
       
       i += 1
       flag = 0
       for j in range(n - 1 - i, i - 1, -1): 
          if array[j - 1] > array[j]:
              array[j], array[j - 1] = array[j - 1], array[j]
              flag = 1
       if flag == 0: #массив упорядочен
          break
    #print("Отсортированный массив (шейкер): ",*array)
    



def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    #print("Отсортированный массив (heap sort): ",*arr)
    

def efficiency():
    t1 = 0 
    t2 = 0
    print("Для массива из 1000 элементов: ")
    array_size = 1000 
    random_array = [random.randint(1, 100) for _ in range(array_size)]
    #print(f"Массив случайных чисел: {random_array}")
    
    start_time = time.clock()  
    shaker_sort(random_array)
    end_time = time.clock()
    dif_time = end_time - start_time
    print(f"Время выполнения шейкерной сортировки: {dif_time} секунд")
    t1 += dif_time 
    
    start_time = time.clock()  
    heap_sort(random_array)
    end_time = time.clock()
    dif_time = end_time - start_time
    print(f"Время выполнения пирамидальной сортировки: {dif_time} секунд")
    t2 = dif_time 

    print("\nДля массива из 10.000 элементов: ")
    array_size = 10000
    random_array = [random.randint(1, 100) for _ in range(array_size)]
    #print(f"Массив случайных чисел: {random_array}")
    
    start_time = time.clock()  
    shaker_sort(random_array)
    end_time = time.clock()
    dif_time = end_time - start_time
    print(f"Время выполнения шейкерной сортировки: {dif_time} секунд")
    t1 += dif_time 
    
    start_time = time.clock()  
    heap_sort(random_array)
    end_time = time.clock()
    dif_time = end_time - start_time
    print(f"Время выполнения пирамидальной сортировки: {dif_time} секунд")
    t2 += dif_time 
    
    print("\nСреднее суммарное время шейкерной сортировки: ",t1/11000, " секунд")
    print("Среднее суммарное время пирамидальной сортировки: ",t2/11000, " секунд")
    

    

'''



arr = [ 12, 11, 13, 5, 6, 7]
ls = [10, 1, 0, 2, 7, 10, 3, 5, 6, 3, 1, 2, 9, 8, -1, -2]

shaker_sort(ls)
heap_sort(arr)
efficiency()'''

efficiency()