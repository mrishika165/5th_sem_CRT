'''
206-reverse linked list
'''
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # temp = head 
        # prev = None 
        # while temp is not None:
        #     next_node = temp.next 
        #     temp.next = prev 
        #     prev = temp 
        #     temp = next_node 
        # return prev
        if head is None or head.next is None:
            return head 
        new_head = self.reverseList(head.next)
        head.next.next = head 
        head.next = None 
        return new_head    

'''
141-linked list cycle
'''

'''
19
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # dummy = ListNode(0)
        # dummy.next = head
        # slow = dummy
        # fast = dummy
        # for i in range(n):
        #     fast = fast.next 
        # while fast.next:
        #     fast = fast.next 
        #     slow = slow.next 
        # slow.next = slow.next.next
        # return dummy.next

        length = 0 
        temp = head 
        while temp:
            length += 1 
            temp = temp.next 
        dummy = ListNode(0)
        dummy.next = head 
        temp = dummy
        for i in range(length-n):
            temp = temp.next 
        temp.next = temp.next.next 
        return dummy.next
