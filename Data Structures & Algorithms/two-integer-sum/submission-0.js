class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let m = new Map()
        for (let i = 0; i < nums.length; i++){
            const num = nums[i]
            if (m.has(target - num)){
               return [m.get(target - num), i]
            }
            m.set(num, i)
        }
    }
}
