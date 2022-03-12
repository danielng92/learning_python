array=[100,2.5,300,"h",500,4.6,700,800,5,1000]
length=len(array)
print(length)
n=1000
flag = False
for i in range(0,length):   # for 0 to length of an array = O(n)
    if n==array[i]:
        flag = True 

if flag == False:               # if - else = O(1) mean no time => O(n) + O(1) = O(n)
    print("Not Found")
elif flag == True: 
    print("Found", n ) 