/*
https://app.codility.com/demo/results/trainingPUSJAR-7Z6/
[61%]
*/

#include <map>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
bool isPretty(string A, string B){
    return (A[1] == B[3]);
}
bool isAllPretty(vector<string> &A) {
    int N = A.size();
    //int K = 4;
    bool all_pretty = true;
    
    for(int i=0; i<N-1; i++){
        if(!isPretty(A[i], A[i+1])){
            all_pretty = false;
            break;
        }
    }
    return all_pretty;
}
string rotCW(string A, int n){
    string B = A;
    int N = A.size();
    for(int i=0; i<4; i++){
        B[i] = A[(i-n+N) % N];
    }
    return B;
}
string rotCC(string A, int n){
    string B = A;
    int N = A.size();
    for(int i=0; i<4; i++){
        B[i] = A[(i+n+N) % N];
    }
    return B;
}
string rotTitle(string A, int n){
    if(n == 1) return rotCC(A, 1);
    else if(n == 2) return rotCC(A, 2);
    else if(n == 3) return rotCW(A, 1);
    return A;
}
int getRotTime(int i){
    if(i <= 2) return i;
    else return 1;
}
int solution(vector<string> &A) {
    // Implement your solution here
    int N = A.size();
    // create a list to save all possible rotated string and total rotating time for each title 0...N-1
    // each title should compare with the previous and save the new mapping data
    vector<map<string, int>> dp;
    int K = 4;  // no rotate, cw+1, cw+2, cc+1
    for(int j=0; j<N; j++){
        map<string, int> tit_rot;
        for(int i=0; i<K; i++){
            string B = rotTitle(A[j], i);
            
            if(j-1 >= 0){
                for(auto m : dp[j-1]){
                    if(isPretty(m.first, B)){
                        int total_r = m.second+getRotTime(i);
                        tit_rot.insert( {B, total_r} );
                        //cout << "2, tit_rot insert  " << B << ", " << 
                        //    total_r << ", " << 
                        //    m.second << ", " << 
                        //    i << endl;
                    }
                }
                
            } else{
                tit_rot.insert( {B, getRotTime(i)} );
                //cout << "1, tit_rot insert  " << B << ", " << getRotTime(i) << endl;
            }
        }
        dp.push_back(tit_rot);
    }
    int min_rotates = N * 2 + 1;
    int M = dp.size();
    if(M >= N){
        for(auto m : dp[N-1]){
            min_rotates = min(min_rotates, m.second);
        }
    }
    return min_rotates;
}
