/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let sol ={};
    for(let i = 0; i<nums.length; i++){
        
        let k = target - nums[i];
        if (k in sol){
            return [sol[k], i];
        }
        sol[nums[i]] = i;
    }
    return [];
}