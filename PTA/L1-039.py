N = int(input())
sentence = list(input())
# N = len(sentence) if N > len(sentence) else N
output = [[] for _ in range(N)]
# while sentence:
#     try:
#         for i in output:
#             i.insert(0, sentence[0])
#             sentence.pop(0)
#     except IndexError:
#         i.insert(0, " ")

while sentence:
    for i in output:
        if sentence:
            i.insert(0, sentence[0])
            sentence.pop(0)
        else:
            i.insert(0, " ")


output = list(map("".join, output))
print("\n".join(output))
