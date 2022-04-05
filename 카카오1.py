import re
# -_.~!@#$%^&*()=+[{]}:?,<>/
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만
# 1번
def solution(new_id):

    new_id = new_id.lower()
    text = re.sub('[~!@#$%^&*()=+{}:?,<>/]', '', new_id)
    text = re.sub(r'(.)\1+', '.', text)

    if text[0] == '.':
        text = text[1:]
    if text == '':
        text = 'a'
    if text[-1] == '.':
        text = text[:-1]

    if len(text) >= 16:
        text = text[:15]
        if text[-1] == '.':
            text = text[:-1]

    if len(text) <= 2:
        while True:
            text += text[-1]
            if len(text) >= 3:
                break


    answer = text
    return answer



new_id = "...!@BaT#*..y.abc{defghijklm"

result = solution(new_id)

print(result)