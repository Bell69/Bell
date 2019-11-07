#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def CompareEvent(self,subarray_left,subarray_right):
        # 宣告左idnex
        left_index = 0
        # 宣告右idnex(直接獲取長度)
        right_index = len(subarray_left)
        # 宣告輸出陣列
        output_list = subarray_left+subarray_right
        # 宣告陣列
        mBorder =len(subarray_left) + len(subarray_right)
        # 遞迴處理輸出陣列長度
        while mBorder>0:
            # 比較分類
            if left_index==right_index or right_index==mBorder:
                remain = output_list[:mBorder]
                output_list = output_list[mBorder:]
                output_list.extend(remain)
                mBorder=0
            elif output_list[left_index]<=output_list[right_index]:
                smaller = output_list[left_index]
                output_list = output_list[:left_index]+output_list[left_index+1:]
                output_list.append(smaller)
                mBorder= mBorder - 1
                right_index= right_index - 1
            else:
                smaller = output_list[right_index]
                output_list = output_list[:right_index]+output_list[right_index+1:]
                output_list.append(smaller)
                mBorder= mBorder - 1
        return output_list
    def merge_sort(self, mlist):
        listlength = len(mlist)
        if listlength > 1:
            # 對半處理
            half = len(mlist)//2
            left_subarray = mlist[:half]
            right_subarray = mlist[half:]
            # 準備左邊的陣列
            subarray_left = self.merge_sort(subarray_left)
            # 準備右邊的陣列
            right_subarray = self.merge_sort(right_subarray)
            # 左右陣列準備好進入比較事件
            return self.CompareEvent(subarray_left,right_subarray)
        else:
            return mlist

