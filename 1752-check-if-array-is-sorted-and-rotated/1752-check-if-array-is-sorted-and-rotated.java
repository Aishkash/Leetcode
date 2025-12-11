class Solution {
    public boolean check(int[] nums) {
        int ln= nums.length;
        int count=0;
        for(int i=0; i<ln; i++){
            if(nums[i]>nums[(i+1)%ln]){
                count=count+1;
            }
        if(count>1){
            return false;
        }
        }
        return true;
    }
        
}