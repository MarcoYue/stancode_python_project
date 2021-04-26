"""
File: anagram.py
Name: Marco
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []
possible_list = []
counts = 0


def main():
    global possible_list
    global counts
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    input_s = input('Find anagrams for : ')

    read_dictionary()  # 讀字典

    while input_s != EXIT:
        ans_list = find_anagrams(input_s)
        print(str(counts) + ' anagrams: ', end='')
        print(ans_list)
        possible_list = []
        input_s = input('Find anagrams for : ')
        counts = 0


def read_dictionary():  # read the dictionary
    global dict_list
    with open(FILE, 'r') as f:
        for line in f:
            line = string_up(line)
            dict_list.append(line)


def find_anagrams(s):
    """
    :param s: input string
    :return: return the anagrams list
    """
    global dict_list
    global possible_list
    global counts
    ans_list = []
    possible_list = finding_non_repetitive(s)  # 得到不重複的排列組合
    print("possible_list = " + str(possible_list))
    print('Searching...')
    for i in range(len(possible_list)):  # finding anagrams
        if possible_list[i] in dict_list:

            print('find :　'+str(possible_list[i]))
            counts += 1
            ans_list.append(possible_list[i])
            print('Searching...')

    return ans_list


def finding_non_repetitive(s):  # 這邊是回傳 輸入單字的所有"不重複的排列組合"
    out = []
    len_s = len(s)
    helper([], s, len_s, out)
    return out


def helper(current_s, s, len_s, out):
    if len(current_s) == len_s:
        temp = ''.join(current_s)  # 把它變回一個字串，而不是分開來的
        if temp not in out:  # 避免重複加入
            out.append(temp)

    for i in range(len(s)):
        current_s.append(s[i])  # choose
        helper(current_s, s[:i] + s[(i + 1):], len_s, out)  # explore ...精華的一行程式....
        current_s.pop()  # un choose


def has_prefix(sub_s):  # 我發現我不太知道要把他加在哪... 而且感覺加了速度還會變慢
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
