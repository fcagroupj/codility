/*
https://app.codility.com/demo/results/trainingPFC7QP-5N7/
*/
int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    vector<int> peaks;
    for(int i=1; i<N-1; i++){
        if(A[i-1] < A[i] && A[i] > A[i+1]){
            peaks.push_back(i);
        }
    }
    int N_P = peaks.size();
    if(N_P < 1) return 0;
    //for(auto p : peaks){
    //    cout << p << ",";
    //}
    //cout << endl;
    for(int i=N_P; i>0; i--){
        vector<int> flags;
        
        for(auto p : peaks){
            if(flags.size() < 1) flags.push_back(p);
            else{
                if(p-flags[flags.size() - 1] >= i) flags.push_back(p);
            }
            if(int(flags.size()) >= i) {
                return i;
            }
        }

    }
    return 0;
}
