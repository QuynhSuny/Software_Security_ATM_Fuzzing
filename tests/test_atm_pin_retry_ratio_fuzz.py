"""Test case SINH TỰ ĐỘNG từ fuzzing (sec_lab_framework v25) cho `atm_pin_retry_ratio` (PYTHON). Chế độ: characterization.
Mỗi test ghi rõ kỹ thuật fuzzing sinh ra nó."""
import math
import pytest
NAN = float('nan')   # dung so sanh nan: math.isnan

# ---- mã nguồn mục tiêu (nhúng để test chạy độc lập) ----
def atm_pin_retry_ratio(total_attempts, failed_attempts):
    return total_attempts // failed_attempts
# ---- hết mã nguồn mục tiêu ----


def test_atm_pin_retry_ratio_boundary_1():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(1.0, 0)

def test_atm_pin_retry_ratio_boundary_2():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(0, 0)

def test_atm_pin_retry_ratio_boundary_3():
    # kỹ thuật: Biên / giá trị đặc biệt — +1 phần tử coverage mới
    assert atm_pin_retry_ratio(1.0, 1) == pytest.approx(1.0)

def test_atm_pin_retry_ratio_boundary_4():
    # kỹ thuật: Biên / giá trị đặc biệt — kết quả đại diện
    assert atm_pin_retry_ratio(0.0, 1) == pytest.approx(0.0)

def test_atm_pin_retry_ratio_boundary_5():
    # kỹ thuật: Biên / giá trị đặc biệt — kết quả đại diện
    assert atm_pin_retry_ratio(-0.0, 1) == pytest.approx(-0.0)

def test_atm_pin_retry_ratio_boundary_6():
    # kỹ thuật: Biên / giá trị đặc biệt — kết quả đại diện
    assert atm_pin_retry_ratio(-1.0, 1) == pytest.approx(-1.0)

def test_atm_pin_retry_ratio_blackbox_7():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(1e+308, 0)

def test_atm_pin_retry_ratio_blackbox_8():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(22.48898459858779, 0)

def test_atm_pin_retry_ratio_blackbox_9():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert repr(atm_pin_retry_ratio(float('nan'), -1642)) == 'nan'

def test_atm_pin_retry_ratio_blackbox_10():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_pin_retry_ratio(-55509.512847766746, 33) == pytest.approx(-1683.0)

def test_atm_pin_retry_ratio_blackbox_11():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_pin_retry_ratio(1000000000.0, 175) == pytest.approx(5714285.0)

def test_atm_pin_retry_ratio_blackbox_12():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    assert atm_pin_retry_ratio(-467338.87908548093, 9370) == pytest.approx(-50.0)

def test_atm_pin_retry_ratio_mutation_13():
    # kỹ thuật: Mutation (đột biến seed) — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(-0.0, 0)

def test_atm_pin_retry_ratio_mutation_14():
    # kỹ thuật: Mutation (đột biến seed) — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(1.0474234445716815, 0)

def test_atm_pin_retry_ratio_mutation_15():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_pin_retry_ratio(0.0, 2305843009213693953) == pytest.approx(0.0)

def test_atm_pin_retry_ratio_mutation_16():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_pin_retry_ratio(1e+308, 1) == pytest.approx(1e+308)

def test_atm_pin_retry_ratio_mutation_17():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    assert atm_pin_retry_ratio(-1.9128507628962974, 1) == pytest.approx(-2.0)

def test_atm_pin_retry_ratio_coverage_18():
    # kỹ thuật: Coverage-guided — crash mới
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(-1.0, 0)

def test_atm_pin_retry_ratio_coverage_19():
    # kỹ thuật: Coverage-guided — kết quả đại diện
    assert atm_pin_retry_ratio(-0.44574119565331194, 1) == pytest.approx(-1.0)

def test_atm_pin_retry_ratio_coverage_20():
    # kỹ thuật: Coverage-guided — kết quả đại diện
    assert atm_pin_retry_ratio(1.0, 2) == pytest.approx(0.0)

def test_atm_pin_retry_ratio_coverage_21():
    # kỹ thuật: Coverage-guided — kết quả đại diện
    assert atm_pin_retry_ratio(2.0, 1) == pytest.approx(2.0)

def test_atm_pin_retry_ratio_concolic_22():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kích hoạt lỗi
    with pytest.raises(ZeroDivisionError):
        atm_pin_retry_ratio(0.0, 0)
