# -*- coding: utf-8 -*-

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        返回一个链表的中间数
        :param head: 指向第一节点的头结点
        :return:
        """
        fast = head  # 快指针
        slow = head  # 慢指针
        while (fast != None and fast.next != None):
            fast = fast.next.next  # 快指针每次走两步
            slow = slow.next  # 慢指针每次走一步
        return slow

