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