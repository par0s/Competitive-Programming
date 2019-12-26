class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int R = nums.length;
        while(l < R){
            int mid = l + (R - l)/2;
            if (nums[mid] == target)
                return mid;
            else
                if (nums[mid] > target)
                    R = mid;
                else
                    l = mid + 1;
        }
    return -1;
    }
}
