import random
users=["Marina"]
password=["12345"]
def passcontrol(psword):
    psword=list(psword)
def passauto()->str:
    """loob arvuti automatselt parool 
    """
    str0 = ".,:;!*-+()/#¤%&"
    str1 = "123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Берём из списка 12 слюбых символов
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов 
    return psword
def paskontroll(psword:str)->bool:
    ls=list(psword)
    for e in ls:
        if e.isdigit(): d=True
        if e.isalpha(): a=True
        if e.isupper(): u=True
        if e.islower(): l=True
        if e in (".,:;!*-+()/#%&"): s=True
    if d==True and a==True and u==True and l==True and s==True :
       t=True
    else:
        t=False
    return t 
def reg():
    while 1:
        log=input("kasutaja tunnus")
        if log not in users:
            print("Tunnus soobib")
            break
        else:
            print("see nimi juba on olemas listis")
        v=input("Arvuti-A või ise-I loob parool")
        if v.upper()=="A": 
            pas=passauto()
        elif v.upper()=="I":
            pas=input("Sisesta oma parool")
            tulemus=passcontrol(pas)
        if tulemus==True:
            user.append(log)
            passwords.append(pas)
            break
