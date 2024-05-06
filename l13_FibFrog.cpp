/*
https://app.codility.com/demo/results/trainingT3KE95-6VS/
*/

vector<int> getFab(int N){
    vector<int> fabs(N+2, 0);
    fabs[1] = 1;
    for(int i=2; i<N+2; i++){
        fabs[i] = fabs[i-1] + fabs[i-2];
        if(fabs[i] > N+1) break;
    }
    // 0, 1, 1, 2, 3, 5, ...
    return fabs;
}

int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    //cout << "N. " << N << endl;
    if(N <= 2) return 1;
    vector<int> fs = getFab(N);
    vector<int> dp(N+2, N + N);
    dp[0] = 1;
    
    for(int j=1; j<N+2; j++){
        if(j < N + 1){
            if(A[j-1] == 0) continue;
        } 
        //cout << "1. " << j << endl;
        for(int i=2; i<N+2; i++){
            int prev = j - fs[i];
            if(prev >=0 && dp[prev] > 0){
                dp[j] = min(dp[j], dp[prev] + 1);
                // cout << "2. " << j << ", " <<
                //     i << ", " <<
                //     fs[i] << "; " <<
                //     prev << ", " <<
                //     dp[prev] << ", " << 
                //     dp[j] << ", " <<
                //     endl;
            }
            if(prev < 0) break;
        }
    }
    if(dp[N+1] == N + N) return -1;
    return dp[N+1] - 1;
}
