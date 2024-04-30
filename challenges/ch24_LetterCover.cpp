/*

https://app.codility.com/cert/view/cert24XRG5-PVQKJXEF43NWRMJY/details/
*/

#include <map>
#include <vector>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
int getLettersNum(string S){
    map<char, int> mp;
    for(auto s : S){
        mp[s] += 1;
    }
    // cout << S << ": " << mp.size() << endl;
    return mp.size();
}
vector<char> getLettersUnique(string S){
    map<char, int> mp;
    for(auto s : S){
        mp[s] += 1;
    }
    vector<char> v;
    // cout << S << ": " << mp.size() << endl;
    for(auto m : mp){
        v.push_back(m.first);
    }
    return v;
}
int solution(string &P, string &Q) {
    // Implement your solution here
    int N = P.size();
    /*
    vector<char> ul = getLettersUnique(P + Q);
    
    vector<vector<int>> m_letters;

    for(auto u : ul){
        vector<int> position(N, 0);
        for(int i=1; i<N; i++){
            if(u == P[i]) position[i] += 1;
            if(u == Q[i]) position[i] += 1;
        }
        m_letters.push_back(position);
    }
    */
    /////////////////
    vector<string> v_S;
    std::string s1(1, P[0]);
    v_S.push_back( s1 );
    std::string s2(1, Q[0]);
    v_S.push_back( s2 );
    int v_N = 2;
    
    for(int i=1; i<N; i++){
        for(int j=0; j<v_N; j++){
            v_S.push_back(v_S[j] + Q[i]);
        }
        
        for(int j=0; j<v_N; j++){
            v_S[j] += P[i];
        }
        v_N = v_N*2;

    }
    int min_identy = N;
    for(auto v : v_S){
        int num = getLettersNum(v);
        min_identy = min(min_identy, num);
        if(min_identy <= 1) break;
    }
    return min_identy;
}
