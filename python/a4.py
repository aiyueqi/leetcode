from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        len_total = len_nums1 + len_nums2

        #[ml, mr),[nl, nr)
        def f_odd(index, m, n):
            #边界
            m_len = len(m)
            n_len = len(n)
            if m_len == 0:
                return n[index]
            if n_len == 0:
                return m[index]

            m_mid = m_len//2
            n_mid = n_len//2

            if m[m_mid] == n[n_mid]:
                tmp_left = m_mid+n_mid
                if index == tmp_left+1 or tmp_left+2:
                    return m[m_mid]
                if index <= tmp_left:
                    return f_odd(index, m[0:m_mid], n[0:n_mid])
                return f_odd(index, m[m_mid+1:], n[n_mid+1:])

            if m[m_mid] < n[n_mid]:
                if index <= m_mid:
                    return f_odd(index, m[0:m_mid+1], n[0:n_mid])
                if index > m_len+n_mid:
                    return f_odd(index-m_mid-1-n_mid, m[m_mid+1:], n[n_mid:])
                return f_odd(index-m_mid-1, m[m_mid+1:], n[0:n_mid])
            
            #如果m[m_mid] > n[n_mid], 交换m_mid和n_mid，走上一条分支逻辑
            return f_odd(index, n, m)

        if (len_total)%2 != 0:
            f_odd((len_total)//2, nums1, nums2)
s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))


