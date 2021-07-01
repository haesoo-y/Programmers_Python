def solution(s, n):
    answer = ''
    for c in s:
        code = ord(c)
        if c == " ":
            answer += " "
            continue
        limit = 90 if code <= 90 else 122 # 아스키코드 대문자 65~90, 소문자 97~122
        code += n
        answer += chr(code) if code <= limit else chr(code-26)
    return answer