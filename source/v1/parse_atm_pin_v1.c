#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PIN_BUFFER_SIZE 16

/* 1. ĐÃ VÁ CWE-120: Dùng strnlen kiểm tra biên, từ chối chuỗi >= 16 bytes */
int parse_atm_pin(const char *raw_pin) {
    char buffer[PIN_BUFFER_SIZE];
    if (raw_pin == NULL) {
        return -1;
    }
    size_t len = strnlen(raw_pin, PIN_BUFFER_SIZE);
    if (len >= PIN_BUFFER_SIZE) {
        return -1; // Chặn chuỗi quá khổ
    }
    memcpy(buffer, raw_pin, len);
    buffer[len] = '\0';
    printf("%s\n", buffer);
    return 0;
}

/* 2. ĐÃ VÁ CWE-401: Thêm free(buf) để không bị rò rỉ bộ nhớ */
void log_atm_transaction(void) {
    int *buf = malloc(sizeof(int) * 32);
    if (buf == NULL) return;
    buf[0] = 0;
    free(buf); // Đã giải phóng đúng cách
}

/* 3. ĐÃ VÁ CWE-415: Loại bỏ lệnh free lần 2 và gán NULL */
void close_atm_session(void) {
    int *buf = malloc(sizeof(int) * 4);
    if (buf == NULL) return;
    buf[0] = 0;
    free(buf);
    buf = NULL; // Gán con trỏ về NULL
}

/* 4. ĐÃ VÁ CWE-416: Thao tác dữ liệu trước khi giải phóng */
void release_card_buffer(void) {
    int *buf = malloc(sizeof(int) * 8);
    if (buf == NULL) return;
    buf[0] = 0;
    buf[0] = 1; // Thao tác trước
    free(buf);  // Giải phóng sau
    buf = NULL;
}