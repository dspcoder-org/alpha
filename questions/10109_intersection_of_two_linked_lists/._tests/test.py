class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'
        
    def test_case_1(self, timeout_window = 5, override = 0):
        # Normal case: intersection at a middle node
        no_of_input_args_A = 5
        input_A = [4, 1, 8, 4, 5]
        no_of_input_args_B = 4
        input_B = [5, 6, 1, 8, 4, 5]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '8'
        return numbers, expected_value

    def test_case_2(self, timeout_window = 5, override = 0):
        # Normal case: no intersection
        no_of_input_args_A = 2
        input_A = [1, 9]
        no_of_input_args_B = 3
        input_B = [3, 2, 4]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = 'null'
        return numbers, expected_value

    def test_case_3(self, timeout_window = 5, override = 0):
        # Edge case: both lists are empty
        no_of_input_args_A = 0
        input_A = []
        no_of_input_args_B = 0
        input_B = []
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = 'null'
        return numbers, expected_value

    def test_case_4(self, timeout_window = 5, override = 0):
        # Edge case: one list is empty
        no_of_input_args_A = 3
        input_A = [2, 6, 4]
        no_of_input_args_B = 0
        input_B = []
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = 'null'
        return numbers, expected_value

    def test_case_5(self, timeout_window = 5, override = 0):
        # Edge case: intersection at the first node
        no_of_input_args_A = 3
        input_A = [1, 2, 3]
        no_of_input_args_B = 3
        input_B = [1, 2, 3]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '1'
        return numbers, expected_value

    def test_case_6(self, timeout_window = 5, override = 0):
        # Case with negative numbers
        no_of_input_args_A = 4
        input_A = [-9999, -7777, -5555, -3333]
        no_of_input_args_B = 4
        input_B = [-9999, -7777, -5555, -3333]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '-9999'
        return numbers, expected_value

    def test_case_7(self, timeout_window = 5, override = 0):
        # Case with mixed positive and negative numbers
        no_of_input_args_A = 5
        input_A = [-10000, 0, 5555, -9999, 2222]
        no_of_input_args_B = 5
        input_B = [5555, -9999, 2222, -1111, 10000]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '5555'
        return numbers, expected_value

    def test_case_8(self, timeout_window = 5, override = 0):
        # Case with repeated numbers
        no_of_input_args_A = 6
        input_A = [9999, 9999, -9999, -9999, 0, 0]
        no_of_input_args_B = 6
        input_B = [9999, 9999, -9999, -9999, 0, 0]
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '9999'
        return numbers, expected_value

    def test_case_9(self, timeout_window = 15, override = 0):  # Increased timeout_window for larger input
        # Large list (10000 elements)
        no_of_input_args_A = 10000
        input_A = list(range(-5000, 5000))
        no_of_input_args_B = 10000
        input_B = list(range(-5000, 5000))
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '-5000'
        return numbers, expected_value

    def test_case_10(self, timeout_window = 5, override = 0):
        # List with alternating max and min values
        no_of_input_args_A = 10
        input_A = [10000, -10000] * 5
        no_of_input_args_B = 10
        input_B = [10000, -10000] * 5
        numbers = f"{no_of_input_args_A}\n{' '.join(map(str, input_A))}\n{no_of_input_args_B}\n{' '.join(map(str, input_B))}"
        expected_value = '10000'
        return numbers, expected_value