//判断一个单链表是否为回文链表
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {        
        ListNode fast = head;
        ListNode slow = head;
        
        //假设链表长度为n，下标0-n-1 ，则下标fast = 2*slow
        //n为偶数时，边界为下标 fast = n, slow = n/2
        //n为奇数时，边界为下标 fast = n+1, slow = (n+1)/2
        //无论奇偶，slow的位置可作为检测回文数的起点
        while(fast!=null) {
            slow = slow.next;
            fast = fast.next;
            if(fast != null) fast = fast.next;
        }
        ListNode reverseHead = reverse(slow);
        while(reverseHead != null) {
            if(reverseHead.val != head.val) return false;
            reverseHead = reverseHead.next;
            head = head.next;
        }
        return true;
    }
    private ListNode reverse(ListNode head) {
        //反转之后链表的头节点
        ListNode reverseHead = null;
        //下一个要插入的节点
        ListNode p = head;
        while(p!=null){
            ListNode tmp = p.next;
            p.next = reverseHead;
            reverseHead = p;
            p = tmp;
        }
        return reverseHead;
    }
}
