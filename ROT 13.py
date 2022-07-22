import random 
import time

def encode(list_d):
    lis="s"
    for i in list_d:
        r=random.choice(cipher)
        i=i+r
        lis=lis+i
    l="s"
    for i in range(0,len(lis)):
        i=chr(ord(lis[i])+4)
        l=l+i
        password_2=l[2:len(l)]
    print("Adding Record...\n")
    time.sleep(1)
    return password_2
    

def decode(list_e):
    
    l="s"
    for i in range(0,len(list_e)):
        i=chr(ord(list_e[i])-4)
        l=l+i
        q=l[1:len(l):2]
    print("........................................................\n")
    time.sleep(1)
    return q
    


cipher=["~","@","#","$","%","^","&","*","(",\
"+","q","w","e","r","y","u","o","p","l","k","J",\
"5","2","9","6","4","1","G","F","D","S","A","Z","C",\
"V","s","a","x","c","b","n","m","3","7",\
"8","0"]



