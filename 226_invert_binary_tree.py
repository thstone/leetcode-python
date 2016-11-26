# coding : UTF-8

'''
226 Invert Binary Tree

example:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self,root):
        '''
        :param root:
        :return:
        '''
        if root == None:
            return root

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

            temp = node.right
            node.right = node.left
            node.left = temp

        return root

if __name__ == '__main__':
    solution = Solution()
