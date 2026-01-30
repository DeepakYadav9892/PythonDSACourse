class Solution:
    def contain_duplicate(self,nums:list[int])->bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

obj=Solution()
data=[1,2,3,43,4,3,7]
result=obj.contain_duplicate(data)

print(result)



