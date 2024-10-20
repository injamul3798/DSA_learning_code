if __name__ == '__main__':
    no = int(input())
    cnt = 0
    arr = map(int,input().split())
    
    target = int(input())
    
    lis_elements = []
    
    for i in arr:
        lis_elements.append(i)
    lis_elements.sort()
    
    for i in range(len(lis_elements)-1, -1, -1):
        while(lis_elements[i] <= target):
            target = target - lis_elements[i]
            cnt += 1
    print(cnt)
    
    """for i in range(len(lis_elements)-1, -1, -1):
        while(target>0 and target>=lis_elements[i]):
        
            total_el_cnt = target // lis_elements[i]
            cnt += total_el_cnt
            target = target - lis_elements[i]*total_el_cnt  # 200 
        if target==0:
            break"""
            
    #print(cnt)
    
 