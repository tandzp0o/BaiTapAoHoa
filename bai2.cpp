#include <stdio.h>

int kiemTraSoChinhPhuong(int n) {
  int i = 1;
  while (i * i <= n) {
    if (i * i == n) {
      return 1;
    }
    i++;
  }
  return 0;
}

int demSoChinhPhuong(int n) {
  int count = 0;
  for (int i = 1; i <= n; i++) {
    if (kiemTraSoChinhPhuong(i)) {
      count++;
    }
  }
  return count;
}

int main() {
  int n;
  printf("Nhap so n: ");
  scanf("%d", &n);

  int soLuongSoChinhPhuong = demSoChinhPhuong(n);
  printf("So luong so chinh phuong nho hon %d la: %d\n", n, soLuongSoChinhPhuong);

  for (int i = 1; i <= n; i++) {
    if (kiemTraSoChinhPhuong(i)) {
      printf("%d ", i);
    }
  }

  return 0;
}
