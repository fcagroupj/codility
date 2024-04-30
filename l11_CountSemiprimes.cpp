/*
[66%]
https://app.codility.com/demo/results/trainingPC28JU-KA6/
*/
vector<bool> getSeive(int N){
    vector<bool> seive(N+1, true);
    seive[0] = false;
    seive[1] = false;
    if(N <= 1){
        return seive;
    }
    int i = 2;
    while(i*i <= N){
        if(seive[i]){
            int j = i*i;
            while(j <= N){
                seive[j] = false;
                j += i;
            }
        }
        i ++;
    }
    return seive;
}
vector<int> getPrimes(int N){
    vector<int> primes;
    int i=2;
    while(i*i < N){
        if(N % i == 0) primes.push_back(i);
        i += 1;
    }
    if(i * i == N) primes.push_back(i);
    return primes;   
}
vector<int> solution(int N, vector<int> &P, vector<int> &Q) {
    // Implement your solution here
    vector<bool> seives = getSeive(N);
    vector<int> ans;
    int M = P.size();
    for(int i=0; i<M; i++){
        int count = 0;
        for(int j=P[i]; j<Q[i]+1; j++){
            auto ps = getPrimes(j);
            for(auto p : ps){
                if( seives[p] && seives[int(j/p)] ) {
                    count ++;
                    break;
                }
            }
        }
        ans.push_back(count);
    }
    return ans;
}
