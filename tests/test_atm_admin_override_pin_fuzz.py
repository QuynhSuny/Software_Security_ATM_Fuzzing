"""Test case SINH TỰ ĐỘNG từ fuzzing (sec_lab_framework v25) cho `atm_admin_override_pin` (PYTHON). Chế độ: characterization.
Mỗi test ghi rõ kỹ thuật fuzzing sinh ra nó."""
import math
import pytest
NAN = float('nan')   # dung so sanh nan: math.isnan

# ---- mã nguồn mục tiêu (nhúng để test chạy độc lập) ----
def atm_admin_override_pin(pin_a, pin_b):
    if pin_a == 7421:
        if pin_b == 3390:
            raise ValueError('magic value reached')
    return pin_a + pin_b
# ---- hết mã nguồn mục tiêu ----


def test_atm_admin_override_pin_boundary_1():
    # kỹ thuật: Biên / giá trị đặc biệt — +3 phần tử coverage mới
    assert atm_admin_override_pin(1, 1) == 2

def test_atm_admin_override_pin_boundary_2():
    # kỹ thuật: Biên / giá trị đặc biệt — +3 phần tử coverage mới
    assert atm_admin_override_pin(7421, 1) == 7422

def test_atm_admin_override_pin_boundary_3():
    # kỹ thuật: Biên / giá trị đặc biệt — kết quả đại diện
    assert atm_admin_override_pin(0, 1) == 1

def test_atm_admin_override_pin_boundary_4():
    # kỹ thuật: Biên / giá trị đặc biệt — kết quả đại diện
    assert atm_admin_override_pin(2, 1) == 3

def test_atm_admin_override_pin_blackbox_5():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_admin_override_pin(7, 106) == 113

def test_atm_admin_override_pin_blackbox_6():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_admin_override_pin(77, -6925) == -6848

def test_atm_admin_override_pin_blackbox_7():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_admin_override_pin(804833100429, -9931) == 804833090498

def test_atm_admin_override_pin_blackbox_8():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_admin_override_pin(185, 9) == 194

def test_atm_admin_override_pin_mutation_9():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_admin_override_pin(7421, 0) == 7421

def test_atm_admin_override_pin_mutation_10():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_admin_override_pin(3390, 1) == 3391

def test_atm_admin_override_pin_mutation_11():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_admin_override_pin(1, 7421) == 7422

def test_atm_admin_override_pin_mutation_12():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_admin_override_pin(1, 0) == 1

def test_atm_admin_override_pin_coverage_13():
    # kỹ thuật: Coverage-guided — kết quả đại diện
    assert atm_admin_override_pin(2, 3390) == 3392

def test_atm_admin_override_pin_concolic_14():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kích hoạt lỗi
    with pytest.raises(ValueError):
        atm_admin_override_pin(7421, 3390)

def test_atm_admin_override_pin_concolic_15():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kết quả đại diện
    assert atm_admin_override_pin(7421, 3391) == 10812

def test_atm_admin_override_pin_concolic_16():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kết quả đại diện
    assert atm_admin_override_pin(7422, 0) == 7422

def test_atm_admin_override_pin_concolic_17():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kết quả đại diện
    assert atm_admin_override_pin(3389, 1) == 3390
