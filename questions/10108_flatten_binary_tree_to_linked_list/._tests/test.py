class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: complete binary tree
        no_of_input_args = 6
        input = [1, 2, 5, 3, 4, 6]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '1 2 3 4 5 6'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: simple binary tree
        no_of_input_args = 3
        input = [1, 2, 3]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '1 2 3'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: single node
        no_of_input_args = 1
        input = [42]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '42'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: two nodes
        no_of_input_args = 2
        input = [1, 2]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '1 2'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: empty tree
        no_of_input_args = 0
        input = []
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = ''
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args = 4
        input = [-10, -20, -30, -40]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-10 -20 -40 -30'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args = 7
        input = [-10, 20, -30, 40, -50, 60, -70]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '-10 20 40 -50 -30 60 -70'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args = 6
        input = [1, 1, 1, 1, 1, 1]
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '1 1 1 1 1 1'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large tree (10000 elements)
        no_of_input_args = 10000
        input = list(range(1, 10001))
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = ' '.join(map(str, input))
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # Tree with alternating max and min values
        no_of_input_args = 10
        input = [100000, -100000] * 5
        numbers = f"{no_of_input_args}\n{' '.join(map(str, input))}"
        expected_value = '100000 -100000 100000 -100000 100000 -100000 100000 -100000 100000 -100000'
        return numbers, expected_value