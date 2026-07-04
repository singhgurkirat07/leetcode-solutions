class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int max_words=0;
        for(auto sentence:sentences){
            int words=0;
            for( int i=0;i<sentence.length();i++){
                if(sentence[i]==' '){words++;}
                
            }
                max_words=max(max_words,words+1);
        }
        return max_words;
    }
};