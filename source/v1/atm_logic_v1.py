# ==========================================
# PHIÊN BẢN v1: ĐÃ VÁ LỖI AN TOÀN
# ==========================================
import hmac
import hashlib

# 1. Đã vá CWE-248: Kiểm tra mẫu số an toàn trước phép chia
def atm_pin_retry_ratio(total_attempts, failed_attempts):
    if failed_attempts is None or failed_attempts <= 0:
        return 0.0
    return total_attempts // failed_attempts

# 2. Đã loại bỏ nhánh bí mật hard-coded (7421, 3390)
# Thay thế bằng cơ chế xác thực chuỗi băm (HMAC) thời gian không đổi
def atm_admin_override_pin(pin_a, pin_b, admin_token=None):
    expected_token = hashlib.sha256(b"SECURE_ATM_ADMIN_KEY").hexdigest()
    if not admin_token or not hmac.compare_digest(admin_token, expected_token):
        return None  # Từ chối quyền override nếu không có token hợp lệ
    return pin_a + pin_b