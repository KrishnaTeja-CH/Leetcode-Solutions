/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossibleToSplit = function(nums) {
    const count = {};
    for(const i of nums){
        count[i] = (count[i] || 0) + 1;
        
        if (count[i] > 2){
            return false;
        }
    }
    return true;
}