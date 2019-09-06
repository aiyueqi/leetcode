class Solution {
    private ListNode head;
    private ListNode tail;
    //向tail结点后面添加结点node
    private ListNode addtail(ListNode node) {
        tail.next=node;
        tail=node;
        return node.next;
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        //初始化头尾标记
        if(l1==null && l2==null || l1!=null && l2==null) head = l1;
        else if(l1==null && l2!=null) head = l2;
        else head = (l1.val<=l2.val)? l1 : l2;
        tail = head;
        if(head==l1 && head!=null) l1=l1.next;
        if(head==l2 && head!=null) l2=l2.next;

        while(l1!=null && l2!=null)
            if(l1.val<=l2.val) l1=addtail(l1);
            else l2=addtail(l2);
        if(l1==null)
            while(l2!=null) l2=addtail(l2);
        if(l2==null) {
            while(l1!=null) l1=addtail(l1);
        }
        return head;
    }
}