class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: duplicates in the middle
        no_of_input_args = 5
        input = [1, 1, 2, 3, 3]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '1 2 3'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: duplicates at the start
        no_of_input_args = 4
        input = [10, 10, 20, 30]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '10 20 30'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        input = [42]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '42'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: two elements, no duplicates
        no_of_input_args = 2
        input = [-10000, 10000]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-10000 10000'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        no_of_input_args = 0
        input = []
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = ''
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers and duplicates
        no_of_input_args = 4
        input = [-9999, -9999, -5555, -5555]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-9999 -5555'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 7
        input = [-10000, -10000, 0, 5555, 5555, 10000, 10000]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-10000 0 5555 10000'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 6
        input = [9999, 9999, 9999, 9999, 9999, 9999]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '9999'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args = 10000
        input = list(range(-5000, 5000))
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 10
        input = [-10000, -10000, -10000, -10000, 0, 0, 10000, 10000, 10000, 10000]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-10000 0 10000'
        return numbers, expected_value