/*
https://app.codility.com/demo/results/trainingXWHATT-4GE/

Note 1, use llabs() rather than abs()
*/

int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    int l = 0, r = N-1;
    int n_distinct = 0;
    {
        while(l<=r){
            n_distinct ++;
            
            if(llabs(A[l]) <  llabs(A[r])){
                int val = llabs(A[r]);
                r --;
                while(llabs(A[r]) == val){
                    r --;
                }
            }
            else if(llabs(A[l]) >  llabs(A[r])){
                int val = llabs(A[l]);
                l ++;
                while(llabs(A[l]) == val){
                    l ++;
                }
            }
            else if(llabs(A[l]) ==  llabs(A[r])){
                int val = llabs(A[l]);
                l ++;
                while(llabs(A[l]) == val){
                    l ++;
                }
                r --;
                while(llabs(A[r]) == val){
                    r --;
                }
            }
            // cout << "1. " << l << ", " <<
            //       r << ", " <<
            //       n_distinct << ", " <<
            //       endl;
        }
    }
    
    return n_distinct;
