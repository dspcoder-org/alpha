class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: odd number of elements
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [1, 2, 3, 4, 5]
        numbers.extend(input)
        expected_value = '3'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: even number of elements
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [10, 20, 30, 40, 50, 60]
        numbers.extend(input)
        expected_value = '40'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        numbers = [no_of_input_args]
        input = [42]
        numbers.extend(input)
        expected_value = '42'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: two elements
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input = [-10000, 10000]  # Using max and min values
        numbers.extend(input)
        expected_value = '10000'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input = [-9999, -7777, -5555, -3333]
        numbers.extend(input)
        expected_value = '-5555'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 7
        numbers = [no_of_input_args]
        input = [-10000, 0, 5555, -9999, 2222, -1111, 10000]
        numbers.extend(input)
        expected_value = '-9999'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [9999, 9999, -9999, -9999, 0, 0]
        numbers.extend(input)
        expected_value = '-9999'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args = 10000
        numbers = [no_of_input_args]
        input = list(range(-5000, 5000))
        numbers.extend(input)
        expected_value = '0'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 10
        numbers = [no_of_input_args]
        input = [10000, -10000] * 5
        numbers.extend(input)
        expected_value = '-10000'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with only zeros
        no_of_input_args = 7
        numbers = [no_of_input_args]
        input = [0] * 7
        numbers.extend(input)
        expected_value = '0'
        return numbers, expected_value