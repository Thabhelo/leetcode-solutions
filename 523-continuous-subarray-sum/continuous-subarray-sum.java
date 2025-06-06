import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); // hashmap with remainder and index as keys, and values
        int prefixSum = 0;

        for (int i = 0; i < nums.length; i++){
            prefixSum += nums[i];

            int remainder = prefixSum % k;

            if (map.containsKey(remainder)) {
                if (i - map.get(remainder) > 1) {
                    return true;
                }
            } else {
                map.put(remainder, i);
                }
        }
        return false;   
    }
}