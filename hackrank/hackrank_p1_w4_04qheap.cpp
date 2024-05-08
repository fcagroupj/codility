/*
This question is designed to help you get a better understanding of basic heap operations.

There are  types of query:

"1 v" - Add an element  to the heap.
"2 v" - Delete the element  from the heap.
"3" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N;
    cin >> N;
    vector<int> data;
    for(int i=0; i<N; i++){
        int op, value;
        cin >> op;
        if(op == 1){
            cin >> value;
            int M = data.size();
            bool found = false;
            for(int j=0; j<M; j++){
                if(data[j] == value){
                    found = true;
                    break;
                } else if(data[j] > value){
                    data.insert(data.begin()+j, value);
                    found = true;
                    break;
                }
            }
            if(! found) data.push_back(value);
        }else if(op == 2){
            cin >> value;
            int M = data.size();
            for(int j=0; j<M; j++){
                if(data[j] == value){
                    data.erase(data.begin() + j);
                }
            }
            
        }else{
            int M = data.size();
            if(M > 0){
                // int min_d = data[0];
                // for(auto d: data){
                //     if(d < min_d) min_d = d;
                // }
                cout << data[0] << endl;
            }
            
        }
    }
    return 0;
}
