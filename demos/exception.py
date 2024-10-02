def remainder_division(a,b):
    try:
        result = a//b
        remainder = a%b
        print(a, '/', b, 'is', result, 'remainder', remainder)
    except:
        print("Cannot divide by 0")
    finally:
        print("You tried to divide", a, 'and', b)


remainder_division(15, 2)
remainder_division(15, 0)
