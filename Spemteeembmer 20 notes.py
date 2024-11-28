print((lambda x: x + 1)(2))

print((lambda y: y * 3)(3))

func = lambda x, y: x + y
print(func(2,3))

higher_order_function = lambda x, func: x + func(x)
print(higher_order_function(2, lambda x: x * x))

print(higher_order_function(3, lambda y: y // 3))

print(list(map(lambda x: len(x), ["hey", "ho", "here"])))

print(list(map(lambda a: a.lower()[0], ["I", "love", "CS", "intro"])))

from functools import reduce
print(reduce(lambda x, y: x + len(y), ["this", "is", "a", "test"], 0))

(lambda x: x % 2 and 'odd' or 'even')(2) 

print(list(filter(lambda x: x % 2 == 0, [0, 1,2,3,4,5])))
