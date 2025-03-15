class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Palindrome case: odd number of elements
        no_of_input_args = 5
        input = [1, 2, 3, 2, 1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Palindrome case: even number of elements
        no_of_input_args = 4
        input = [1, 2, 2, 1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Non-palindrome case
        no_of_input_args = 3
        input = [1, 2, 3]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        input = [42]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        no_of_input_args = 0
        input = []
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Palindrome with negative numbers
        no_of_input_args = 5
        input = [-1, -2, -3, -2, -1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Non-palindrome with mixed numbers
        no_of_input_args = 6
        input = [-1, 2, -3, 3, 2, 1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Palindrome with repeated numbers
        no_of_input_args = 6
        input = [1, 1, 1, 1, 1, 1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large palindrome list (10000 elements)
        no_of_input_args = 10000
        input = list(range(5000)) + list(range(5000)[::-1])
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 10
        input = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value