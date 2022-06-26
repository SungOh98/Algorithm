from Quick_Sort import Quick_Sort
from Merge_Sort import Merge_Sort
from Heap_Sort import Heap_Sort
import time, random, sys
sys.setrecursionlimit(100000)

n = int(input("배열의 크기를 입력하세요: "))
array = []
for _ in range(n):
    array.append(random.randint(0, n))

array1 = array[:]
array2 = array[:]
array3 = array[:]


s = time.time()
Quick_Sort(array1, 0, len(array1) - 1)
e = time.time()

q_time = e - s

s = time.time()
Merge_Sort(array2, 0, len(array1) - 1)
e = time.time()

m_time = e - s

s = time.time()
array3 = Heap_Sort(array3)
e = time.time()

h_time = e - s

s = time.time()
Quick_Sort(array1, 0, len(array1) - 1)
e = time.time()

q_time2 = e - s

s = time.time()
Merge_Sort(array2, 0, len(array1) - 1)
e = time.time()

m_time2 = e - s

s = time.time()
array3 = Heap_Sort(array3)
e = time.time()

h_time2 = e - s




print(f"Quick_sort_time: {q_time:.2f}s")
print(f"Merge_sort_time: {m_time:.2f}s")
print(f"heap_sort_time: {h_time:.2f}s")

print(f"already_sorted_Quick_sort_time: {q_time2:.2f}s")
print(f"already_sorted_Merge_sort_time: {m_time2:.2f}s")
print(f"already_sorted_heap_sort_time: {h_time2:.2f}s")



