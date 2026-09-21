#include <stdio.h>

void calculate_the_maximum(int n, int k) {
    int maxAnd = 0, maxOr = 0, maxXor = 0;

    for (int a = 1; a <= n; a++) {
        for (int b = a + 1; b <= n; b++) {
            int andVal = a & b;
            int orVal = a | b;
            int xorVal = a ^ b;

            if (andVal < k && andVal > maxAnd) maxAnd = andVal;
            if (orVal < k && orVal > maxOr) maxOr = orVal;
            if (xorVal < k && xorVal > maxXor) maxXor = xorVal;
        }
    }

    printf("%d\n%d\n%d\n", maxAnd, maxOr, maxXor);
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
    return 0;
}
