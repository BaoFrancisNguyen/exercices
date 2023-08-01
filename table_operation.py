# table opération


def addition_callback(a, b):
    return a+b

def multiplication_callback(a, b):
    return a*b

def division_callback(a, b):
    return a/b

def soustraction_callback(a, b):
    return a - b


def table_operation(n, operator_str, operation_callback):
    for i in range(1, 10):
        print(i, operator_str, n, "=", operation_callback(i, n))
        
table_operation(2, "+", addition_callback)
print()
table_operation(3, "*", multiplication_callback)