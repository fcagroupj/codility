/*
https://app.codility.com/demo/results/trainingT8Q8R2-C3C/
*/

int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    
    sort(A.begin(), A.end());
    int min_abs_sum = abs(A[0] * 2);
    int l = 0, r = N-1;
    while(l <= r){
        int val = abs(A[l] + A[r]);
        min_abs_sum = min(min_abs_sum, val);
        if(min_abs_sum == 0) return 0;

        if(A[l] + A[r] <= 0){
            l ++;
        } else{
            r --;
        }
    }
    return min_abs_sum;
}
