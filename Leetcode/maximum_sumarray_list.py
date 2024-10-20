lis = [2, 3, -8, 7, -1, 2, 3]

c_sum = lis[0]
mx = lis[0]

start = 0
end  = 0
temp = 0
for i in range(1,len(lis)):
    if c_sum <0:
        c_sum = lis[i]
        temp = i
    else:
        c_sum = c_sum + lis[i]
        
    if c_sum> mx:  
       mx = max(mx,c_sum)
       end = i
       start  = temp
    
print(mx)
print(lis[start:end+1])
    


