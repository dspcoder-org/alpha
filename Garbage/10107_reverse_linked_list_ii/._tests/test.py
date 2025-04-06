class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: reverse middle part
        no_of_input_args = 5
        input = [1, 2, 3, 4, 5]
        left, right = 2, 4
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '1 4 3 2 5'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: reverse from start
        no_of_input_args = 3
        input = [10, 20, 30]
        left, right = 1, 2
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '20 10 30'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        input = [42]
        left, right = 1, 1
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '42'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: reverse entire list
        no_of_input_args = 2
        input = [-10000, 10000]
        left, right = 1, 2
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '10000 -10000'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args = 4
        input = [-9999, -7777, -5555, -3333]
        left, right = 2, 3
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '-9999 -5555 -7777 -3333'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 7
        input = [-10000, 0, 5555, -9999, 2222, -1111, 10000]
        left, right = 3, 5
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '-10000 0 2222 -9999 5555 -1111 10000'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 6
        input = [9999, 9999, -9999, -9999, 0, 0]
        left, right = 1, 6
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '0 0 -9999 -9999 9999 9999'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args = 10000
        input = list(range(-5000, 5000))
        left, right = 1, 10000
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_9(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 10
        input = [10000, -10000] * 5
        left, right = 3, 8
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '10000 -10000 -10000 10000 -10000 10000 -10000 10000 10000 -10000'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with all elements the same
        no_of_input_args = 5
        input = [7, 7, 7, 7, 7]
        left, right = 2, 4
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}\n{left} {right}"
        expected_value = '7 7 7 7 7'
        return numbers, expected_value