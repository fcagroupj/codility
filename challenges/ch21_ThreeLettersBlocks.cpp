/*
https://app.codility.com/demo/results/trainingEHHK4R-9ZT/
[38%]
*/
#include <map>
#include <vector>

int solution(string &S) {
    // Implement your solution here
    vector<map<string, int>> dp;
    int i = 0;
    for(auto s: S){
        map<string, int> mp;
        int K = dp.size();
        if(K > 0){
            for(auto d: dp[K-1]){
                string s1(1, s);
                int M = d.first.size();
                int n_block = d.second;
                if(M > 0){
                    if(d.first[M-1] != s) n_block ++;
                } else n_block ++;
                if(n_block <= 3){
                    mp.insert({d.first+s1, n_block});
                    //cout << i << ", " << 
                    //    d.first+s1 << ", " <<
                    //    n_block << ", " << s1 <<
                    //    endl;
                }
                // delete itself
                mp.insert({d.first, d.second});
                //cout << i << ", " << 
                //        d.first << ", " <<
                //        d.second << 
                //        endl;
            }
        } else {
            string s1(1, s);
            mp.insert({s1, 1});
            mp.insert({"", 0});
        }
        if(mp.size() > 0)
            dp.push_back(mp);
        i ++;
    }
    int K = dp.size();
    int max_s = 0;
    //cout << "2, " << K << ", " << max_s << endl;
    if(K > 0){
        for(auto d: dp[K-1]){
            int L = d.first.size();
            max_s = max(max_s, L);
            //cout << "3, " << d.first << ", " << max_s << endl;
        }
    }
    return max_s;
}
