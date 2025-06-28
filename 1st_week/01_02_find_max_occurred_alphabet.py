# 알파벳 문자열 0~25까지 인덱스 배열 변환
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

# 변환된 배열에서 최대값을 찾고, 최대값 알파벳 반환
def find_max_occurred_alphabet(string):
     alphabet_occurrence_array = find_alphabet_occurrence_array(string)

     max_value_dup = max(alphabet_occurrence_array)
     max_value_dup = alphabet_occurrence_array.index(max_value_dup)

     return chr(max_value_dup + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))