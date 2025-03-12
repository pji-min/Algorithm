def solution(phone_number):
    
    sli = phone_number[-4:]
    
    count = len(phone_number) - 4
    
    str1 = f"{'*' * count}"
    
    answer = str1+sli
    
    return answer