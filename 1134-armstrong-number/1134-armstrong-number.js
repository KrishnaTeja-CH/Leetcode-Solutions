/**
 * @param {number} n
 * @return {boolean}
 */
var isArmstrong = function(n) {
    let sol = Array.from(String(n), Number);
    let res = 0
    sol.forEach(i=>{res += Math.pow(i, sol.length);});
    return res==n;
}