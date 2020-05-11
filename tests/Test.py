from tests import approximate_entropy_test_12, binary_matrix_rank_test_05, cumulative_sums_test_13
from tests import dft_test_06, frequency_within_block_test_02, linear_complexity_test_10, longest_run_ones_in_a_block_test_04, maurers_universal_test_09
from tests import monobit_test_01, non_overlapping_template_matching_test_07, overlapping_template_matching_test_08
from tests import random_excursion_variant_test_15, random_excursion_test_14, runs_test_03, serial_test_11


input_file = open('/Users/truffy/Documents/Python/projects/PRNG_Lab/result.txt', "r")
input = input_file.read()
n = len(input)
NUM_TEST = 15
print(n)


print("test 1: ", end=" ")
monobit_test_01.test(input, n)
print("test 2: ", end=" ")
frequency_within_block_test_02.test(input, n)
print("test 3: ", end=" ")
runs_test_03.test(input, n)
print("test 4: ", end=" ")
longest_run_ones_in_a_block_test_04.test(input, n)
print("test 5: ", end=" ")
binary_matrix_rank_test_05.test(input, n)
print("test 6: ")
dft_test_06.test(input, n)
print("test 7: ", end=" ")
non_overlapping_template_matching_test_07.test(input, n)
print("test 8: ")
overlapping_template_matching_test_08.test(input, n)
print("test 9: ", end=" ")
maurers_universal_test_09.test(input, n)
print("test 10: ", end=" ")
linear_complexity_test_10.test(input, n)
print("test 11: ", end=" ")
serial_test_11.test(input, n)
print("test 12: ", end=" ")
approximate_entropy_test_12.test(input, n)
print("test 13: ", end=" ")
cumulative_sums_test_13.test(input,n)
print("test 14: ", end=" ")
random_excursion_test_14.test(input,n)
print("test 15: ", end=" ")
random_excursion_variant_test_15.test(input, n)





