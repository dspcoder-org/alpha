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
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: even number of elements
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [10, 20, 30, 40, 50, 60]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single element
        no_of_input_args = 1
        numbers = [no_of_input_args]
        input = [42]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: two elements
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input = [-10000, 10000]  # Using max and min values
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty list
        no_of_input_args = 0
        numbers = [no_of_input_args]
        input = []
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input = [-9999, -7777, -5555, -3333]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 7
        numbers = [no_of_input_args]
        input = [-10000, 0, 5555, -9999, 2222, -1111, 10000]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [9999, 9999, -9999, -9999, 0, 0]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args = 10000
        numbers = [no_of_input_args]
        input = list(range(-5000, 5000))
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 10
        numbers = [no_of_input_args]
        input = [10000, -10000] * 5
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_11(self, timeout_window = 5, override = 0):
        # List with all elements the same
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [7, 7, 7, 7, 7]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_12(self, timeout_window = 5, override = 0):
        # List with increasing sequence
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [1, 2, 3, 4, 5]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_13(self, timeout_window = 5, override = 0):
        # List with decreasing sequence
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [5, 4, 3, 2, 1]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_14(self, timeout_window = 5, override = 0):
        # List with alternating positive and negative numbers
        no_of_input_args = 6
        numbers = [no_of_input_args]
        input = [-1, 1, -2, 2, -3, 3]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_15(self, timeout_window = 5, override = 0):
        # List with zeros
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input = [0, 0, 0, 0]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_16(self, timeout_window = 5, override = 0):
        # List with large positive numbers
        no_of_input_args = 3
        numbers = [no_of_input_args]
        input = [99999, 88888, 77777]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_17(self, timeout_window = 5, override = 0):
        # List with large negative numbers
        no_of_input_args = 3
        numbers = [no_of_input_args]
        input = [-99999, -88888, -77777]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_18(self, timeout_window = 5, override = 0):
        # List with alternating large positive and negative numbers
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input = [99999, -99999, 88888, -88888]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_19(self, timeout_window = 5, override = 0):
        # List with a mix of small and large numbers
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input = [1, 10000, -1, -10000, 0]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_20(self, timeout_window = 5, override = 0):
        # List with a single large number
        no_of_input_args = 1
        numbers = [no_of_input_args]
        input = [100000]
        numbers.extend(input)
        input.reverse()
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value