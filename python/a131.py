class Solution:
    f = []
    def init(self):
        self.f = []
        self.f.append([[]])
        result = []

    def partition(self, s: str) -> List[List[str]]:
        self.init()
        l = len(s)
        #f(i) 表示下标[0, i-1] f(1)~f(n), 为方便补充定义f(0)=[]
        for t in range(1, l+1):
            global f
            self.f.append([])
            for i in range(0, t):
                if not self.pandlindrome(s[i:t]):
                    continue
                for j in self.f[i]:
                    tmp = j[:]
                    tmp.append(s[i:t])
                    self.f[t].append(tmp)
        return self.f[l]
    def pandlindrome(self, s):
        l = len(s)
        half = l//2
        for i in range(0, half):
            if s[i] != s[l-1-i]:
                return False
        return True