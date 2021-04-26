"""
File: boggle.py
Name: Marco Yue
----------------------------------------
TODO: To play a game called Boggle!
"""
import time
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []
new_dict_list = []
count = [0]


def main():
	"""
	TODO:input 4 ch for 4 row, play boggle!
	"""
	boggle = []
	no_problem = True  # 玩家輸入沒問題才繼續玩
	for i in range(4):
		line = input(str(i+1)+' row of letters: ').split()
		if len(line) == 4:
			for ch in line:
				if not ch.isalpha() or len(ch) > 1:
					no_problem = False
					break
			if no_problem:
				boggle.append(line)
			else:
				break
		else:
			no_problem = False
			break

	if no_problem is True:  # 玩家輸入沒問題
		read_dictionary()
		print('Your boggle is :', boggle)
		start = time.time()
		find_boggle(boggle)
		end = time.time()
		print('There are ' + str(count[0]) + ' words in total.')
		print("執行時間：%f 秒" % (end - start))
	else:
		print('illegal format')
	# s = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]  # 測試用!


def find_boggle(boggle):

	for i in range(len(boggle)):
		for j in range(len(boggle)):
			start_word = [boggle[i][j]]							# 選擇要開始搜尋的第一個字母是誰
			path = [[i, j]]  									# 用來記錄走過的路
			find_list = []  									# 紀錄找到的單字
			helper(boggle, start_word, i, j, path, find_list)


def helper(boggle, current_w, index_i, index_j, path, find_list):
	"""
	:param boggle: 輸入的boggle list[list]
	:param current_w: 已經包含起始字母的 list
	:param index_i:  紀錄起始字母的row位置 int
	:param index_j: 紀錄起始字母的column位置 int
	:param path:  紀錄走過的路徑 list
	:param find_list: 紀錄已經找到的單字 list
	:return: None
	"""
	answer = ''.join(current_w)
	if len(answer) >= 4:
		if answer not in find_list:  									# 避免找到重複的字
			if answer in dict_list:
				find_list.append(answer)
				count[0] += 1
				print('Found "'+str(answer)+'"')
				check = list(answer)  									# 把已經得到結果的答案再度分拆掉
				loop(boggle, check, index_i, index_j, path, find_list)  # 得到答案後繼續探索不要停~~~~
	else:
		loop(boggle, current_w, index_i, index_j, path, find_list)


def loop(boggle, current_w, index_i, index_j, path, find_list):  # 這是處理非 base case 情況的程式 我把它分拆出來了
	for x in range(-1, 2):
		for y in range(-1, 2):
			if x == 0 and y == 0:  # 不要原地踏步啦
				pass
			else:
				if [index_i + x, index_j + y] not in path:  					# 如果是沒走過的才要繼續走
					if 0 <= (index_i + x) <= 3 and 0 <= (index_j + y) <= 3: 	# 搜尋的路在可行的範圍內
						path.append([index_i + x, index_j + y]) 		 		# 記錄走過的路
						current_w.append(boggle[index_i + x][index_j + y])  	# choose

						# check = ''.join(current_w)							# 我加了prefix反而時間變更久......
						# if has_prefix(check):
						# 	helper(boggle, current_w, index_i + x, index_j + y, path, find_list)

						helper(boggle, current_w, index_i + x, index_j + y, path, find_list)  	# explore

						current_w.pop()  										# un choose
						path.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_list
	with open(FILE, 'r') as f:
		for line in f:
			line = string_up(line)
			if len(line) >= 4:  # 只要管長度大於4的單字就好
				dict_list.append(line)
	pass


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if word.startswith(sub_s):
			# sub_s in dict
			return True
		else:
			# sub_s not in dict
			pass
	return False


def string_up(s):  # 重新串字典的字串，把\n趕走
	ans = ''
	for ch in s:
		if ch != '\n':
			ans += ch
	return ans


if __name__ == '__main__':
	main()
