class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        class Node:
            def __init__(self):
                self.leftCh = None
                self.rightCh = None
                self.prefix = 0
                self.suffix = 0
                self.maximum = 0
                self.length = 0

        tree = [Node() for _ in range(4 * n)]

        def merge(left, right):
            parent = Node()

            parent.leftCh = left.leftCh
            parent.rightCh = right.rightCh
            parent.length = left.length + right.length

            parent.prefix = left.prefix
            parent.suffix = right.suffix

            parent.maximum = max(left.maximum, right.maximum)

            if left.rightCh == right.leftCh:
                parent.maximum = max(
                    parent.maximum,
                    left.suffix + right.prefix
                )

                if left.prefix == left.length:
                    parent.prefix = left.length + right.prefix

                if right.suffix == right.length:
                    parent.suffix = right.length + left.suffix

            return parent

        def build(node, left, right):

            if left == right:
                tree[node].leftCh = s[left]
                tree[node].rightCh = s[left]
                tree[node].prefix = 1
                tree[node].suffix = 1
                tree[node].maximum = 1
                tree[node].length = 1
                return

            mid = left + (right - left) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):

    
            if left == right:
                tree[node].leftCh = char
                tree[node].rightCh = char
                tree[node].prefix = 1
                tree[node].suffix = 1
                tree[node].maximum = 1
                tree[node].length = 1
                return

            mid = left + (right - left) // 2

    
            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

    
            tree[node] = merge(tree[node * 2],tree[node * 2 + 1])
        
        build(1,0,n-1)

        ans=[]

        for i in range(len(queryIndices)):
            update(1,0,n-1,queryIndices[i],queryCharacters[i])
            ans.append(tree[1].maximum)
        return ans