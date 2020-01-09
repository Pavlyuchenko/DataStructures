'''
Linked List Data Structure
'''

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

class LinkedList:
    """
    This is the Single Linked List Data Structure.
    It works like this: A -> B -> C -> Null, where A is the Head, Null is the End and each capital letter is representing each Node (type Node().__doc__() to learn more), which points to another Node
    You can initialize Linked List like this: llist = LinkedList()")
    The Aviable Commands:
        print_llist() - Prints every element in Linked List
        append(data) - Puts new Node to the end of Linked List
        prepend(data) - Puts new Node to the beginning of Linked List
        insert(data, index) - Inserts Node on specified index
        delete(index, data) - Deletes Node on specified index or containing specified data
        swap(index1, index2) - Swaps two nodes
        reverse_list() - 1 -> 2 -> 3 - > None  == 3 -> 2 -> 1 -> None
        merge(self, other) - makes one Linked List out of two - 1 -> 3 -> 5 + 2 -> 4 -> 6 == 1 -> 2 -> 3 -> 4 -> 5 -> 6
        sort() - sorts Linked List elements from lowest to highest 
        remove_duplicates() - removes duplicate data 
        get_node(index) - gets node on specified index
    """

    def __init__(self):
        self.head = None

    def print_llist(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data, "-> ", end="")
            curr_node = curr_node.next
        print("None")

    
    def get_llist(self):
        llist_array = []
        curr_node = self.head

        while curr_node:
            llist_array.append(curr_node.data)
            curr_node = curr_node.next
        return llist_array


    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)

        prev_node = self.head

        while prev_node.next and index != 1:
            prev_node = prev_node.next
            index -= 1
            if prev_node.next is None:
                print("llist.insert('", data ,"', ", index, ")")
                print("Error: The previous Node does not exist yet.")
                return
        next_node = prev_node.next

        new_node.next = next_node
        prev_node.next = new_node

    def delete(self, index=None, data=None):
        if index:
            if index == 0:
                self.head = self.head.next
                curr_node = self.head
                curr_node = None
                return

            prev_node = self.head
            while prev_node.next and index != 1:
                prev_node = prev_node.next
                index -= 1
                if prev_node.next is None:
                    print("Error: The Node does not exist yet, thus cannot be deleted.")
                    return

            curr_node = prev_node.next
            prev_node.next = prev_node.next.next

            curr_node = None
        else:
            curr_node = self.head
            prev_node = None
            
            while curr_node and curr_node.data != data:
                prev_node = curr_node
                curr_node = curr_node.next

            if curr_node == None:
                return

            if prev_node:
                prev_node.next = curr_node.next
            else:
                self.head = curr_node.next
            curr_node = None
            

    def swap(self, index_1, index_2):
        if index_1 == index_2:
            return

        if index_2 == 0:
            index_1, index_2 = index_2, index_1
        
        curr_node = self.head


        if index_1 == 0:
            base_index_2 = index_2
            while curr_node and index_2 >= 1:
                index_2 -= 1
                prev_node = curr_node
                curr_node = curr_node.next
            
            if curr_node == None:
                print("You cannot swap index 0 with", base_index_2,", because there is not index", base_index_2, "in this Stack.")
                return
            
            head_next = self.head.next
            
            prev_node.next = self.head
            self.head.next = curr_node.next
            if base_index_2 != 1:
                curr_node.next = head_next
            else:
                curr_node.next = self.head
            
            self.head = curr_node
        else:
            base_index_1 = index_1
            base_index_2 = index_2
            curr_node_1 = self.head
            curr_node_2 = self.head
            while curr_node_1 and index_1 >= 1:
                index_1 -= 1
                prev_node_1 = curr_node_1
                curr_node_1 = curr_node_1.next
            while curr_node_2 and index_2 >= 1:
                index_2 -= 1
                prev_node_2 = curr_node_2
                curr_node_2 = curr_node_2.next
            if curr_node_1 == None or curr_node_2 == None:
                print("You cannot swap indexes", base_index_1, "with", base_index_2, ", because one of them does not exist.")
                return 

            prev_node_1.next = curr_node_2
            prev_node_2.next = curr_node_1
            curr_node_1.next, curr_node_2.next = curr_node_2.next, curr_node_1.next

    
    def reverse_list(self):
        curr_node = self.head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    
    def __reversed__(self):
        curr_node = self.head
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


    def merge(self, other):
        if not isinstance(self, LinkedList) or not isinstance(other, LinkedList):
            print("One of your inserted variables is not instance of Linked List")
            return
            
        new_self = self.sort()
        new_other = other.sort()
        new_llist = LinkedList()
        
        curr_self = new_self.head
        curr_other = new_other.head
        prev = None

        while curr_self or curr_other:
            prev_next = prev

            if curr_other == None or curr_self.data < curr_other.data:
                new_node = Node(curr_self.data)
                new_llist.append(new_node.data)
                
                prev = curr_self
                curr_self = curr_self.next
            elif curr_self.data > curr_other.data:
                new_node = Node(curr_other.data)
                new_llist.append(curr_other.data)

                prev = curr_other
                curr_other = curr_other.next
            else:
                return new_llist

        return new_llist


    def sort(self):
        while True:
            l_sorted = True
            counter = 0
            curr = self.head
            prev = None
        
            while curr:
                if prev and curr:
                    if curr < prev:
                        self.swap(counter-1, counter)
                        l_sorted = False
                        counter -= 1
                prev = curr
                curr = curr.next
                counter += 1

            if l_sorted:
                break

        return self

    
    def remove_duplicates(self):
        duplicates = []

        curr = self.head

        while curr:
            if curr.data in duplicates:
                self.delete(data=curr.data)
            else:
                duplicates.append(curr.data)
            curr = curr.next


    def get_node(self, index):
        curr = self.head

        while index >= 0:
            try:
                data = curr.data
                curr = curr.next
                index -= 1
            except:
                return None
        return data


    def __getitem__(self, index):
        curr = self.head

        while index >= 0:
            try:
                data = curr.data
                curr = curr.next
                index -= 1
            except:
                return None
        return data


    def count_occurencies(self, search, curr="a"):
        if curr == "a":
            curr = self.head
        if not curr:
            return 0
        elif curr.data == search:
            return 1 + self.count_occurencies(search, curr.next)
        else:
            return self.count_occurencies(search, curr.next)


    def rotate(self, index):
        curr = self.head
        nxt = curr.next

        while nxt:
            curr = nxt
            nxt = curr.next
            if index == 1:
                new_last = curr
            index -= 1

        if index > 0:
            return print("There is not that much Nodes in this Linked List. \nRotate() did not make any changes")

        curr.next = self.head
        self.head = new_last.next
        new_last.next = None


    def __len__(self):
        curr_node = self.head
        counter = 0

        while curr_node:
            counter += 1
            curr_node = curr_node.next
        return counter

    
    def __eq__(self, other):
        curr_self = self.head
        curr_other = other.head
        try:
            while curr_self or curr_other:
                if not curr_self.data == curr_other.data:
                    print(curr_self.data.data == curr_other.data.data)
                    return False
                curr_self = curr_self.next
                curr_other = curr_other.next
        except:
            return False

        return True


    def __add__(self, other):
        self_new = LinkedList()
        self.copy_list(self_new)

        other_new = LinkedList()
        other.copy_list(other_new)

        while len(self_new) < len(other_new):
            self_new.append(0)
        while len(self_new) > len(other_new):
            other_new.append(0)

        self_new.print_llist()
        other_new.print_llist()

        curr_other = other_new.head
        curr_self = self_new.head
        new_list = LinkedList()

        leftover = 0
        while curr_self and curr_other:
            result = curr_self.data + curr_other.data
            if new_list.head == None:
                if result >= 10:
                    result -= 10
                    new_node = Node(result + leftover)
                    leftover = 1
                else:
                    new_node = Node(result + leftover)
                    leftover = 0

                new_list.head = new_node
                prev = new_node
                curr_self = curr_self.next
                curr_other = curr_other.next
            else:
                if result >= 10:
                    result -= 10
                    new_node = Node(result + leftover)
                    leftover = 1
                else:
                    new_node = Node(result + leftover)
                    leftover = 0
                prev.next = new_node
                prev = new_node
                curr_self = curr_self.next
                curr_other = curr_other.next
        if leftover == 1:
            new_list.append(1)
        new_list.reverse_list()
        return new_list


    def copy_list(self, other):
        curr = self.head
        other_prev = None
        
        while curr:
            new_node = Node(curr.data)
            if curr == self.head:
                other.head = new_node
            else:
                other_prev.next = new_node
            other_prev = new_node
            curr = curr.next

    
    def is_palindrome(self):
        length = len(self)

        if length % 2 == 0:
            return
        
        curr = self.head
        length = int(length) / 2
        first_half = LinkedList()
        second_half = LinkedList()

        while length >= 1:
            first_half.append(curr.data)
            curr = curr.next
            length -= 1

        curr = curr.next
        while curr:
            second_half.append(curr.data)
            curr = curr.next

        second_half.reverse_list()

        if first_half == second_half:
            return True
        else:
            return False


    def __setitem__(self, index, data):
        curr = self.head

        while index >= 0:
            try:
                prev = curr
                curr = curr.next
                index -= 1
            except:
                return None
        prev.data = data


if __name__ == "__main__":
    '''llist = LinkedList()
    llist.append(5)
    llist.append(10)
    llist.append(12)
    llist.append(13)
    llist.print_llist()
    
    print("Lenght is: ", len(llist))
    print()

    llist.prepend("D")
    llist.insert("E", 2)
    llist.print_llist()
    print("Lenght is: ", len(llist))
    print()
    llist.delete(data="A")
    llist.print_llist()
    print("Lenght is: ", len(llist))
    print(LinkedList.__doc__)
    llist.swap(1, 1)
    llist.reverse_list()
    llist2 = LinkedList()
    llist2.append(11)
    llist2.append(7)
    llist2.append(8)
    llist2.append(6)
    llist2.print_llist()
    new_llist = LinkedList.merge(llist, llist2)
    print("Merged:", new_llist.get_llist())
    
    llist3 = LinkedList()
    llist3.append(1)
    llist3.append(4)
    llist3.append(25)
    llist3.append(0)
    llist3.sort()
    llist3.print_llist()


    llist4 = LinkedList()
    llist4.append("r")
    llist4.append("a")
    llist4.append("c")
    llist4.append("e")
    llist4.append("c")
    llist4.append("a")
    llist4.append("s")
    print(llist4.is_palindrome())
    llist4.rotate(5)
    llist4.print_llist()
  
    llist_add = LinkedList()

    llist_add.append(0)
    llist_add.append(5)

    llist_add_2 = LinkedList()

    llist_add_2.append(5)
    llist_add_2.append(7)

    added = llist_add + llist_add_2
    added.print_llist()'''


    llist = LinkedList()
    llist.append(5)
    llist.append(10)
    llist.append(12)
    llist.append(13)
    llist.print_llist()
    llist[0] = 1
    llist.print_llist()
    reversed(llist)
    llist.print_llist()
    print(llist[0])