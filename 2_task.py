from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = self._get_value_node_list(l1)
        value2 = self._get_value_node_list(l2)
        result = list(str(value1 + value2))[::-1]
        head = self.create_node_list(result)
        self.print_node_list(head)
        return head

    def _get_value_node_list(self, node_list: ListNode) -> int:
        sum_value = ""
        while True:
            sum_value += str(node_list.val)
            node_list = node_list.next
            if node_list is None:
                break
        return int(sum_value[::-1])

    @classmethod
    def create_node_list(cls, list_: list):
        node_list = None
        head = None

        while list_:
            if node_list is None:
                node_list = ListNode(list_.pop(0))
                head = node_list

            if not list_:
                break
            node_list.next = ListNode(list_.pop(0))
            node_list = node_list.next

        return head

    @classmethod
    def print_node_list(cls, node_list: ListNode) -> None:
        while True:
            print(node_list.val)
            node_list = node_list.next
            if node_list is None:
                break


if __name__ == '__main__':
    l1_ = Solution.create_node_list([9, 9, 9, 9, 9, 9, 9])
    l2_ = Solution.create_node_list([9, 9, 9, 9])
    solution = Solution()
    solution.addTwoNumbers(l1_, l2_)


"""
Don't look if you have not solved the problem yet

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
"""
