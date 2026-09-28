
int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    va_end(args);
    return total;
}

int min(int count, ...) {
    va_list args;
    va_start(args, count);
    int result = va_arg(args, int);
    for (int i = 1; i < count; i++) {
        int value = va_arg(args, int);
        if (value < result) {
            result = value;
        }
    }
    va_end(args);
    return result;
}

int max(int count, ...) {
    va_list args;
    va_start(args, count);
    int result = va_arg(args, int);
    for (int i = 1; i < count; i++) {
        int value = va_arg(args, int);
        if (value > result) {
            result = value;
        }
    }
    va_end(args);
    return result;
}
