class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: odd number of elements, palindrome
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [1, 2, 3, 2, 1]
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: even number of elements, palindrome
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input = [1, 2, 2, 1]
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Normal case: odd number of elements, not a palindrome
        no_of_input_args = 3
        numbers = [no_of_input_args]
        input = [1, 2, 3]
        numbers.extend(input)
        expected_value = 'false'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        numbers = [no_of_input_args]
        input = [42]
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: two elements, palindrome
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input = [100, 100]
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Edge case: two elements, not a palindrome
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input = [100, 200]
        numbers.extend(input)
        expected_value = 'false'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        no_of_input_args = 0
        numbers = [no_of_input_args]
        input = []
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with negative numbers, palindrome
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [-1, -2, -3, -2, -1]
        numbers.extend(input)
        expected_value = 'true'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 5, override = 0):
        # Case with negative numbers, not a palindrome
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [-1, -2, -3, -4, -5]
        numbers.extend(input)
        expected_value = 'false'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with two halves being mirror images, not a palindrome
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [1, 2, 3, 4, 2, 1]
        numbers.extend(input)
        expected_value = 'false'
        return numbers, expected_value