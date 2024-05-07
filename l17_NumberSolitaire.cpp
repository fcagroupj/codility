/*
https://app.codility.com/demo/results/trainingH8UJHH-2PX/
*/

#include <limits>

int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    vector<int> dp(N+1, -numeric_limits<int>::max());
    int K = 6;
    dp[0] = A[0];
    for(int j=1; j<N; j++){
        for(int i=1; i<K+1; i++){
            int prev = j - i;
            if(prev >= 0){
                dp[j] = max(dp[j], dp[prev] + A[j]);
            }
        }
    }
    return dp[N-1];
}
