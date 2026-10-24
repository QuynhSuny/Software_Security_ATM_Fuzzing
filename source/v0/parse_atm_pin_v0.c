#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Sinh từ đặc tả 'atm_fuzzing_verification', hàm 'parse_atm_pin', kind='buffer_copy' */
void parse_atm_pin(const char *raw_pin) {
    char buffer[16];
    strcpy(buffer, raw_pin);   /* Lỗ hổng CWE-120: Stack Buffer Overflow */
    printf("%s\n", buffer);
}

/* Sinh từ đặc tả 'atm_fuzzing_verification', hàm 'log_atm_transaction', kind='alloc_release' */
void log_atm_transaction(void) {
    int *buf = malloc(sizeof(int) * 32);
    buf[0] = 0;
    /* Lỗ hổng CWE-401: Memory Leak (thiếu free) */
}

/* Sinh từ đặc tả 'atm_fuzzing_verification', hàm 'close_atm_session', kind='alloc_release' */
void close_atm_session(void) {
    int *buf = malloc(sizeof(int) * 4);
    buf[0] = 0;
    free(buf);
    free(buf);   /* Lỗ hổng CWE-415: Double Free */
}

/* Sinh từ đặc tả 'atm_fuzzing_verification', hàm 'release_card_buffer', kind='alloc_release' */
void release_card_buffer(void) {
    int *buf = malloc(sizeof(int) * 8);
    buf[0] = 0;
    free(buf);
    buf[0] = 1;   /* Lỗ hổng CWE-416: Use-After-Free */
}