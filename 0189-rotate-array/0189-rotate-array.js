/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length;

    // Reverse helper function
    function reverse(arr, start, end) {
        while (start < end) {
            [arr[start], arr[end]] = [arr[end], arr[start]]; // swap
            start++;
            end--;
        }
    }

    // Step 1: Reverse the entire array
    reverse(nums, 0, nums.length - 1);

    // Step 2: Reverse the first k elements
    reverse(nums, 0, k - 1);

    // Step 3: Reverse the rest
    reverse(nums, k, nums.length - 1);

    return nums;
    
};