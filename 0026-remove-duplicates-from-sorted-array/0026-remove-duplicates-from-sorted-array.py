class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        i =0
        j=0
        while (j<len(arr)):
            if (arr[i]==arr[j]):
                j+=1
            else:
                i+=1
                arr[i]=arr[j]
        return i+1
        