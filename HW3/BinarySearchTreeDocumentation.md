
# Binary Search Tree
## About BST:
二叉查詢樹（binary search tree），顧名思義二叉查詢樹中每個節點至多有兩個子節點，並且還對儲存於每個節點中的關鍵字值有個小小的要求，<br>
即只要這個節點有左節點或右節點，那麼其關鍵字值總的大於其左節點的關鍵字值，小於其右節點的關鍵字值，如下圖：<br>
![](https://img-blog.csdn.net/20140711211402185?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaGpqNDE0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
## Binary Search Tree的特徵
有了加裝Dictionary後的TreeNode，便能夠說明BST的特徵。<br>
任何CurrnetNode之Key若與其left child、right child之Key有以下關係(若pointer指向NULL則忽略)：Key(L)<Key(Current)<Key(R)，則可稱這棵樹為Binary Search Tree(BST)。
