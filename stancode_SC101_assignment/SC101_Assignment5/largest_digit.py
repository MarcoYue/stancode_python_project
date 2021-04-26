"""
File: largest_digit.py
Name: Marco Yue
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: input number
	:return: return largest digit
	"""
	meter = 1
	recent_max = 0
	if n < 0:  # if n is a negative num, positive it.
		n *= -1
	return helper(n, meter, recent_max)


def helper(n, meter, recent_max):
	if n // meter % 10 == 0:  # base case, there's no digit.
		return recent_max
	else:
		if n // meter % 10 > recent_max:
			recent_max = n // meter % 10
		return helper(n, meter*10, recent_max)  # for each recurse, meter should multiple 10 for getting the next digit.


if __name__ == '__main__':
	main()
