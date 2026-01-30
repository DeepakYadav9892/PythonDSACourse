class solution:
    def reverse(self,s:list[str])->None:
        left,right=0,len(s)-1

        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1


#Running the function 

obj=solution()
data=['H','l','l','o']
obj.reverse(data)
print(data)