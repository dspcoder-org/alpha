class testCases:
    def __init__(self, koro_exe) -> None:
        self.RUN = 3
        self.exe = koro_exe
        self.default_timeout_window = 10
        self.usage = 'prod'

    # Added comments to explain the purpose of each test case
    def test_case_1(self, timeout_window=5, override=0):
        # Normal case: cycle present
        no_of_input_args = 4
        pos = 1
        input = [1, 2, 3, 4]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_2(self, timeout_window=5, override=0):
        # Normal case: cycle present at head
        no_of_input_args = 5
        pos = 0
        input = [3, -3, 4, 0, 2]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_3(self, timeout_window=5, override=0):
        # Edge case: no cycle
        no_of_input_args = 3
        pos = -1
        input = [2, 0, 1]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_4(self, timeout_window=5, override=0):
        # Edge case: single node, no cycle
        no_of_input_args = 1
        pos = -1
        input = [42]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_5(self, timeout_window=5, override=0):
        # Edge case: single node, cycle to itself
        no_of_input_args = 1
        pos = 0
        input = [42]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_6(self, timeout_window=5, override=0):
        # Case with negative numbers, cycle present
        no_of_input_args = 4
        pos = 2
        input = [-9999, -7777, -5555, -3333]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_7(self, timeout_window=5, override=0):
        # Case with mixed positive and negative numbers, no cycle
        no_of_input_args = 7
        pos = -1
        input = [-10000, 0, 5555, -9999, 2222, -1111, 10000]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_8(self, timeout_window=5, override=0):
        # Case with repeated numbers, cycle present
        no_of_input_args = 6
        pos = 3
        input = [9999, 9999, -9999, -9999, 0, 0]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_9(self, timeout_window=15, override=0):
        # Large list (10,000 elements), no cycle
        no_of_input_args = 10000
        pos = -1
        input = list(range(-5000, 5000))
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_10(self, timeout_window=5, override=0):
        # List with alternating max and min values, cycle present
        no_of_input_args = 10
        pos = 5
        input = [10000, -10000] * 5
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_11(self, timeout_window=5, override=0):
        # List with all elements the same, no cycle
        no_of_input_args = 5
        pos = -1
        input = [7, 7, 7, 7, 7]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_12(self, timeout_window=5, override=0):
        # List with increasing sequence, cycle present
        no_of_input_args = 5
        pos = 2
        input = [1, 2, 3, 4, 5]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_13(self, timeout_window=5, override=0):
        # List with decreasing sequence, no cycle
        no_of_input_args = 5
        pos = -1
        input = [5, 4, 3, 2, 1]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_14(self, timeout_window=5, override=0):
        # List with alternating positive and negative numbers, cycle present
        no_of_input_args = 6
        pos = 1
        input = [-1, 1, -2, 2, -3, 3]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_15(self, timeout_window=5, override=0):
        # List with zeros, no cycle
        no_of_input_args = 4
        pos = -1
        input = [0, 0, 0, 0]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_16(self, timeout_window=5, override=0):
        # List with large positive numbers, cycle present
        no_of_input_args = 3
        pos = 0
        input = [99999, 88888, 77777]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_17(self, timeout_window=5, override=0):
        # List with large negative numbers, no cycle
        no_of_input_args = 3
        pos = -1
        input = [-99999, -88888, -77777]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_18(self, timeout_window=5, override=0):
        # List with alternating large positive and negative numbers, cycle present
        no_of_input_args = 4
        pos = 2
        input = [99999, -99999, 88888, -88888]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_19(self, timeout_window=5, override=0):
        # List with a mix of small and large numbers, no cycle
        no_of_input_args = 5
        pos = -1
        input = [1, 10000, -1, -10000, 0]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_20(self, timeout_window=5, override=0):
        # List with a single large number, cycle to itself
        no_of_input_args = 1
        pos = 0
        input = [100000]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_21(self, timeout_window=5, override=0):
        # Edge case: list with only zeros, no cycle
        no_of_input_args = 5
        pos = -1
        input = [0, 0, 0, 0, 0]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_22(self, timeout_window=5, override=0):
        # Edge case: list with alternating large positive and small negative numbers, cycle present
        no_of_input_args = 6
        pos = 4
        input = [100000, -1, 99999, -2, 88888, -3]
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value

    def test_case_23(self, timeout_window=5, override=0):
        # Edge case: list with maximum and minimum integer values, no cycle
        no_of_input_args = 2
        pos = -1
        input = [2147483647, -2147483648]  # Max and min 32-bit signed integers
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'false'
        return numbers, expected_value

    def test_case_master(self, timeout_window=5, override=0):
        # Master test case
        # This test case is designed to be a bit more complex and larger than the others.
        # Checking the performance of the function with a larger input size given in readme     
        # 1. The number of nodes in the list is in the range `[0, 10,000]`.
        # 2. Each node's value satisfies `-10⁵ ≤ Node.val ≤ 10⁵`.
        no_of_input_args = 10000
        pos = 5000
        input = list(range(-5000, 5000))
        numbers = f"{no_of_input_args} {pos}\n{' '.join(map(str, input))}"
        expected_value = 'true'
        return numbers, expected_value