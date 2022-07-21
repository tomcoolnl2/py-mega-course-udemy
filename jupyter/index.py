# import pandas as pd

# df1 = pd.DataFrame([[2,4,6], [10,20,30]])
# df1
 
# l1 =[[2 - i for i in range(2)] for j in range(2)]
# print(l1)
# result = 0
# for i in range(2):
#     print('add ', i, l1[i][i])
#     result += l1[i][i]
# print(result)

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = l2
# print(l3 is l2)
# print(l1 == l3)
# print(l1 is l3)
# print(l1 is l2)

# x = input('first:')
# y = input('second:')
# print('sum:' + str(int(x) + int(y)))


# year = 10
# print("Year less than 2021") if year < 2021 else print("Bye 2020")


# for i in range(10):
#     if i == 3: continue
#     print(i)


# determine order of execution
# print(17 / 2 % 2 * (3 ** 3))
# print(17 / 2 * 3 + 2)

# print((19 % 4) + (15 / 2) * 3)


# data = "" # empty string evaluates to False
# while data:
#     print("Data is not Empty")
# else:
#     print("Data is Empty")


# print("2"*3)


# t = 4,
# print(type(t))

# var1 = 1
# var2  =2

# var2 = var1
# print(var1 is not var2)
# print(var1 is var2)

# myList = [7]
# yourList = myList[:]
# myList[0] = 5
# print(myList)
# print(yourList)


# l = [17,7,5,3,4]
# l2 = l[1:-1]
# print(l2)


# t = (7, 14, 21)
# t1 = t + (28,)
# t2 = t * 3
# print(t1, t2)

# d = { 'test2': 'test', 'test3': 'test' }
# d['test3'] = 4
# print(len(d), d.items())
# print(d)

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# l3 = l2
# print(l3 is l2) # True
# print(l1 == l3) # True
# print(l1 is l3) # False
# print(l1 is l3) # False

# print(7//2*4)
# print(7%2*4)
# print(7/2%4)
# print(7/2*4)

# var = 2
# while var < 8:
#     print('#', var << 1)
#     var = var << 1

# for x in open('data/supermarkets.json', 'rt'):
#     print(x)

# x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def func(data): # [[1, 2], [3, 4]]
#     res = data[0][0]  # 1
#     for da in data: # [1, 2], [3, 4]
#         for d in da:
#             if res < d:
#                 res = d
#     return res
# print(func(x[0]))
# # print(x[0])


# num = 1
 
# def func():
#     num = num + 3
#     print(num)
  
# func()
 
# file = open('data/supermarkets.json', 'rt')
# chars = file.read(12)
# print(chars)

# class Cat:
#     Species = 1
 
#     def get_species(self):
#         return 'kitty'
 
 
# class Tiger(Cat):
#     def get_species(self):
#         return 'tiggy'
 
#     def set_species(self):
#         pass
 
 
# creature = Tiger()
# print(hasattr(creature, "Species"),
#       hasattr(Cat, "set_species"))

# from datetime import datetime
 
# datetime = datetime(2019, 11, 27, 11, 27, 22)
# print(datetime.strftime('%y/%B/%d %H:%M:%S'))

# data = [261, 321]
# try:
#     print(data[-3])
# except Exception as exception:
#     print(exception.args)
# else:
#     print("('success',)")

# v = [1, 2, 3]
# def g(a,b,m):
#     return m(a,b)
 
# print(g(1, 1, lambda x,y: v[ x:y+1 ]))


# class Economy:
#     def __init__(self):
#         self.econ_attr = True
 
 
# class Business(Economy):
#     def __init__(self):
#         super().__init__()
#         self.busn_attr = False
 
 
# econ_a = Economy()
# econ_b = Economy()
# busn_a = Business()
# busn_b = busn_a
# print(isinstance(busn_a, Economy)
#       and isinstance(econ_a, Business), end=" ")
# print(busn_b is busn_a or econ_a is econ_b)

# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] += 1
 
# sum = 0
 
# for k in d:
#     sum += d[k]
 
# print(sum, d) # 4 {1: 2, '1': 2}


# class A:
#     def __init__(self, name):
#         self.name = name
 
# a = A('class')
# print(a) # <__main__.A object at 0x10dc4e380>


# x = '\''
# print(len(x))


# class A:
#     def __init__(self, x):
#         self.__a = x + 1

# a = A(0)
# print(a.__a)

# list1 = [1, 3]
# list2 = list1
# list1[0] = 4 # !! Reference
# print(list2)


# x = 2
# y = 1
# x *= y + 1
# print(x) # 4 !!!! not 3
 

# foo = [i + i for i in range(5)]
# print(foo)

# L = [i for i in range(-1, -2)]
# print(L)



# class A:
#     def __init__(self, x=0):
#         self.x = x
 
#     def func(self):
#         self.x += 1
 
 
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
 
#     def func(self):
#         self.y += 1
 
 
# b = B()
# b.func()
# print(b.x, b.y)
