# tall1 * tall2 = tall1 + [tall1 * (tall2-1) ]

def mult_as_add_iter(op1:int,op2:int)-> int:
    result = 0
    for i in range(op2):
        result += op1
        if i == op2-1:
            return result
        



def mult_as_add_rec(op1:int,op2:int)-> int:
    if op2 == 1:
        return op1
    else:
        return op1 +  mult_as_add_rec(op1, op2 - 1)
        

print(mult_as_add_rec(6,4))
print(mult_as_add_iter(6,4))