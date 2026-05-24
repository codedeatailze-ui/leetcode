def addTwoNumbers(l1, l2):
    result = []
    carry = 0
    i, j = 0, 0
    
  
    while i < len(l1) or j < len(l2) or carry:
      
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[j] if j < len(l2) else 0
        
     
        total = val1 + val2 + carry
        
      
        carry = total // 10
        
   
        result.append(total % 10)
        
        i += 1
        j += 1
    
    return result



print(addTwoNumbers([2,4,3], [5,6,4]))     # [7,0,8]  (342 + 465 = 807)
print(addTwoNumbers([0], [0]))              # [0]
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))  # [8,9,9,9,0,0,0,1]