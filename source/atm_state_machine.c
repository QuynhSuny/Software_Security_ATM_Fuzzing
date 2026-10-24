#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/* 5 trạng thái xác thực ATM */
typedef enum {
    STATE_IDLE,
    STATE_PIN_FAILED_1,
    STATE_PIN_FAILED_2,
    STATE_AUTHENTICATED,
    STATE_LOCKED
} ATMState;

typedef struct {
    ATMState state;
    int failed_attempts;
    char correct_pin[5];
} ATMSession;

void atm_init(ATMSession *session) {
    session->state = STATE_IDLE;
    session->failed_attempts = 0;
    strncpy(session->correct_pin, "1234", sizeof(session->correct_pin) - 1);
    session->correct_pin[4] = '\0';
}

bool atm_verify_pin(ATMSession *session, const char *entered_pin) {
    /* Đã bị khóa thì tuyệt đối không cho phép xác thực tiếp */
    if (session->state == STATE_LOCKED) {
        return false;
    }

    if (strcmp(entered_pin, session->correct_pin) == 0) {
        session->state = STATE_AUTHENTICATED;
        session->failed_attempts = 0;
        return true;
    } else {
        session->failed_attempts++;
        if (session->failed_attempts == 1) {
            session->state = STATE_PIN_FAILED_1;
        } else if (session->failed_attempts == 2) {
            session->state = STATE_PIN_FAILED_2;
        } else {
            session->state = STATE_LOCKED; // Khóa tài khoản sau 3 lần sai
        }
        return false;
    }
}

int main(void) {
    ATMSession session;
    atm_init(&session);
    printf("=== MO PHONG HE THONG ATM (CHUAN 5 TRANG THAI) ===\n");
    printf("Trang thai ban dau: IDLE\n");

    printf("\n[Thu nghiem nhap sai 3 lan]:\n");
    atm_verify_pin(&session, "0000");
    printf("Nhap sai lan 1 -> Trang thai: PIN_FAILED_1\n");
    atm_verify_pin(&session, "1111");
    printf("Nhap sai lan 2 -> Trang thai: PIN_FAILED_2\n");
    atm_verify_pin(&session, "2222");
    printf("Nhap sai lan 3 -> Trang thai: LOCKED\n");

    return 0;
}