/*
 * Complete the 'arrayManipulation' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

long arrayManipulation(int n, vector<vector<int>> queries) {
    vector<long> data(n+1, 0);
    for(auto qu : queries){
        data[qu[0]-1] += qu[2];
        data[qu[1]-1 + 1] += -qu[2];
    }
    long max_n = data[0];
    for(int i=1; i<n+1; i++){
        data[i] = data[i] + data[i-1];
        max_n = max(max_n, data[i]);
    }
    return max_n;
}
