
double area(triangle t) {
    double p = (t.a + t.b + t.c) / 2.0;
    return sqrt(p * (p - t.a) * (p - t.b) * (p - t.c));
}

void sort_by_area(triangle* tr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (area(tr[j]) > area(tr[j + 1])) {
                triangle temp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp;
            }
        }
    }
}
