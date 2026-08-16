class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last=second_last=-1
        last_count=0
        start=0
        ans=0
        for i,fruit in enumerate(fruits):
            if fruit == last:
                last_count+=1
            else:
                if fruit !=second_last:
                    start=i-last_count
                second_last=last
                last=fruit
                last_count=1
            ans=max(ans,i-start+1)
        return ans