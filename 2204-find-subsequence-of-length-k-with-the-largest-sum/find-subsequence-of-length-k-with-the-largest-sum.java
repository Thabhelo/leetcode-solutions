import java.util.*;

class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        // Convert array to list for easier manipulation
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }
        
        // Remove minimum elements until we have k elements left
        for (int i = 0; i < nums.length - k; i++) {
            // Find the minimum value in the current list
            int minValue = Collections.min(list);
            // Remove the first occurrence of the minimum value
            list.remove(Integer.valueOf(minValue));
        }
        
        // Convert back to array
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}