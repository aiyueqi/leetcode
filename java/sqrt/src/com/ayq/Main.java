package com.ayq;

import java.lang.reflect.Array;
import java.util.Arrays;

class Solution {
    public int maximumGap(int[] nums) {
        Arrays.sort(nums);
        int max=0;
        for(int i=1;i<nums.length;i++) {
            int now = nums[i] - nums[i-1];
            max = now > max ? now : max;
        }
        return max;
    }
}
