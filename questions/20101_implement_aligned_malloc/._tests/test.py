class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: small size and alignment
        size = 16
        alignment = 8
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: larger size and alignment
        size = 100
        alignment = 64
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: minimum size and alignment
        size = 1
        alignment = 2
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: maximum size
        size = 100000000
        alignment = 128
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: alignment larger than size
        size = 10
        alignment = 16
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with alignment of 1 (no alignment)
        size = 50
        alignment = 1
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with alignment equal to size
        size = 32
        alignment = 32
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with very large alignment
        size = 256
        alignment = 1024
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_9(self, timeout_window = 5, override = 0):
        # Case with small size and large alignment
        size = 8
        alignment = 64
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # Case with size and alignment both powers of 2
        size = 128
        alignment = 128
        input = f"{size} {alignment}"
        expected_value = "Allocated memory at: "
        return input, expected_value