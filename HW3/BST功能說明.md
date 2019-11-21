
# BST:InsertBST(新增資料)
# insert(key)——將關鍵字值為key的節點插入到適當的位置
函式InsertBST()的概念，可以視為Search()的延伸：<br>
根據BST對Key之規則，先找到將要新增之node「適合的位置」；再將欲新增的node接上BST。<br>

# BST:DeleteBST(刪除資料)
# delete(key)——將關鍵字值為key的節點從樹中刪掉
要在BST上執行刪除資料(被刪除的node稱為A)，必須讓刪除A後的BST仍然維持BST的性質。因此，所有「具有指向A的pointer」之node(也就是A的parent、leftchild以及rightchild)都必須調整該pointer，使其指向新的記憶體位置。<br>
刪除資料的工作，根據欲刪除之node「有幾個child pointer」分成三類：<br>
Case1：欲刪除之node沒有child pointer；
Case2：欲刪除之node只有一個child pointer(不論是leftchild或rightchild)；
Case3：欲刪除之node有兩個child pointer。

# BST:Search(搜尋)
BST的Search()操作，便是根據BST的特徵：Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。<br>
搜尋結果可能成功，可能失敗。<br>




