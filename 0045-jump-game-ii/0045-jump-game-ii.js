/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let pos = nums.length - 1;
    let count = 0;
    while (pos > 0) {
        for (let i = 0; i < pos; i++) {
            if (i + nums[i] >= pos) {
                pos = i;
                count++;
                break;
            }
        }
        
    }
    return count;
}
    