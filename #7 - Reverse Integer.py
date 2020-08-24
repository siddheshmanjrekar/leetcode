class Solution:
    def reverse(self, x: int) -> int:

        rev, isPositive = 0, 1
        
        if x<0:
            isPositive= -1
            x*= -1 
        
        while x>0:
            rev= (rev*10)+ x%10
            x= x//10
            
        if(rev> 2147483647):
            return 0
            
        return rev * isPositive
        