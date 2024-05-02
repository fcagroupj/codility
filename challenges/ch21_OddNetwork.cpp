/*
https://app.codility.com/demo/results/trainingAY6C8X-E3Y/
[58%]
*/

///
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

vector<int> findConnected(vector<int> &A, vector<int> &B, int node){
    vector<int> nodes;
    int N = A.size();
    for(int j=0; j<N; j++){
        if(A[j] == node) nodes.push_back(B[j]);
        else if(B[j] == node) nodes.push_back(A[j]);
    }
    // cout << node << ": ";
    // for(auto n: nodes){
    //     cout << n << ", ";
    // }
    // cout << endl;
    return nodes;
}
vector<vector<int>> allConnected(vector<int> &A, vector<int> &B){
    vector<vector<int>> all_conn;
    int N = A.size();
    for(int j=0; j<N+1; j++){
        all_conn.push_back( findConnected(A, B, j));
    }
    return (all_conn);
}
int g_paris = 0;
int findAllCons(vector<vector<int>> tab_conn, vector<int> conns, int total_pairs ){
    int N = conns.size();
    if(N < 1) return total_pairs;
    int n_node = conns[N-1];  // last node number
    for(auto a_node : tab_conn[n_node]){
        auto it = find(conns.begin(), conns.end(), a_node);
        if(it == conns.end()){
            
            conns.push_back(a_node);
            int n = conns.size();
            if(n % 2 == 0) {
                total_pairs ++;
                g_paris ++;
                
                cout << "3, ";
                for(auto a_con:conns){
                        cout << a_con << ", ";
                }
                cout << endl;
            }
            findAllCons(tab_conn, conns, total_pairs);
            conns.pop_back();
        }
    }
        
    return total_pairs;
    
}
int solution(vector<int> &A, vector<int> &B) {
    // Implement your solution here
    int N = A.size();
    // 
    vector<vector<int>> tab_conn = allConnected(A, B);

    for(int j=0; j<N+1; j++){
        int pairs = 0;
        vector<int> conns;
        
        conns.push_back(j);
        pairs = findAllCons(tab_conn, conns, pairs);
        
        cout << "4, " << j << ", " <<
             pairs << ", " << g_paris << endl;;
    }
    
    return g_paris/2;
}

int main(){
    //[0, 3, 4, 2, 6, 3], [3, 1, 3, 3, 3, 5]
    vector<int> A;
    A.push_back(0);
    A.push_back(3);
    A.push_back(4);
    A.push_back(2);
    A.push_back(6);
    A.push_back(3);
    vector<int> B;
    B.push_back(3);
    B.push_back(1);
    B.push_back(3);
    B.push_back(3);
    B.push_back(3);
    B.push_back(3);
    solution(A, B);
}
