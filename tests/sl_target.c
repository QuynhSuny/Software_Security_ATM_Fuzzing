#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* sinh từ đặc tả 'atm_fuzzing_verification', hàm 'parse_atm_pin', kind='buffer_copy' */
void parse_atm_pin(const char *raw_pin) {
    char buffer[16];
    strcpy(buffer, raw_pin);   /* sinh từ đặc tả: buffer-overflow */
    printf("%s\n", buffer);
}
