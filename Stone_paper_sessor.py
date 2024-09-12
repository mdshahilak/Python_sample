import random
li=["stone","paper","sessor"]
rou = int(input("Enter the round:"))
i=0
mark_of_pc = 0
mark_of_user = 0
while(i<rou):
    ch = input("give your choice"+str(i+1)+":")
    ran = random.choice(li)
    i+=1
    if(ch==ran):
        mark_of_pc = 0
        mark_of_user = 0
    elif((ran=="paper" and ch=="stone")or(ran=="stone" and ch=="sessor")or(ran=="sessor" and ch=="paper")):
        mark_of_pc += 1
    else:
        mark_of_user += 1
    print("random:"+ran)
    
print("mark of th user"+ str(mark_of_user))
print("mark of th pc"+ str(mark_of_pc))
    
        
        
