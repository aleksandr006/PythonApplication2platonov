#def loe_failist(file:str)->str:
#    """loeme tekst failist
#    """
#    f=open(file,"r")
#    stroka=f.read()#str
#    #stroka=f.readlines()#list
#    f.close()
#    return stroka
#stroka=loe_failist("TextFile1.txt")
#print(stroka)
#def loe_failist_listisee(file:str)->list:
#    """loeme tekst failist ja salvesta järgemose
#    """
#    f=open(file,"r")
#    list=[]
#    for stroka in f:
#        list_.append(stroka.strip())
#        f.close()
#        return list_
#spisok=loe_failist("TextFile1.txt")
#print(spisok)
#def salvesta_failisse(file:str):
#    f=open(file,"a")
#    text=input("sisesta teksti")
#    f.write(text+"\n")
#    f.close()
#for i in range(10):
#    salvesta_failisse("Loetelu.txt")
def failis_sisu_umberkirjutamine(file:str):
    text=input("sisesta uus text:")
    with open(file,"w")as f:
        f.write(text+"\n")
failis_sisu_umberkirjutamine(input("file nimetus")+".txt")
    

