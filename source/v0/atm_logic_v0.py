# ==========================================
# PHIÊN BẢN v0: CHỨA CÁC LỖ HỔNG LOGIC & RUNTIME
# ==========================================

# 1. Lỗ hổng CWE-248 (Uncaught Exception): Lỗi chia cho 0 khi failed_attempts = 0
def atm_pin_retry_ratio(total_attempts, failed_attempts):
    return total_attempts // failed_attempts

# 2. Lỗ hổng backdoor / logic ẩn (Magic Value) phục vụ Concolic Fuzzing
def atm_admin_override_pin(pin_a, pin_b):
    if pin_a == 7421:
        if pin_b == 3390:
            raise ValueError('magic value reached')
    return pin_a + pin_b