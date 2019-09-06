/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // //反转后的头节点
        // ListNode reverseHead = null;
        // //下一个要加入新链表的节点
        // ListNode p = head;
        // while(p!=null) {
        //     ListNode tmp = p.next;
        //     p.next = reverseHead;
        //     reverseHead = p;
        //     p = tmp;
        // }
        // return reverseHead;

        //递归 定义reverseList：反转以head为头节点的链表，并返回反转后链表的头节点
        if(head==null) return null;
        if(head.next == null) return head;
        ListNode tmp = head.next;
        ListNode result = reverseList(tmp);
        tmp.next = head;
        head.next = null;
        return result;
    }
}