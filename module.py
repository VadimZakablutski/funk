def arithmetic(a: float,b:float,c=str):
    """Lihtne kalkulaator
    + - liitamine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
    else:
        print("Viga!")
    return("")
def is_year_leap(year:int):
    if year%4==0:
        print("True")
    else:
        print("False")
    return("")
def square(kv:float):
    return(4*kv, kv**2, (2*kv**2)**.5)
    return("")
def season(kuu:int):
    if kuu==12:
        print("Зима")
    elif 0<kuu<3:
        print("Зима")
    elif 2<kuu<6:
        print("Весна")
    elif 5<kuu<9:
        print("Лето")
    elif 8<kuu<12:
        print("Осень")
    else:
        print("Viga!")
    return
def bank(a:float,years:int):
    for _ in range(years):
        a=((1.1*1/100)*a)*100
    print("Ваш баланс:",a)
    return("")
def is_prime(a:int):
    b=2
    while a%b!=0:
        b+=1
    return b==a
def xor_cipher(string:str, key:str)->str:
    """ Tavaline sõna kodeeritakse
    """
    result=""
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i]) #näitab sümnoli kood
        for j in range(len(key)):
            temp ^= ord(key[j])
        result += chr(temp)
    return result 
def xor_uncipher(string:str, key:str)->str:
    """ Kodeeritud text dekodeeritakse
    """
    result=""
    temp=[]
    for i in range(len(string)):
        temp .append(string[i])
        for j in reversed(range(len(key))):
            temp[i]=chr(ord(key[j])) ^ ord(temp[i])
        result += temp[i]
    return result
def date(day:int, month:int, year:int):
    set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
    else:
        return False

