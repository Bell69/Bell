
# HW2 Merge Sort
## About Merge Sort:
Merge sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。<br>
![](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Sorting%20series/ComparisonSort_fig/MergeSort/f1.png?raw=true)
以圖一為例，要把數列{5,3,8,6,2,7,1,4}排序成{1,2,3,4,5,6,7,8}，Merge Sort的方法為：

* Divide：把數列「對半拆解」成兩個小數列。<br>
先把{5,3,8,6,2,7,1,4}分成{5,3,8,6}與{2,7,1,4}。<br>
再把{5,3,8,6}分解成{5,3}與{8,6}。<br>
{2,7,1,4}分解成{2,7}與{1,4}。<br>
依此類推，直到每個數列剩下一個元素。<br>
* Conquer：按照「由小到大」的順序，「合併」小數列。<br>
考慮數列{5}與{3}，比較大小後，合併成數列{3,5}。<br>
考慮數列{8}與{6}，比較大小後，合併成數列{6,8}。<br>
考慮數列{3,5}與{6,8}，比較大小後，合併成數列{3,5,6,8}。<br>
依此類推，最後，考慮數列{3,5,6,8}與{1,2,4,7}，比較大小後，合併成數列{1,2,3,4,5,6,7,8}。<br>
即完成Merge Sort。<br>
資料參考：[Comparison Sort](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html#ref)
 
