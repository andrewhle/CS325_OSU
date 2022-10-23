
def max_independent_set(nums): 
    dp=[0 for i in range(len(nums))]
    dp[0]=nums[0]  
    dp[1]=nums[1]  
    for i in range(2,len(nums)): 
        dp[i]=max(nums[i],nums[i]+dp[i-2],dp[i-2],dp[i-1])
    i=len(nums)-1  
    lis=[]   
    while(i>1): 
        if dp[i]==dp[i-1]:  
            i-=1 
        elif dp[i]==nums[i]: 
            lis.append(nums[i])
            lis.reverse()
            return lis
        elif dp[i]==dp[i-2]+nums[i]: 
            lis.append(nums[i])
            i=i-2
        else:        
            i=i-2
    if i==0:   
        if(nums[i]>0 or len(lis)==0): 
            lis.append(nums[i])
    else:
        t=max(nums[0],nums[1]) 
        if(t>0 or len(lis)==0): 
            lis.append(t)
    lis.reverse() 
    return lis 



arr=[15, 15, 25, 0, 0, 0, 15, 15]

max_independent_set(arr)
