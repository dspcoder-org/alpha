class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: merge two lists with some common elements
        input1 = [1, 2, 4]
        input2 = [1, 3, 4]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '1 1 2 3 4 4'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: merge two lists with no common elements
        input1 = [0, 3, 6]
        input2 = [1, 2, 5]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '0 1 2 3 5 6'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: one list is empty
        input1 = []
        input2 = [0, 1, 2]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '0 1 2'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: both lists are empty
        input1 = []
        input2 = []
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = ''
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: lists with one element each
        input1 = [1]
        input2 = [2]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '1 2'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        input1 = [-3, -2, -1]
        input2 = [-5, -4, 0]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '-5 -4 -3 -2 -1 0'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        input1 = [-10, -5, 0, 5]
        input2 = [-7, -3, 2, 8]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '-10 -7 -5 -3 0 2 5 8'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        input1 = [1, 1, 1]
        input2 = [1, 1, 1]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '1 1 1 1 1 1'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 5, override = 0):
        # Case with alternating numbers
        input1 = [1, 3, 5]
        input2 = [2, 4, 6]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '1 2 3 4 5 6'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # Case with large numbers
        input1 = [100000, 100001]
        input2 = [99999, 100002]
        numbers = f"{len(input1)}\n{' '.join(map(str, input1))}\n{len(input2)}\n{' '.join(map(str, input2))}"
        expected_value = '99999 100000 100001 100002'
        return numbers, expected_value