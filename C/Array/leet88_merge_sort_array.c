void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;        // nums1의 실제 값 마지막
    int j = n - 1;        // nums2의 마지막
    int k = m + n - 1;    // nums1 전체 마지막 위치

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k] = nums1[i];
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }

        k--;
    }
}