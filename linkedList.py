class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = None


class LinkedList():


    def __init__(self, head_node):
        self.head = head_node


    def add_nodes(self, head, val):
        newNode = Node(val)
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

        
    def reverse_linkedList(self, head):
        if head is None:
            return None

        prev = None
        curr = head

        while(curr!=None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev




def main():
    head = Node(1)
    linked_list_obj = LinkedList(head)

    linked_list_obj.add_nodes(head, 2)
    linked_list_obj.add_nodes(head, 3)
    linked_list_obj.add_nodes(head, 4)
    linked_list_obj.add_nodes(head, 5)
    linked_list_obj.print_linkedList(head)
    print '\n'
    rev_head = linked_list_obj.reverse_linkedList(head)
    linked_list_obj.print_linkedList(rev_head)




if __name__ == '__main__':
    main()