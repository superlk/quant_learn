class Solution:
    def reverseList(self, head):
        if not head: return
        pre = None
        while head.next:
            print("head.next1", head.next)
            nex = head.next
            head.next = pre
            print("head.next2", head.next)
            pre = head
            print("pre", pre)
            head = nex
            print("head", head)
        head.next = pre
        print("head.next3", head.next)
        return head


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    s = Solution()
    s.reverseList(enumerate(head))
    print(head)
