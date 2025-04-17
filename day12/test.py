a = 1
b = 1
print(a is b)
print(id(a),id(b))

a = 10000 # 2353991194416
b = 10000
print(id(a),id(b))

c = int(-9999999999999999)
d = -9999999999999999


print(id(c),id(d))