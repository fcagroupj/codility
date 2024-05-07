/*
https://app.codility.com/demo/results/trainingVPJG8D-VZ4/
[76%]

There are N points (numbered from 0 to N−1) on a plane. Each point is colored either red ('R') or green ('G'). The K-th point is located at coordinates (X[K], Y[K]) and its color is colors[K]. No point lies on coordinates (0, 0).

We want to draw a circle centered on coordinates (0, 0), such that the number of red points and green points inside the circle is equal. What is the maximum number of points that can lie inside such a circle? Note that it is always possible to draw a circle with no points inside.

Write a function:

class Solution { public int solution(int[] X, int[] Y, String colors); }

that, given two arrays of integers X, Y and a string colors, returns an integer specifying the maximum number of points inside a circle containing an equal number of red points and green points.
*/

#include <cmath>
bool sortKey(pair<float, string> a, pair<float, string> b){
    return a.first > b.first;
}
int solution(vector<int> &X, vector<int> &Y, string &colors) {
    // Implement your solution here
    int N = X.size();
    vector<pair<float, string>> v_points(N);
    int N_R = 0, N_G = 0;
    for(int i=0; i<N; i++){
        float rad = sqrtf(X[i]*X[i] + Y[i]*Y[i]);
        string s_color(1, colors[i]);
        v_points.push_back(pair(rad, s_color));
        if(s_color == "R") N_R ++;
        else N_G ++;
    }
    if(N_G == N_R) return (N_G + N_R);
    sort(v_points.begin(), v_points.end(), sortKey);
    int i = 0;
    while(i < N){
        int k = i;
        int n_r=0, n_g=0;
        while(v_points[i] == v_points[k]){
            
            if(v_points[k].second == "R") n_r ++;
            else n_g ++;
            k ++;
        }
        N_R -= n_r;
        N_G -= n_g;
        if(N_G == N_R) return (N_G + N_R);
        i = k;
    }
    return 0;
}
