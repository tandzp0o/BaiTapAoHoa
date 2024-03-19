#include <stdio.h>

int main() {
    // Duyệt qua các số từ 10 đến 99
    for (int i = 10; i <= 99; i++) {
        // Kiểm tra xem số đó có chia hết cho 7 hay không
        if (i % 7 == 0) {
            // In số đó ra màn hình
            printf("%d ", i);
        }
    }

    return 0;
}
