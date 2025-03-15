class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: cycle at the end
        no_of_input_args = 5
        numbers = [no_of_input_args, 4]
        input = [1, 2, 3, 4, 5]
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: cycle in the middle
        no_of_input_args = 6
        numbers = [no_of_input_args, 2]
        input = [10, 20, 30, 40, 50, 60]
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single element with cycle (self-loop)
        no_of_input_args = 1
        numbers = [no_of_input_args, 0]
        input = [42]
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: no cycle
        no_of_input_args = 5
        numbers = [no_of_input_args, -1]
        input = [1, 2, 3, 4, 5]
        numbers.extend(input)
        expected_value = "false"
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        no_of_input_args = 0
        numbers = [no_of_input_args, -1]
        input = []
        numbers.extend(input)
        expected_value = "false"
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with cycle at the beginning
        no_of_input_args = 4
        numbers = [no_of_input_args, 0]
        input = [-9999, -7777, -5555, -3333]
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with cycle at the second node
        no_of_input_args = 7
        numbers = [no_of_input_args, 1]
        input = [-10000, 0, 5555, -9999, 2222, -1111, 10000]
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers and no cycle
        no_of_input_args = 6
        numbers = [no_of_input_args, -1]
        input = [9999, 9999, -9999, -9999, 0, 0]
        numbers.extend(input)
        expected_value = "false"
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements) with cycle at the end
        no_of_input_args = 10000
        numbers = [no_of_input_args, 9999]
        input = list(range(-5000, 5000))
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values and cycle in the middle
        no_of_input_args = 10
        numbers = [no_of_input_args, 5]
        input = [10000, -10000] * 5
        numbers.extend(input)
        expected_value = "true"
        return numbers, expected_value