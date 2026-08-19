class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(arr)
        arr2=[]
        for i in range(len(arr)-k,len(arr)):
            arr2.append(arr[i])
        print(arr2)
        for i in range(len(arr) - k - 1, -1, -1):
            arr[i + k] = arr[i]
        for i in range(k):
            arr[i]=arr2[i]
        