/*
https://app.codility.com/demo/results/training6PNCK5-QCB/
[63%]
*/

bool sortKey(int a, int b){
    return abs(a) > abs(b);
}
int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    if(N < 1) return 0;
    sort(A.begin(), A.end(), sortKey);
    // for(auto a : A){
    //     cout << a << ", ";
    // }
    // cout << endl;

    vector<int> dp(N+1, numeric_limits<int>::max());
    dp[0] = abs( A[0] );
    for(int i=1; i<N; i++){
        dp[i] = min( abs(dp[i-1] + A[i]), abs(dp[i-1] - A[i]) );
    }
    return dp[N-1];
}
