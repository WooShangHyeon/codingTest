def solution(phone_book):
    answer = True
    
    # #zip
    # phone_book.sort()
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    
    #hash
    ph_hash = {x : 1 for x in phone_book}
    for nums in phone_book:
        str = ""
        for num in nums:
            str += num
            if str in ph_hash and str!=nums:
                return False

    return answer