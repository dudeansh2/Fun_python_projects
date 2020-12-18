print("hello I am calculator i do calculations")
h = input("enter the task\n")
def add(num1,num2):
    return num1+num2
def div(n1,n2):
    if n1>=n2:
        return n2/n1
    else:
        return n1/n2
def multi(z1,z2):
    return z1*z2
def square(s1):
    return s1**2
def sub(a1,a2):
    if a1>a2:
        return a1-a2
    else:
        return a2-a1
if  h =="square"or h =="**":
    rr = int(input("please enter the digit"))
    print(square(rr))
elif h.lower() =='add'or h == '+':
    zen = int(input("enter a number\n"))
    nus = int(input("enter another number\n"))
    print(add(zen,nus))
elif h.lower() == 'multiply' or h== "multi" or h=="*":
    ss = int(input("a number"))
    sss = int(input("another number"))
    print(multi(ss,sss))
elif h.lower() == "division" or h== "div"  or h == '/':
    jj = int(input("a number"))
    jjj = int(input("one more number"))
    print(div(jj,jjj))
elif h.lower() =="substract" or h =="sub" or h=="-":
    dif = int(input("a number"))
    he = int(input("one more number"))
    print(sub(dif,he))
else:
    print("invalid")
print('''Made with love by Ⓐ Ⓝ Ⓢ Ⓗ Ⓡ Ⓐ Ⓣ Ⓗ Ⓘ  
            ｇｉｔｈｕｂ ： ｄｕｄｅａｎｓｈ２''')     
