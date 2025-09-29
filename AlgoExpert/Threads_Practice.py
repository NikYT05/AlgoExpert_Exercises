# from threading import Lock, Thread
# from time import sleep


# def print_numbers(begin, end, start_lock, end_lock):
#     start_lock.acquire()
#     for i in range(begin, end):
#         print(i)
#     end_lock.release()

# lock1 = Lock()
# lock2 = Lock()
# lock2.acquire()

# thread1 = Thread(target=print_numbers, args=(1,6, lock1, lock2))
# thread2 = Thread(target=print_numbers, args=(6, 11, lock2, lock1))

# thread1.start()
# thread2.start()
# lock2.release()

# def print_values(values, start_lock, end_lock, name):
#     for item in values:
#         #nprint(f"{name} waiting for lock")
#         start_lock.acquire()
#         print(item)
#         end_lock.release()

# lock1 = Lock()
# lock2 = Lock()
# lock2.acquire()

# thread1 = Thread(target=print_values, args=([1,3,5], lock1, lock2, "t1"))
# thread2 = Thread(target=print_values, args=([2,4], lock2, lock1, "t2"))

# thread1.start()
# thread2.start()


# import threading
# from time import sleep
# import math


# def append_values(lst, values=[], delay=1):
#     for value in values:
#         lst.append(value)
#         sleep(math.ceil(abs(delay)))


# def append_integer(lst, integer):
#     lst.append(integer)


# lst = []

# thread1 = threading.Thread(target=append_values, args = (lst, [1, 3, 5]))
# thread2 = threading.Thread(target=append_values, args = (lst, [4]))
# thread3 = threading.Thread(target=append_integer, args = (lst, 3))

# thread1.start()
# thread2.start()
# thread1.join()
# thread3.start()

# print(lst)

# Write your code here.
from threading import Lock, Thread

string = ""

n = int(input("Enter a positive integer: "))

def append_str(to_concat, n, start_lock, end_lock):
    for i in range(n):
        global string
        start_lock.acquire()
        string += to_concat
        end_lock.release()

lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread1 = Thread(target=append_str, args = ("foo", n, lock1, lock2))
thread2 = Thread(target = append_str, args = ("bar", n, lock2, lock1))

thread1.start()
thread2.start()
thread2.join()
print(string)