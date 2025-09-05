import java.util.*;

class Solution {
    public int[] sortEvenOdd(int[] nums) {
        List<Integer> evens = new ArrayList<>();
        List<Integer> odds = new ArrayList<>();
        
        // Separate even and odd index values
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                evens.add(nums[i]);
            } else {
                odds.add(nums[i]);
            }
        }
        
        // Sort even ascending, odd descending
        Collections.sort(evens); 
        Collections.sort(odds, Collections.reverseOrder());
        
        int[] res = new int[nums.length];
        int e = 0, o = 0;
        
        // Merge back
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                res[i] = evens.get(e++);
            } else {
                res[i] = odds.get(o++);
            }
        }
        
        return res;
    }
}