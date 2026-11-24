#include <iostream>
int main() {
    int a = 6, b = 3;
    int *p = &a;
    int &r = b;
    int c = *p * r;
    int d = a & b;
    std::cout << c << ' ' << d << std::endl;
    return 0;
}
