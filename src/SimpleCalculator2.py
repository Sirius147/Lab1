#계산기 Lab1-3
def add(x,y):
    return x+y 
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return x**y
def fun(x,y):
    return x//y,x%y

while True:
    print("Select Option")
    print("0.exit")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.power")
    print("6.cal_QR")

    choice=int(input("enter choice: "))
    if choice==0:
        print("프로그램을 종료합니다.")
        break
    if choice<0 or choice>6:
        print("invalid input.")
        continue
        
    num1=float(input("첫번째 숫자를 입력하시오: "))
    num2=float(input("두번쨰 숫자를 입력하시오: "))
    q,r=fun(num1,num2)

    if choice == 1:
        print("%.2f+%.2f=%.2f" % (num1,num2,add(num1,num2)))

    elif choice == 2:
        print("%.2f-%.2f=%.2f" % (num1,num2,subtract(num1,num2)))

    elif choice == 3:
        print("%.2f*%.2f=%.2f" % (num1,num2,multiply(num1,num2)))

    elif choice==4:
        print("%.2f/%.2f=%.2f" % (num1,num2,divide(num1,num2)))

    elif choice==5:
        print("%.2f의 %.2f 거듭제곱은 %.2f입니다." % (num1,num2,power(num1,num2)))

    else:
        print("%.2f를 %.2f로 나누었을 때 몫=%.2f 나머지=%.2f 입니다." % (num1,num2,q,r))               
              





        
