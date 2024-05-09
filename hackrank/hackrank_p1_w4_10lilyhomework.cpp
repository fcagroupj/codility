#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'lilysHomework' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
bool sortKey(int a, int b){
    return (a > b);
}
int lilysHomework(vector<int> arr) {
    int N = arr.size();
    vector<int> arr_asc;
    vector<int> arr_des;
    map<int, int> mp;
    int i = 0;
    for(auto a : arr){
        arr_asc.push_back(a);
        arr_des.push_back(a);
        mp[a] = i;
        i ++;
    }
    sort(arr_asc.begin(), arr_asc.end());
    int n_dif_asc = 0;
    for(int i=0; i<N; i++){
        if(arr_asc[i] != arr[i]) n_dif_asc ++;
    }
    sort(arr_des.begin(), arr_des.end(), sortKey);
    int n_dif_des = 0;
    for(int i=0; i<N; i++){
        if(arr_des[i] != arr[i]) n_dif_des ++;
    }
    // choose to be ascending or descending list
    vector<int> arr_tgt = arr_asc;
    if(n_dif_asc > n_dif_des) {
        arr_tgt = arr_des;
        n_dif_asc = n_dif_des;
    }
    // list all swaps by position: soure -> target
    map<int, int> mp_target;
    for(int i=0; i<N; i++){
        if(mp[arr_tgt[i]] != i){
            mp_target[ mp[arr_tgt[i]] ] = i;
        }
    }
    cout << "1: ";
    for(auto m : mp_target){
        cout << m.first << " -> " << m.second << ", ";
    }
    cout << endl;
    int min_swaps = 0;
    while(n_dif_asc > 0){
        bool b_diff = false;
        // exchange all swaps  source and target are paired with each other
        for(auto m : mp_target){
            if(m.first == m.second) continue;
            if(mp_target[m.second] == m.first){
                min_swaps ++;
                mp_target[m.first] = m.first;
                mp_target[m.second] = m.second;
                n_dif_asc -= 2;
            } else {
                b_diff = true; 
            }
        }
        // if there is no paired source and target, let's swap one
        if(b_diff){
            for(auto m : mp_target){
                if(m.first == m.second) continue;
                min_swaps ++;
                mp_target[m.first] = mp_target[m.second];
                mp_target[m.second] = m.second;
                n_dif_asc -= 1;
                break;
            }
        }
        cout << "2, " << n_dif_asc << ", " << min_swaps << ": ";
        for(auto m : mp_target){
                cout << m.first << " -> " << m.second << ", ";
        }
        cout << endl;
    }
    
    
    return min_swaps;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = lilysHomework(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
