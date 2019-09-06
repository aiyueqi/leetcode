package com.ayq;

public class Main {
    void swap(int[] A, int a, int b){
        int tmp = A[a];
        A[a] = A[b];
        A[b] = tmp;
    }
    //从头尾中间三点中，选取中间值作为快排比较标准，并且放到末尾
    void moveMidToEnd(int[] A, int l, int r) {
        int mid = (l+r)/2;
        if(A[l]<A[mid] && A[mid]<A[r] || A[l]>A[mid] && A[mid]>A[r]) swap(A, mid, r);
        else if(A[mid]<A[l] && A[l]<A[r] || A[mid]>A[l] && A[l]>A[r]) swap(A, l, r);
    }

    int patition(int[] A, int l, int r) {
        moveMidToEnd(A, l, r);
        int pivot = A[r];
        //p指向下一个比piovt小的元素要插入的位置
        int p = l;
        //i指向当前扫描到的元素
        for(int i=l; i<r; i++){
            if(A[i]<pivot){
                if(i!=p) swap(A,i,p);
                p++;
            }
        }
        swap(A, p, r);
        return p;
    }

    void qSort(int[] A, int l, int r) {
        if(l>=r) return;
        //r选的位置还需要优化，不然会成n^2
        int index = patition(A, l, r);
        qSort(A, l, index-1);
        qSort(A, index+1, r);
    }

    void qSort2(int[] A,int l, int r) {
        if(l>=r) return;

        moveMidToEnd(A, l, r);
        int pivot = A[r];

        int i=l; int j=r;
        while(i<j) {
            while(i<j && A[i]<pivot) ++i;
            A[j] = A[i];
            while(i<j && A[j]>=pivot) --j;
            A[i] = A[j];
        }
        A[i] = pivot;
        qSort(A,l,i-1);
        qSort(A,i+1,r);
    }

    //归并排序
    private int[] tmp;
    void merge(int[] A, int l, int mid, int r){
        int i=l; int j=mid+1;
        int index;
        for(index=l; index<=r; index++) {
            if(j>r || i>mid) break;
            if(A[i]<=A[j]) tmp[index] = A[i++];
            else tmp[index] = A[j++];
        }
        //A[l,mid]中有剩余数据
        if(i>mid)
            while(index<=r) tmp[index++] = A[j++];
        else
            while(index<=r) tmp[index++] = A[i++];
        for(int k=l; k<=r; ++k) A[k] = tmp[k];
    }

    void merge_sort(int[] A, int l, int r){
        if(l>=r) return;
        int mid = (l+r)/2;
        merge_sort(A, l, mid);
        merge_sort(A, mid+1, r);

        merge(A, l, mid, r);
    }

    void mergeSort(int[] A, int l, int r) {
        tmp = new int[r-l+1];
        merge_sort(A, l, r);
    }

    public static void main(String[] args) {
	// write your code here
        int[] Array = {8,8};
        Main m = new Main();
        m.mergeSort(Array,0,Array.length-1);
        for (int i: Array) {
            System.out.print(i);
        }
    }
}
