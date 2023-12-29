"""
Бинарный поиск -
это алгоритм, который на вход получает отсортированный список элементов. 
Если элемент, который Вы ищите, присутствует в списке, он возвращает ту позицию, 
в которой он был найден. В противном случае возвращает null.

Для списка из n элементов бинарный поиск выполняется за logn по основанию 2.
"""

def binary_search(list, item):
  # В переменных low и hight хранятся границы той части списка, в которой выполняется поиск
  low = 0
  hight = len(list) - 1

  # Пока эта часть не сократится до одного элемента, проверяем средний элемент
  while low <= high:
    # Если значение нечетно, огругляется в меньшую сторону
    mid = (low + high)/2 
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      high = mid + 1
  return None

"""
Массивы и связанные списки:
Связанные списки отлично подходят в тех случаях, когда данные должны читаться последовательно: 
сначала вы читаете один элемент, потом по адресу переходите к следующему элементу. 
В связанном списке элементы не хранятся рядом друг с другом, поэтому мгновенно определить 
i-го элемента в памяти невозможно - нужно обратиться к первому элементу, чтобы получить адрес 
второго элемента, затем обратиться ко второму элементу для того, чтобы получить адрес третьего - и так далее.

Массивы прекрасно подходят для чтения элементов в произвольных позициях, потому что обращение к любому
элементу в массиве происходит мгновенно. 

Массивы обеспечивают быстрое чтение. Связанные списки обеспечивают быструю вставку и удаление.
"""

# Функция для поиска индекса наименьшего элемента в массиве

def findSmallest(arr):
  # Для хранения наименьшего значения
  smallest = arr[0]
  # Для хварнения индекса наименьшего значения
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

# Функция сортировки

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest)) # Удаляет элемент по индексу, потом возвращает его
  return newArr

"""Алгоритм быстрой сортировки"""

def quicksort(array):
  if len(array) < 2:
    # Базовый случай (массивы с 0 и 1 элементом уже "отсортированы")
    return array
  else:
    # Рекурсивный случай
    pivot = array[0]
    # Подмассив всех элементов, меньших опорного
    less = [i for i in array[1:] if i < pivot]
    # Подмассив всех элементов, больших опорного
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

"""Алгоритм поиска в ширину"""

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['jonny', 'anuj']
graph['claire'] = ['thom']
graph['peggy'] = []
graph['jonny'] = []
graph['anuj'] = []
graph['thom'] = []

# В python для создания двухсторонней очереди (дека) используется функция deque:

from collections import deque

def person_is_seller(name): # Если имя заканчивается на "m" будем считать, чтот этот человек продавец манго
  return name[-1] == 'm'

def serch(name):
  # Создание новой очереди
  search_queue = deque()
  # Нет, не являются. Все друзья этого человека добавляются в очередь поиска
  search_queue += graph[name]
  # Массив, который используется для отслеживания уже проверенных людей
  searched = []
  # Пока очередь не пуста
  while search_queue:
    # Из очереди извлекается первый человек
    person = search_queue.popleft()
    # Проверяем является ли человек продавцом манго
    if not person in searched:
      if person_is_seller(person):
        # Да, это продавец манго
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        # Человек помечается как уже проверенный
        searched.append(person)
  return False

serch("you")

"""
Алгоритм Дейкстры состоит из 4 шагов:
1. Найти узел с наименьшей стоимостью (то есть узел, до которого можно добраться за минимальное время).
2. Обновить стоимости соседей этого узла.
3. Повторить, пока не будет сделано для всех узлов графа.
4. Вычислить итоговый путь.

Использование невозможно с отрицательными ребрами.
"""

# Нахождение узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  # Перебрать все узлы
  for node in costs:
    cost = costs[node]
    # Если этот узел с наименьшей стоимостью из уже виденных и он еще не был обработан
    if cost < lowest_cost and node not in processed:
      # ... он назначается новым узлом с наименьшей стоимостью
        lowest_cost = cost
        lowest_cost_node = node
  return lowest_cost_node

infinity = float("inf")
# Таблица стоимосттей узла
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# Таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None
# Массив для отслеживания уже обработанных узлов (один узел не должен обрабатываться многократно)
processed = []

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# Если обработаны все узлы, while будет завершен
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  # Перебрать всех соседей текущего узла
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    # Если к соседу можно быстрее добраться через текущий узел...
    if costs[n] > new_cost:
      # ... обновить стоимость этого узла
      costs[n] = new_cost
      # Этот узел становится новым родителем для соседа
      parents[n] = node
  # Узел помечается как обработанный
  processed.append(node)
  # Найти следующий узел для обработки и повторить
  node = find_lowest_cost_node(costs)
