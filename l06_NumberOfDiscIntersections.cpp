/*
https://app.codility.com/demo/results/trainingY5W6DF-EBG/
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).
Write a function:

int solution(vector<int> &A);

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
*/

bool sortVKey( pair<int, string> &a,  pair<int, string> &b){
    if(a.first == b.first){
        return(a.second < b.second);
    }
    return a.first < b.first;
}
int solution(vector<int> &A) {
    // Implement your solution here
    int N = A.size();
    vector<pair<int, string>> v;
    for(int i=0; i<N; i++){
        v.push_back(make_pair(i-A[i], "ins"));
        v.push_back(make_pair(i+A[i], "out"));
    }
    sort(v.begin(), v.end(), sortVKey );
    //for(auto m : v){
    //    cout << m.first << " " << m.second << endl;
    //}
    // now add discs
    int n_pairs = 0;
    int n_disc = 0;
    
    for(auto m : v){
        {
            if(m.second == "ins") {
                n_pairs += n_disc;
                if(n_pairs > 10000000) return -1;
                n_disc ++;
            }else{
                n_disc --;
            }
        }
    } 
    return n_pairs;
}
