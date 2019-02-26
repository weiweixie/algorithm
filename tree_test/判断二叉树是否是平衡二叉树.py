# -*- coding: utf-8 -*-
'''
Created on 2019/2/26 22:03
file : 判断二叉树是否是平衡二叉树.py

@author: xieweiwei
'''

class Solution:
    def __int__(self):
        self.tree = None

    # 判断二叉树是否为平衡二叉树
    # 先判断该节点是否平衡
    # 再递归去判断左节点和右节点是否平衡

    # 递归求当前节点的深度
    def getdepth(self,node):
        if not node:
            return 0
        ld = self.getdepth(node.left)
        rd = self.getdepth(node.right)
        return max(ld, rd) + 1

    def isB(self,head):
        if not head:
            return True
        ld = self.getdepth(head.left)
        rd = self.getdepth(head.right)
        if abs(ld - rd) > 1:
            return False
        return self.isB(head.left) and self.isB(head.right)


