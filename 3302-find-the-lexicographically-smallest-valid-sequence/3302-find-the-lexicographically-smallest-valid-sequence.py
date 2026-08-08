class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        suf=[0]*(len(word1)+1)
        j=len(word2)-1
        cnt=0

        for i in range(len(word1)-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                cnt+=1
                j-=1
            suf[i]=cnt
        
        ans=[]
        cnt=0
        j=0
        mismatch=0

        for i in range(len(word1)):
            if j==len(word2):
                break
            if word1[i]==word2[j]:
                ans.append(i)
                j+=1
                continue
            else:
                rem_letter=len(word2)-j-1
                possible_suf=suf[i+1]

                if mismatch==0 and rem_letter<=possible_suf:
                    ans.append(i)
                    j+=1
                    mismatch=1
                    continue
                else:
                    continue
        return ans if len(ans)==len(word2) else []