class Node:
    """
    This is Node class, which is automatically created using class Linked List.
    It contains Data and a "link" to next Node in order
    When initaized, it sets variables data and next, which acts like a pointer
    The Aviable Commands:
        None
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "The data: " + str(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data


class CircularLinkedList:
    def __init__(self):
        self.head = None


    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
            return
        
        last = self.head
        while last.next != self.head:
            last = last.next
        
        new_node = Node(data)

        last.next = new_node
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
            return
        
        new_node = Node(data)

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head


    def print_llist(self):
        curr = self.head

        while curr:
            print(curr.data, "-> ", end="")
            curr = curr.next
            if curr == self.head:
                print("(Head)", end="")
                break
        print()

    
    def remove(self, index):
        curr = self.head
        prev = self.head

        if index == 0:
            while prev.next != self.head:
                prev = prev.next
            curr = self.head
            
            prev.next = curr.next
            self.head = curr.next
            curr.next = None
            curr.data = None
            return

        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
            if curr == self.head:
                curr = None
                break
    
        if not curr:
            return print("There is not that much Nodes in this Circular Linked List. No changes have been made.")

        prev.next = curr.next
        curr.next = None
        curr.data = None
        curr = None
        return


    def split_list(self, index=None):
        if index == None:
            len_of_self = len(self)
            half = int(len_of_self / 2) - 1
        elif index:
            if len(self) - 1 == index:
                return print("No action was made. Try to instead delete last node.")
            half = index - 1

        curr = self.head

        while curr.next != self.head and half > 0:
            curr = curr.next
            half -= 1

        if curr == None:
            return

        new_head = curr.next
        new_last = curr

        new_cllist = CircularLinkedList()

        new_cllist.head = new_head

        prev = curr.next
        curr = curr.next.next

        while curr.next != self.head:
            prev.next = curr
            new_cllist.append(curr)
            curr = curr.next

        curr.next = new_cllist.head
        new_last.next = self.head

        self.print_llist()
        new_cllist.print_llist()


    def __len__(self):
        curr = self.head
        length = 1

        while curr.next != self.head:
            curr = curr.next
            length += 1

        return length        


if __name__ == "__main__":
    llist = CircularLinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.append("E")
    llist.append("F")

    llist.print_llist()