#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'highestValuePalindrome' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER n
 *  3. INTEGER k
 */

string highestValuePalindrome(string s, int n, int k) {
    int n_unmatched = 0;
    vector<int> unmatched(n, 0);
    for(int i=0; i<(int(n/2)); i++){
        if(s[i] != s[n - 1 - i]){
            n_unmatched ++;
            
            if(s[i] > s[n - 1 - i]){
                s[n - 1 - i] = s[i];
                
            } else {
                s[i] = s[n - 1 - i];
            }
            unmatched[i] = s[i];
        } 
    }
    cout << "1: " << s << ", " <<
        n_unmatched << ", " <<
        endl;
    if(n_unmatched > k) return "-1";
    int n_left_changes = k - n_unmatched;
    for(int i=0; i<n; i++){
        if(s[i] == '9') continue;
        if(unmatched[i] <= 0 ){
            if(n_left_changes >= 2){
                s[i] = '9';
                s[n - 1 -i] = '9';
                n_left_changes -= 2;
            }
        } else {
            if(n_left_changes >= 1){
                s[i] = '9';
                s[n - 1 -i] = '9';
                n_left_changes -= 1;
            }
        }
        if(n_left_changes < 1) break;
    }    
    if(n_left_changes > 0 && (n%2 == 1)){
        s[int(n/2)] = '9';
    }
    cout << "2: " << s << ", " <<
        n_left_changes << ", " <<
        endl;
    return s;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int k = stoi(first_multiple_input[1]);

    string s;
    getline(cin, s);

    string result = highestValuePalindrome(s, n, k);

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
