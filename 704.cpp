#include<algorithm>
class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto it = lower_bound(nums.begin(), nums.end(), target);
        return it == nums.end() || *it != target? -1 : it - nums.begin();
    }
};
