n=7
for i in range(n): #0<=i<7
    for j in range(n):#0<=j<7 chay het vong lap j thi moi bat dau lai vong lap i
       if j==0 or j==6 or i==j:
           print('*',end=' ')
       else: 
            print('',end='  ')
    print(' ')



n=7
for i in range(n): #0<=i<7
    for j in range(n):#0<=j<7 chay het vong lap j thi moi bat dau lai vong lap i
       if i==0 or i==6 or i==j:
           print('*',end=' ')
       else: 
            print('',end='  ')
    print(' ')
