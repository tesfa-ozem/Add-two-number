class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.val = None

    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while current is not None:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    # def push(self, new_data: 0, next=None):
    #     new_node = ListNode(new_data, next)
    #     new_node.next = self.head
    #     self.head = new_node
    #     # Utility function to print the LinkedList

    # def printList(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.val, end=" ")
    #         temp = temp.next

    # def list_value(self) -> int:
    #     temp = self.head
    #     value = ''
    #     while temp:
    #         value = value + str(temp.val)
    #         temp = temp.next
    #     return int(value)


class Solution:
    def addTwoNumbers(self, l1, l2):
        # create a list
        # next_node = l1.next
        current_l1, current_l2 = l1, l2
        value_l1 = []
        value_l2 = []

        while current_l1 is not None:
            next_node = current_l1.next
            value_l1.append(current_l1.val)
            current_l1 = next_node

        while current_l2 is not None:
            next_node = current_l2.next
            value_l2.append(current_l2.val)
            current_l2 = next_node

        l1_value = int("".join(map(str, value_l1)))
        l2_value = int("".join(map(str, value_l2)))

        sum_list = list(str(l1_value + l2_value))

        head = ListNode(val=sum_list[0])
        temp = head

        for i in range(2, len(sum_list)):
            n = ListNode(val=i)
            temp.next = n
            temp = n

        return head


l1 = ListNode(val=3)
l2 = ListNode(val=2)
l3 = ListNode(val=6)

l1.next = l2
l2.next = l3

v1 = ListNode(val=3)
v2 = ListNode(val=2)
v3 = ListNode(val=6)

v1.next = l2
v2.next = l3


sl = Solution()
print(sl.addTwoNumbers(l1, v1))
# l1.push(4)
# l1.push(3)

# l2 = LinkedList()
# l2.push(5)
# l2.push(6)
# l2.push(4)
# sl = Solution()
# print(sl.addTwoNumbers(l1, l2))
