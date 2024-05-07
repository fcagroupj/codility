/*
https://app.codility.com/demo/results/trainingBGH3P9-AJ7/
[100%]
*/
long long merge(std::vector<int>& A, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1);
    std::vector<int> R(n2);

    for (int i = 0; i < n1; ++i)
        L[i] = A[left + i];
    for (int j = 0; j < n2; ++j)
        R[j] = A[mid + 1 + j];

    long long inversions = 0;

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            A[k++] = L[i++];
        } else {
            A[k++] = R[j++];
            inversions += n1 - i;
        }
    }

    while (i < n1)
        A[k++] = L[i++];

    while (j < n2)
        A[k++] = R[j++];

    return inversions;
}

long long mergeSort(std::vector<int>& A, int left, int right) {
    long long inversions = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        inversions += mergeSort(A, left, mid);
        inversions += mergeSort(A, mid + 1, right);
        inversions += merge(A, left, mid, right);
    }
    return inversions;
}
int solution(vector<int> &A) {
    // Implement your solution here
    long long inversions = mergeSort(A, 0, A.size() - 1);
    if (inversions > 1000000000)
        return -1;
    return inversions;
}
