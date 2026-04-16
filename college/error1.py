def ZDE(N,D):
    try:
        R=N/D
        return R
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
try:
    num=int(input("Enter the Numerator:: "))
    den=float(input("Enter the Denominator:: "))
    op=ZDE(num,den)
    print(op)

except:
    print("Error:Enter numeric value")