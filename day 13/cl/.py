# def words_length(number):
#     num = 0
#     for i in number:
#         num = num + 1
#     return num


# def how_many_k(text):
#     total = 0
#     for ch in text.lower():
#         if ch == 'k':
#             total += 1
#     return total


def sum_numbers_in_list(data):
    total = 0
    for i in data:
        try:
            total += i
        except:
            continue
    return total