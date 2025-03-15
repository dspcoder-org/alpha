class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: merging two lists with odd number of elements
        no_of_input_args = 3
        numbers = [no_of_input_args]
        input1 = [1, 2, 4]
        numbers.extend(input1)
        no_of_input_args2 = 3
        numbers.append(no_of_input_args2)
        input2 = [1, 3, 4]
        numbers.extend(input2)
        expected_value = '1 1 2 3 4 4'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: merging two lists with even number of elements
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input1 = [1, 3]
        numbers.extend(input1)
        no_of_input_args2 = 3
        numbers.append(no_of_input_args2)
        input2 = [2, 4, 5]
        numbers.extend(input2)
        expected_value = '1 2 3 4 5'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: merging two single-element lists
        no_of_input_args = 1
        numbers = [no_of_input_args]
        input1 = [42]
        numbers.extend(input1)
        no_of_input_args2 = 1
        numbers.append(no_of_input_args2)
        input2 = [43]
        numbers.extend(input2)
        expected_value = '42 43'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: merging two lists with two elements each
        no_of_input_args = 2
        numbers = [no_of_input_args]
        input1 = [-10000, 10000]
        numbers.extend(input1)
        no_of_input_args2 = 2
        numbers.append(no_of_input_args2)
        input2 = [-9999, 9999]
        numbers.extend(input2)
        expected_value = '-10000 -9999 9999 10000'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: merging two empty lists
        no_of_input_args = 0
        numbers = [no_of_input_args]
        input1 = []
        numbers.extend(input1)
        no_of_input_args2 = 0
        numbers.append(no_of_input_args2)
        input2 = []
        numbers.extend(input2)
        expected_value = ''
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input1 = [-9999, -7777, -5555, -3333]
        numbers.extend(input1)
        no_of_input_args2 = 3
        numbers.append(no_of_input_args2)
        input2 = [-8888, -6666, -4444]
        numbers.extend(input2)
        expected_value = '-9999 -8888 -7777 -6666 -5555 -4444 -3333'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 4
        numbers = [no_of_input_args]
        input1 = [-10000, 0, 5555, 10000]
        numbers.extend(input1)
        no_of_input_args2 = 3
        numbers.append(no_of_input_args2)
        input2 = [-9999, 2222, 9999]
        numbers.extend(input2)
        expected_value = '-10000 -9999 0 2222 5555 9999 10000'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 3
        numbers = [no_of_input_args]
        input1 = [9999, 9999, 9999]
        numbers.extend(input1)
        no_of_input_args2 = 3
        numbers.append(no_of_input_args2)
        input2 = [-9999, -9999, -9999]
        numbers.extend(input2)
        expected_value = '-9999 -9999 -9999 9999 9999 9999'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args = 5000
        numbers = [no_of_input_args]
        input1 = list(range(-5000, 0))
        numbers.extend(input1)
        no_of_input_args2 = 5000
        numbers.append(no_of_input_args2)
        input2 = list(range(0, 5000))
        numbers.extend(input2)
        expected_value = ' '.join(map(str, range(-5000, 5000)))
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args = 5
        numbers = [no_of_input_args]
        input1 = [10000, 10000, 10000, 10000, 10000]
        numbers.extend(input1)
        no_of_input_args2 = 5
        numbers.append(no_of_input_args2)
        input2 = [-10000, -10000, -10000, -10000, -10000]
        numbers.extend(input2)
        expected_value = '-10000 -10000 -10000 -10000 -10000 10000 10000 10000 10000 10000'
        return numbers, expected_value
