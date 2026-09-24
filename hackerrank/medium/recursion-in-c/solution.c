#include <stdio.h>

int S(int n, int a, int b, int c) {
    if (n == 1) return a;
    if (n == 2) return b;
    if (n == 3) return c;
    return S(n-1, a, b, c) + S(n-2, a, b, c) + S(n-3, a, b, c);
}

int main() {
    int n, a, b, c;
    scanf("%d", &n);
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n", S(n, a, b, c));
    return 0;
}
