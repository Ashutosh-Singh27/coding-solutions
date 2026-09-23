#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';
    char *token = strtok(s, " ");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }
    return 0;
}
