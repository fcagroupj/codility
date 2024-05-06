/*
https://app.codility.com/demo/results/trainingQ7D65T-WQT/
[61%]

*/

int solution(vector<int> &A, vector<int> &B, vector<int> &C) {
    // Implement your solution here
    int N = A.size();
    int M = C.size();
    int n_nailed = 0;
    vector<int> v_nailed(N, 0);
    for(int i=0; i<M; i++){
        for(int k=0; k<N; k++){
            if(v_nailed[k] > 0) continue;
            if(A[k] <= C[i] && C[i] <= B[k]){
                v_nailed[k] += 1;
                n_nailed ++;
            } 
        } 
        if(n_nailed == N) return (i+1);
    }
    return -1;
}
