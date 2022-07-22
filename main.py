import random ,csv,time,getpass
from tabulate import tabulate


admin=False
User="Aman"

cipher=["~","@","#","$","%","^","&","*","(",\
"+","q","w","e","r","y","u","o","p","l","k","J",\
"5","2","9","6","4","1","G","F","D","S","A","Z","C",\
"V","s","a","x","c","b","n","m","3","7",\
"8","0","~","@","#","$","%","^","&","*","(","+","1","3","7","8","0"]


                      
                         ############# FUNCTIONS ##################

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
    print("\nAdding Record...")
    time.sleep(0.25)
    return password_2
    
def decode(list_e):
    
    l="s"
    for i in range(0,len(list_e)):
        i=chr(ord(list_e[i])-4)
        l=l+i
        q=l[1:len(l):2]
    return q
    
def generator(len_pass):
    options=cipher
    pass_word=[]
    for i in range(0,len_pass+1):
        word=random.choice(options)
        pass_word.append(word) 
    print("\nYOUR PASSWORD:",end="")
    for i in pass_word:
        print(i,end="")
    print("\n")

def csv_writer(username,e_mail_id,password,web_name):
    row=[username,e_mail_id,password,web_name]

    with open("First_Pass.csv", 'a', encoding="utf-8") as file:
        csv_write= csv.writer(file)
        csv_write.writerow(row)
    file.close()

def csv_reader():
    final_row=[["Username","E-Mail Id","Password","Website"]]
    with open("First_Pass.csv",'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row!=[]:
                pw=decode(row[2])
                table2=[row[0],row[1],pw,row[3]]
                final_row.append(table2)
            elif row==[]:
                continue
        print("\n")
        print(tabulate(final_row))
    csvfile.close()

def csv_search(to_be_searched):
    final_row=[["Username","E-Mail Id","Password","Website"]]
    with open("First_Pass.csv",'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row!=[]:
                if (to_be_searched in row[0]) or (to_be_searched in row[3]):
                    final_row.append([row[0],row[1],decode(row[2]),row[3]])
                else:
                    continue
            if row==[]:
                continue
        print("\n")
        if final_row==[["Username","E-Mail Id","Password","Website"]]:
            print("No Records Found !!")  
        elif final_row!=[["Username","E-Mail Id","Password","Website"]]:
            print(tabulate(final_row))
    csvfile.close()

def choice_2_3():

        if choice==2:
            user_name=str(input("\nEnter Username: "))
            e_mail=str(input("Enter Valid E-Mail ID: "))
            password_1=str(input("Enter Password: "))
            web_name=str(input("Enter Name Of Website: "))
            password_2= encode(password_1)
            csv_writer(user_name,e_mail,password_2,web_name)
            print("\nRecord Entered !!")

        elif choice==3:
            csv_reader()
        
def validate_main_pass(key):
    if len(key)==16:
        if key==(chr(83)+chr(79)+chr(67)+chr(73)+chr(65)+\
            chr(76)+chr(104)+chr(97)+chr(99)+chr(107)+chr(101)\
            +chr(114)+chr(50)+chr(48)+chr(48)+chr(51)):
        
            print(f"\nWelcome Back,{User}!!") 
            return True
        else:
            return False              
    elif len(key)!=16:
        return False

                    
running=True
                    #############  MAIN  ####################

while running:
    time.sleep(1)
    print("\n-----------------------------------------------------------------")
    print("\nPress 1 To Generate Secure Password. ")
    print("\nPress 2 To Enter Record. ")
    print("\nPress 3 To Read Records. ")
    print("\nPress 4 To Search Record Based On Username/Website. ")
    print("\nPress 5 To Exit. ")

    print("\n--------------------------------------------------------------------\n")
    choice=int(input("Enter Your Choice: "))

    try :
        if choice==1:
            print("\n")
            len_pass=eval(input("Enter Length Of Password(8-25): "))
            if len_pass<=25 and len_pass>=8:
                generator(len_pass)
            else:
                print("\nERROR !! ")

        elif choice in (2,3):
            if admin==False:
                main_pass=getpass.getpass("Enter Master Password:")
                check_pass=validate_main_pass(main_pass)
                if check_pass==True:
                    admin=True
                    choice_2_3()
                elif check_pass==False:
                    print("Wrong Password")
                    running=False
            elif admin==True:
                choice_2_3()

        elif choice==4:
            if admin==False:
                main_pass=getpass.getpass("Enter Master Password:")
                check_pass=validate_main_pass(main_pass)
                if check_pass==True:
                    admin=True
                    print("\n")
                    to_be_searched=str(input("Enter Username/Website To Be Searched: "))
                    csv_search(to_be_searched) 
                elif check_pass==False: 
                    print("Wrong Password")
                    running=False 
            elif admin==True:
                print("\n")
                to_be_searched=str(input("Enter Username/Website To Be Searched: "))
                csv_search(to_be_searched)  

        elif choice==5: 
            print("\nBye !!")
            running=False

    except NameError:
        print("Enter Correct Values !!")
