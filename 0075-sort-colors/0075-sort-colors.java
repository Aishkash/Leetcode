class Solution {
    public void sortColors(int[] nums) {
        int a=0;
        int i=0;
        int size=(nums.length)-1;
        while(i<=size){
            if(nums[i]==2){
                int temp = nums[i];
                nums[i]=nums[size];
                nums[size]=temp;
                size--;
            }
            else if(nums[i]==0){
                int temp = nums[i];
                nums[i]=nums[a];
                nums[a]=temp;
                a++;
                i++;
            }
            else{
                i++;
            }
        }
        // return nums;
    }
}