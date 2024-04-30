/*
https://app.codility.com/demo/results/trainingGKC3C2-NUA/
[61%]
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

int solution(vector<int> &A);

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.
*/
int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    int max_sum = INT_MIN;
    
    for(int i=1; i<N-1; i++){ // the middle one
        int max_s1 = 0, max_s2 = 0;
        int s1=0, s2=0;
        int j = i-1;
        while(j > 0){
            s1 += A[j];
            if(s1 <= 0) break;
            max_s1 = max(s1, max_s1);
            j --;
        }
        j = i+1;
        while(j < N-1){
            s2 += A[j];
            if(s2 <= 0) break;
            max_s2 = max(s2, max_s2);
            j ++;
        }
        max_sum = max(max_sum, max_s1+max_s2);
    }
    return max_sum;
