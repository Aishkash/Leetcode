class Solution {
    public int maxSubArray(int[] nums) {
        int a=0;
        int ans=Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++){
            a+=nums[i];
            ans=Math.max(a,ans);
            if(a<0){
                a=0;
            }
        }return ans;
        
    }
}