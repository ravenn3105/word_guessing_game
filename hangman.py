import random
s=['apple','ipad','mouse','laptop','bed','wardrobe','bottle','umbrella']
conti="yes"
while conti=="yes":
    a=random.randrange(len(s))
    m=s[a]
    print("")
    print("length of your word is:",len(m))

    print("no of guesses=10\n")
    b=list(m)
    l=set(m)

    z=[]
    e=[]


    for i in range(10):
        count=0
        c=input("your guess:\n")
        if c in m and c!="":
            print("\tCorrect guess!\n")
            z.append(c)
            for k in b:
                if k==c or k in z:
                    print(k, end=" ")
           
                else:
                    print("_", end=" ")
         
            e.append(c)
            print()
            print("\tyour guesses",e)
            for j in b:
                if j==c:
                    count=count+1
                else:
                    count= count  
            
            print("\tno of that letter in your word:",count)
            print("")
            if set(e)==l:
                print("\thooray! your word is:",m)
                break
        else:
            print("\tOops. try again\n")
            t=9-i
            print("\tno. of tries left",t)
            if t==0:
                print("\t!!!!! GAME OVER !!!!!")
                print("\tYour word was:", m)
                break
    conti=input("wanna play again? (yes/no)")


