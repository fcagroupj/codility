/*
https://app.codility.com/demo/results/trainingWPG53G-325/
[100%]
*/
int solution(vector<int> &A, vector<int> &B) {
    // Implement your solution here
    int N = A.size();
    vector<int> rotCons(N, 0);
    for(int i=0; i<N; i++){
        
        for(int j=0; j<N; j++){
            if(A[i] == B[j]){
                int rot = (i - j + N) % N;
                rotCons[rot] ++;
            }
        }
    }
    for(int i=0; i<N; i++){
        if(rotCons[i] <= 0) return i;
    }
    
    return -1;
}

/*
https://app.codility.com/demo/results/trainingB988DB-XHG/


*/
int solution(vector<int> &A, vector<int> &B) {
    // Implement your solution here
    int N = A.size();
    vector<int> rotCons;
    for(int i=0; i<N; i++){
        
        for(int j=0; j<N; j++){
            if(A[i] == B[j]){
                int rot = (i - j + N) % N;
                rotCons.push_back(rot);
            }
        }
    }
    int M = rotCons.size();
    if(M < 1) return 0;
    sort(rotCons.begin(), rotCons.end());
    int start = 0, i=0;
    while(i < M){
        if(rotCons[i] != start){
            return start;
        } 
        while(rotCons[i] == start){
            i ++;
        }
        start++;
    }
    return -1;
}

/*

As a reference
https://app.codility.com/demo/results/trainingR7PCW9-QFK/
*/
bool checkNoDislike(vector<int> &A, vector<int> &C){
    int N = A.size();
    
    for(int i=0; i<N; i++){
        if(A[i] == C[i]){
            return false;
        }
    }
    return true;
}
bool checkSame(vector<int> &B, vector<int> &C){
    int N = B.size();
    
    for(int i=0; i<N; i++){
        if(B[i] != C[i]){
            return false;
        }
    }
    return true;
}
int solution(vector<int> &A, vector<int> &B) {
    // Implement your solution here
    
    /////////////
    vector<int> C(N, 0);
    for(int i=0; i<N; i++){
        C[i] = B[i];
    }
    int rot = 0;
    while(true){
        if(checkNoDislike(A, C)) return rot;
        rot ++;
        
        for(int i=0; i<N; i++){
            C[i] = B[(i-rot + N)%N];
        }
        if(checkSame(C, B)) break;
        
    }
    return -1;
}
