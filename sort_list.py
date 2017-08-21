class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():


    def __init__(self, head_node):
        self.head = head_node


    def add_nodes(self, head, val):
        newNode = ListNode(val)
        curr = head
        while(curr.next!=None):
            curr = curr.next
        curr.next = newNode

    def print_linkedList(self, head):
        curr = head
        while(curr.next!=None):
            print str(curr.val) + '->',
            curr = curr.next
        print curr.val,


class Solution(object):

    def sorted_list(self, head):

        if head is None or head.next is None:
            return head

        prev = None
        slow = head
        fast = head

        while(fast!=None and fast.next!=None):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        l1 = self.sorted_list(head)
        l2 = self.sorted_list(slow)

        return self.merge(l1, l2)

    def merge(self, head1, head2):
        mergedList = ListNode(0)
        curr = mergedList


        while(head1!=None and head2!=None):
            if head1.val < head2.val:
                newNode = ListNode(head1.val)
                curr.next = newNode
                head1 = head1.next

            else:
                newNode = ListNode(head1.val)
                curr.next = newNode
                head2 = head2.next

            curr = newNode
            
        if head1!=None:
            curr.next = head2
        if head2!=None:
            curr.next = head1

        return mergedList.next




def main():
    head = ListNode(1)
    linked_list_obj = LinkedList(head)

    linked_list_obj.add_nodes(head, 2)
    linked_list_obj.add_nodes(head, 9)
    linked_list_obj.add_nodes(head, 4)
    linked_list_obj.add_nodes(head, 5)
    linked_list_obj.print_linkedList(head)

    solutionObj = Solution()
    merged_list = solutionObj.sorted_list(head)
    print 'merge'
    linked_list_obj.print_linkedList(merged_list)


if __name__=='__main__':
    main()



