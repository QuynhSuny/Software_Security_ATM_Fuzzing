# BÁO CÁO BÀI TẬP LỚN: AN TOÀN PHẦN MỀM
## Đề tài: Phương pháp fuzzing cho kiểm chứng hình thức của hệ thống ATM (`atm_fuzzing_verification`)

---

### 1. Thông tin chung
- **Sinh viên thực hiện:** Hoàng Như Quỳnh
- **Mã số sinh viên:** 23010027
- **Lớp:** K17_KTPM(EL)_1
- **Giảng viên hướng dẫn:** ThS. Vũ Quang Dũng
- **Công cụ thực hiện:** SecLabFramework (Educational Security Suite)

---

### 2. Yêu cầu môi trường & Cài đặt
- **Hệ điều hành:** Windows 10/11 (64-bit)
- **Python:** Phiên bản >= 3.10 (cần cài đặt `pytest`, `z3-solver`)
- **Trình biên dịch C:** GCC (MinGW-w64 / w64devkit)
- Cài đặt thư viện kiểm thử:
  ```bash
  pip install pytest

---

### 3. Cấu trúc thư mục bài nộp
```text
23010027_Hoang Nhu Quynh_BTL/
├── DacTa_ATM_Nhom10.xlsx             # File Excel dac ta 10 sheet
├── README.md                         # Huong dan cai dat va chay thuc nghiem
│
├── results/                          # Bang chung thuc nghiem va bao cao
│   ├── kripke_model.png              # So do Kripke 5 trang thai
│   ├── pipeline_execution.png        # Anh chup Pipeline Ch1-Ch6
│   ├── bao_cao_tich_hop_atm_fuzzing_verification.pdf # Bao cao tu tool
│   └── BaoCao_23010027_HoangNhuQuynh_ATM.pdf        # Bao cao chinh thuc
│
├── source/                           # Ma nguon he thong
│   ├── v0/                           # Ban goc chua loi
│   │   ├── parse_atm_pin_v0.c        # Loi CWE-120, 401, 415, 416
│   │   └── atm_logic_v0.py           # Loi CWE-248 va backdoor Z3
│   │
│   ├── v1/                           # Ban da va an toan
│   │   ├── parse_atm_pin_v1.c        # Da va CERT C STR31-C
│   │   └── atm_logic_v1.py           # Da kiem tra mau so va HMAC
│   │
│   └── atm_state_machine.c           # Mo phong may trang thai ATM
│
└── tests/                            # Goi kiem thu tu dong (53 test cases)
    ├── test_atm_pin_retry_ratio_fuzz.py
    ├── test_atm_admin_override_pin_fuzz.py
    ├── test_target_parse_atm_pin_fuzz.py
    ├── target_wrap.py
    ├── target_shim.c
    ├── sl_target.c
    └── libtarget_wrap.dll