def nums_roami (a):
    num_roami={"I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
    
    s=0  
    for i in range(len(a)-1):
        
            
        if num_roami[a[i]] < num_roami [a[i+1]]:
            s-=num_roami[a[i]]
        else :
            s+=num_roami[a[i]]
    s += num_roami[a[-1]]
    return s
print(nums_roami(input("inter your symbol:")))