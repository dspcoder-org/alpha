class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: cycle present
        input_str = "4 1\n1 2 3 4\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: no cycle
        input_str = "5 -1\n1 2 3 4 5\n"
        expected_value = "false"
        return input_str, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single node with cycle
        input_str = "1 0\n1\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: single node without cycle
        input_str = "1 -1\n1\n"
        expected_value = "false"
        return input_str, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        input_str = "0 -1\n"
        expected_value = "false"
        return input_str, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case: cycle at the head
        input_str = "3 0\n1 2 3\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case: cycle at the tail
        input_str = "4 3\n1 2 3 4\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case: cycle at the middle
        input_str = "5 2\n1 2 3 4 5\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 nodes) with cycle
        n = 10000
        pos = 5000
        nodes = list(range(1, n + 1))
        input_str = f"{n} {pos}\n" + " ".join(map(str, nodes)) + "\n"
        expected_value = "true"
        return input_str, expected_value

    def test_case_10(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 nodes) without cycle
        n = 10000
        pos = -1
        nodes = list(range(1, n + 1))
        input_str = f"{n} {pos}\n" + " ".join(map(str, nodes)) + "\n"
        expected_value = "false"
        return input_str, expected_value