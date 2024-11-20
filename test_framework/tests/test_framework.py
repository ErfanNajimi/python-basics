def checkEqual(a, b):
    return True if a == b else False
print(checkEqual(3, 3))

def assert_equals(value1, value2) -> bool:
    return value1 == value2

# print(assert_equals(2, 2))
# print(assert_equals(True, False))
# print(assert_equals("Hello", "Hello"))
# print(assert_equals(10,20))

def assert_true(value) -> bool:
    return value == True

print(assert_true(10 < 20))

def assert_greater_than(value1: int, value2: int) -> bool:
    if type(value1) != int or type(value2) != int:
        return TypeError("At least one value was not an integer")
    # return value1 > value2

print(assert_greater_than(30, "43"))
print(TypeError("At least one value was not an integer"))
#type-hinting