a = int(input())
b = int(input())
c = int(input())
def blackjack(a,b,c):
    zz = a+b+c
    if zz <= 21:
        return  zz
    elif zz > 21 and (a == 11 or b == 11 or c ==11):
        ss = zz - 10
        return ss
    elif ss > 21:
        return "BUST"
print(blackjack(a,b,c))
print('''Made with love by Ⓐ Ⓝ Ⓢ Ⓗ Ⓡ Ⓐ Ⓣ Ⓗ Ⓘ  
            ｇｉｔｈｕｂ ： ｄｕｄｅａｎｓｈ２''')    
        
