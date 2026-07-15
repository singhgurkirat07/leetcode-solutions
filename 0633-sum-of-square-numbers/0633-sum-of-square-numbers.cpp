class Solution {
public:
    bool judgeSquareSum(int c) {
        long long left=0,right=sqrt(c);
        while(left<=right){
           if(left*left + right*right ==c){return true;}
           if(left*left + right*right > c){right--;}
           if(left*left + right*right < c){left++;}
        }
        return false;
    }
};