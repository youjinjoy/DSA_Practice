def solution(phone_book):
    answer = True
    dic={}
    for number in phone_book:
        dic[number]=1
    
    for number in phone_book:
        s=""
        for n in number:
            s+=n
            if s in dic and s!=number:
                answer=False

    return answer