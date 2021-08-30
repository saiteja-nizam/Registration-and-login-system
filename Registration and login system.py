def start(u):
    print("Enter \n 1 for Registration\n 2 for login \n 3 for forgot password")
    a=int(input())
    if(a==1):
        username=input("Enter username:")
        if username.count("@")==1 and username.count(".")==1:
            if username.index(".")-username.index("@")>1:
                if username[0].isalpha():
                    password=input("Enter password:")
                    if (password.islower() or password.isupper()) is False:
                        if password.isalnum() is False:
                            c=0
                            for t in password:
                                if t.isdigit():
                                    c+=1
                            if c>0:
                                if (len(password)>5 and len(password)<16):
                                    print("Registration is succesful!")
                                    data=username+":"+password+" "
                                    f0=open("sd.txt","a")
                                    f0.write(data)
                                    f0.close()
                                    start(u)
                                else:
                                    print("password length must be between 5 and 16")
                                    start(u)
                            else:
                                print("password must have one digit")
                                start(u)
                        else:
                            print("password must have one special character")
                            start(u)
                    else:
                        print("password must have one lower case and one upper case character")
                        start(u)
                else:
                    print("username can't start with special character or number")
                    start(u)
            else:
                print(". can't preceed @ and can't be immediately followed by @")
                start(u)
        else:
            print("username must and can have only one @ and .")
            start(u)
    elif(a==2):
        x=input("enter username:")
        w=input("enter password:")
        f1=open("sd.txt","r")
        l=f1.read().rstrip()
        k=l.split(" ")
        username=[]
        password=[]
        for z in k:
            s,t=z.split(":")
            username.append(s)
            password.append(t)
        if x in username:
            p=username.index(x)
            if w==password[p]:
                print("Welcome!logged in succesfully!")
                start(u)
            else:
                print("password incorrect")
                start(u)
        else:
            print("Username credentials doesn't exist,Go to registration")
            start(u)
        f1.close()
    elif(a==3):
        x=input("enter username:")
        f2=open("sd.txt","r")
        l=f2.read().rstrip()
        k=l.split(" ")
        username=[]
        password=[]
        for z in k:
            s,t=z.split(":")
            username.append(s)
            password.append(t)
        if x in username:
            p=username.index(x)
            print("password:"+password[p])
            start(u)
        else:
            print("Enter valid username")
            start(u)
        f2.close()
    else:
        print("choose relevant number")
        start(u)
print("press Enter to start")
u=input()
start(u)

            
    

     
            
