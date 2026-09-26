#include <stdio.h>
#include <string.h>

int main() {
    char num[1001];
    scanf("%s", num);

    int freq[10] = {0};
    int len = strlen(num);

    for (int i = 0; i < len; i++) {
        if (num[i] >= '0' && num[i] <= '9') {
            freq[num[i] - '0']++;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", freq[i]);
    }
    printf("\n");

    return 0;
}
