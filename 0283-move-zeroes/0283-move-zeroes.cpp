class Solution {
public:
    void moveZeroes(vector<int>& arr) {
        int i = -1;
        for (int j = 0; j < arr.size(); j++) {
            if (arr[j] == 0) {
                i = j;
                break;
            }
        }
        if (i == -1)
            return;
        for (int j = i+1; j < arr.size(); j++) {
            if (arr[j] != 0) {
                swap(arr[i], arr[j]);
                 i++;
            }
        }
    }
};