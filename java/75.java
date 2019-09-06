
class Solution {
    //记录不同数字总的出现次数
    //扫一遍
    public void sortColors(int[] nums) {
        int low = 0;
        int high = nums.length-1;
        int index = 0;
        while(index<=high) {
            if(nums[index] == 2) {
                int tmp = nums[high];
                nums[high--] = nums[index];
                nums[index] = tmp;
            }
            else if(nums[index] == 1) index++;
            else{
                int tmp = nums[low];
                nums[low++] = nums[index];
                nums[index] = tmp;
                index++;
            }
        }

//        //计数排序算法
//        for(int i=0; i<nums.length; i++) {
//            count[nums[i]]++;
//        }
//
//        //location 记录不同数字当前的插入位置
//        int[] location = {0,0,0};
//        for (int i=1; i<3; ++i) {
//            location[i] = location[i-1] + count[i-1];
//        }
//
//        int[] tmp = new int[nums.length];
//        for(int i=0; i<nums.length; i++) {
//            tmp[location[nums[i]]] = nums[i];
//            location[nums[i]]++;
//        }
//        for (int i:
//             tmp) {
//            System.out.print(i);
//        }
//        nums = tmp;

//        //不对原始数据进行区分
//        count = new int[3];
//        for(int i=0; i<nums.length; i++)
//            count[nums[i]]++;
//        int index = 0;
//        for(int i=0; i<3; ++i) {
//            while(count[i]-->0) {
//                nums[index++] = i;
//            }
//        }
    }
}