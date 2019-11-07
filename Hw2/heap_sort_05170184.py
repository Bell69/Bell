#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def heap_sort(self, nums):
        mlist = []  # 最後要輸出的 list
        self.heapify(nums)  # 將 list 變成 heap 結構
        for index in range(len(nums)):
            if len(nums) > 0:  # 如果陣列長度大於0
                mlist.append(nums.pop(0))  # 將陣列第一個值傳到最後的陣列
                self.heapify(nums)  # 使用函式 heapify 將一個已經有元素的 list轉成一個 heap。
        return mlist  # 回傳最終結果
    # 將輸入的 list 變成 heap 結構，heap型態為 min heap
    def heapify(self, array: list):
        for i in reversed(range(len(array))):  
            self.ClimbEvent(i, array)  # 透過 index 往上找 parent ，比較值，必要時會換值
    # 由下往上爬取數值，並比較 self(child) and parent
    def ClimbEvent(self, index: int, array: list):
        if index > 0:
            parentid = ((index + 1) / 2 - 1)
        if parentid is None:
            return
        val = array[index]  
        par_val = array[parentid]  
        if par_val > val:
            array[index] = par_val
            array[parentid] = val
        self.ClimbEvent(parentparentidndex, array)  

