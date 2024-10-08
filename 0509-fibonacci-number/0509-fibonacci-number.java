class Solution {
    public int fib(int n) {
        int prev1 = 1;
        int prev2 = 0;
        int current = 0;
        if(n <2) return n;
        for(int i=2;i< n+1; i++ ){
            current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }        
        return prev1;
    }
}