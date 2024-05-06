/*
https://app.codility.com/demo/results/trainingY8EQKJ-EPE/
[61%]
https://app.codility.com/demo/results/training5Z69PD-GFQ/

*/
// cout << "this is a debug message" << endl;
int getGcd(int a, int b){
    if(a % b == 0) return b;
    return getGcd(b, a % b);
}
int isPrime(int a){
    
    int i = 2;
    while(i * i <= a){
        if(a % i == 0) return false;
        i ++;
    }
    return true;
}
vector<int> getDivs(int a){
    vector<int> divs;
    if(a != 1) divs.push_back(a);
    int i=2;
    while(i * i < a){
        if(a % i == 0) {
            divs.push_back(i);
            divs.push_back(int(a / i));
        }
        i ++;
    }
    if(i * i == a) divs.push_back(i);
    return divs;
}
int solution(vector<int> &A, vector<int> &B) {
    // Implement your solution here
    int N = A.size();
    int n_same_prime = 0;
    for(int i=0; i<N; i++){
        bool hasSamePrime = true;
        
        int g = getGcd(A[i], B[i]);
        //cout << "1. " << g << ", " << endl;
        vector<int> g_primes = getDivs(g);
        {
            A[i] = int(A[i] / g);
            
            vector<int> g_primes1 = getDivs(A[i]);
            for(auto g_p : g_primes1){
                //cout << "2. " << g_p << ", " << endl;
                if(isPrime(g_p) ){
                    auto it = find(g_primes.begin(), g_primes.end(), g_p);
                    if(it == g_primes.end()){
                        hasSamePrime = false;
                        break;
                    }
                }
            }
            B[i] = int(B[i] / g);
            vector<int> g_primes2 = getDivs(B[i]);
            for(auto g_p : g_primes2){
                //cout << "3. " << g_p << ", " << endl;
                if(isPrime(g_p) ){
                    auto it = find(g_primes.begin(), g_primes.end(), g_p);
                    if(it == g_primes.end()){
                        hasSamePrime = false;
                        break;
                    }
                }
            }
        } 
        
        if(hasSamePrime) n_same_prime ++;
    }
    return n_same_prime;
}
