number=[1,2,3,4,5,6,7,8,9]
so_chan=0
so_le=0
for i in range(0,len(number)):
  if number[i]%2==0:
    so_chan+=1
  else:
    so_le+=1


print("Even numbers: ", so_chan)
print("Odd numbers: ", so_le)
