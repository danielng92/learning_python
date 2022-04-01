array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
so_le=[]
so_chan=[]
for i in range(0,len(array)):
    if array[i]%2==0:
        so_chan.append(array[i])
    else:
        so_le.append(array[i])
print('so chan: ',so_chan)
print('so le: ',so_le)
    