# [28实现strStr()][title]
## 题目描述
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
## 思路
使用经典的KMP算法，维护一个next数组，时间复杂度O(n+m)，具体KMP算法分析知乎上面有很清晰的讲解：[点击这里](https://www.zhihu.com/question/21923021/answer/281346746)
## 代码实现
```java
class Solution {
    private int[] next;
    private void initNext(String s) {
        next = new int[s.length()];
        next[0] = -1;
        int i=-1; int j=1;
        while(j<s.length()){
            if(i==-1 || s.charAt(j-1)==s.charAt(i)) next[j++] = ++i;
            else{
                i=next[i];
            }
        }
    }
    public int strStr(String haystack, String needle) {
        if(needle.length()==0) return 0;
        initNext(needle);
        int result = -1;
        int i=0; int j=0;
        while(j<needle.length() && i<haystack.length()){
            if(j==-1 || haystack.charAt(i)==needle.charAt(j)){
                i++; j++;
            }else {
                j=next[j];
            }
        }
        if(j==needle.length()) result = i-j;
        return result;
    }
}
```
[title]:https://leetcode-cn.com/problems/implement-strstr/
