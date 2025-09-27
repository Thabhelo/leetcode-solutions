impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut res = nums[0];
        let mut curr_max = nums[0];
        let mut curr_min = nums[0];
        for &val in nums.iter().skip(1) {
            if val < 0 {
            std::mem::swap(&mut curr_max, &mut curr_min);
            }
            curr_max = std::cmp::max(val, curr_max * val);
            curr_min = std::cmp::min(val, curr_min * val);
            res = std::cmp::max(res, curr_max);
        }
        res
    }
    
}