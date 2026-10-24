"""Test case SINH TỰ ĐỘNG từ fuzzing (sec_lab_framework v25) cho `parse_atm_pin` (C). Chế độ: characterization.
Mỗi test ghi rõ kỹ thuật fuzzing sinh ra nó."""
import math
import pytest
NAN = float('nan')   # dung so sanh nan: math.isnan
import target_wrap as w


def test_parse_atm_pin_boundary_1():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    # kỳ vọng crash: ACCESS_VIOLATION
    r = w.call_isolated('parse_atm_pin', '<script>alert(1)</script>')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_boundary_2():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_boundary_3():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    # kỳ vọng crash: ACCESS_VIOLATION
    r = w.call_isolated('parse_atm_pin', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_boundary_4():
    # kỹ thuật: Biên / giá trị đặc biệt — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', 'A' * 64)
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_boundary_5():
    # kỹ thuật: Biên / giá trị đặc biệt — +4 phần tử coverage mới
    r = w.call_isolated('parse_atm_pin', 'hello')
    assert r["status"] == "ok"

def test_parse_atm_pin_blackbox_6():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', '78f8v4/4LJpx13p%n WGySnuItP5jkYBgKeC-lON6iGj2zmYy6-EUA.1wAMhTt_8QrqgvsiPvahlsBf3YPAWJM2OtlHJ0ZJ%oWJBMYgS4D vWNaj9YM29xZ9uKVSAv/68d7ndU8irQSLMQLy.JjAR.QP6Ik%pFGVrdYefAtO/T3.iNH CS-kcQDu9_risFv--YPq5fViV0fjODzS/W_gd5k')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_blackbox_7():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    # kỳ vọng crash: ACCESS_VIOLATION
    r = w.call_isolated('parse_atm_pin', 'EdTV1wjcBzs-qGg7UVKY0VDKbOIpeBVxPLUIw6va0Ey4IwT0% 99.4Vn%Zqn8 mqGEjQYL/TZy87O4%n7kjzwQwWIzHduOmfhH2PRN3vWYbLKOFty541-R/I3YH_OFKuu0ueDTA34dZiijFW WEM.P//5iMd-xssW2w%rMm QrI38JOvi4D4FiItJsYBz/sBR0a/SyCccU4Eb12_1Q/F N8ccLp5FY1Af3Yo0wwjVvDi.WeqI-dS.hJ/cf09dKxD hLF56wHu1N/bLPAxeN_c2u3RKmk1Q%e04%xZn/Q/y/mYlO.qjQ9Hji5bTeBn5wfI-ZNeRRBl/FmMcikdMS3cY6lBkSQTXTmdqr5TqmhIueR_k-3Uc1OyvD2v3_rW-8XNJHsTqHNFLvt6hH1VgSb-ezNy8XKOX1I5/hQGyOmZUU2LX0KGv6Tz.xhW6qEWMV0GCP4OpvGwZ5HJ5lv/6 ghMBWq0jytLVLx38gE9Ymugomsqp8VnckArOWG2LU5DiOgAMZ%V%_NGvxOcfR.QU6p3kL1/nPrYI9fWa0dC%ii/VU fhacCpXJ-DGMijLQR28e61PBAzIb0%d7aI3bg02vl5EeDmHbAZXdysmRnklo5ezZYzQRhh104C45.U-PK o.I U7PnsxnJ0L6-IIlf9P4%mhFeAlmZYUQmIzrSUJ.9f%7f2dzoMxH/2uL_i-jzR6m7o _YKLj1Ce/%.Nt_H_%PEF5%nZpkzhXMFYxyyrFpbMJ/AqhLXO5Evs3_rOvr_5QSwDAoH%U9KAYkUYYXCyTGvrr3G6I3FYYkiONgfmci9HDGxmjoRdUMr75m24o9v5/rS/cA-EdqSTuaEftBkNRYUiGJTXqkeFFetm27/TQYg3MOwkT5lK%25Fp%BY5JHoM0VmG6VMm4oKT_vygWTRfTJ7C6ce_nOpBHS2yeNGV/Y5OEx1bI9K/NR-JU-ZxM%umrdiRO/%dnL_Q92Ehq0Z1HQ%o2xcKZb9jJv_Jwg')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_blackbox_8():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', '/uGgPmJrmdfSCrdd0 QSt_t7GST_Jp7I')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_blackbox_9():
    # kỹ thuật: Black-box (ngẫu nhiên) — kích hoạt lỗi
    # kỳ vọng crash: ACCESS_VIOLATION
    r = w.call_isolated('parse_atm_pin', '1pDg9tTY1GDnPUzWYN99bwgBMXlC o')
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_blackbox_10():
    # kỹ thuật: Black-box (ngẫu nhiên) — kết quả đại diện
    r = w.call_isolated('parse_atm_pin', 'ekmTEcd')
    assert r["status"] == "ok"

def test_parse_atm_pin_mutation_11():
    # kỹ thuật: Mutation (đột biến seed) — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', 'A' * 300)
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_mutation_12():
    # kỹ thuật: Mutation (đột biến seed) — kích hoạt lỗi
    # kỳ vọng crash: TIMEOUT
    r = w.call_isolated('parse_atm_pin', 'A' * 128)
    assert r["status"] in ("crash", "timeout")

def test_parse_atm_pin_mutation_13():
    # kỹ thuật: Mutation (đột biến seed) — kết quả đại diện
    r = w.call_isolated('parse_atm_pin', '/')
    assert r["status"] == "ok"

def test_parse_atm_pin_concolic_14():
    # kỹ thuật: Concolic / white-box (SMT + hằng số) — kết quả đại diện
    r = w.call_isolated('parse_atm_pin', '%s\n')
    assert r["status"] == "ok"
