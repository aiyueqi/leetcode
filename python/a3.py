class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = len(s)
        result = 0
        d = {}
        if length>0:
            d[s[0]] = 0
        for r in range(1, length):
            #print("l=",l,"r=",r)
            result = max(result, r-l)
            if s[r] in d:
                old_l = l
                l = d[s[r]]+1
                #这里可以优化
                for tmp in range(old_l, l):
                    d.pop(s[tmp])
            d[s[r]] = r
        
        #print("result=",result, "l",l)
        return max(result, length-l)

            
#优化后的解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        dicts={}
        start=0
        max_len=0
        for i in range(n):
            if s[i]in dicts:
                temp_len=i-start
                if temp_len>max_len:
                    max_len=temp_len
                temp_start=dicts[s[i]]+1
                if start<temp_start:
                    start=temp_start
                
            dicts[s[i]]=i
            # temp_len=i+1-start
            # if temp_len>max_len:
            #     max_len=temp_len
        return max(max_len,n-start)
