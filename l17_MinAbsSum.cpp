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
///////////////////////////////////////////////////////
// it is from Python codes, but it doesn't work
//
//
int solution(vector<int> &A) {
    // Implement your solution here
    int sm = 0;
    int mx = 0;
    for(auto a : A){
        sm += abs(a);
        mx = max(mx, abs(a));
    }
    vector<int> counts(mx+1, 0);
    for(auto a : A){
        counts[a] += 1;
    }
    vector<int> Total(sm+1, -1);
    Total[0] = 0;
    for(int i=1; i<mx+1; i++){
        for(int j=0; j<sm+1; j++){
            if(Total[j] >= 0){
                Total[j] = counts[i];
            }else if(j-i >= 0 && Total[j-i] > 0){
                Total[j] = Total[j-i] - 1;
            }
            /*
            cout << "2: ";
            for(auto t : Total){
                cout << t << ", ";
            }
            cout << endl;
            */
        }
    }
    int result = sm;
    for(int i=0; i < int((sm+1)/2) + 1; i++){
        if(Total[i] >= 0 && result > abs(sm - 2*i))
        result = abs(sm - 2*i);
    }

    return result;
}
