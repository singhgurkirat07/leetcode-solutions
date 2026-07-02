class Solution {
public:
bool isPrime(int x) {
    if( x == 2 || x == 3 || x == 5 || x == 7 ||
           x == 11 || x == 13 || x == 17 || x == 19){return true;}return false;
}
    int countPrimeSetBits(int left, int right) {
        int cnt=0;
        for( int i=left;i<=right;i++){
            if(isPrime(__builtin_popcount(i))){cnt++;}
        }
        return cnt;
    }
};