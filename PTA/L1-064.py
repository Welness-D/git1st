import re
N = int(input())

arr = []

for _ in range(N):
    arr.append(input())
pattern = re.compile(r'\b(can|could) you\b')
pattern2 = re.compile(r'\bI\b')
pattern3 = re.compile(r'(\bI\b)|(\b(can|could) you\b)')

for v in arr:
    print(v)
    # 处理空格
    v = re.sub(r"\s+", ' ', v)
    v = re.sub(r"(^[\s])|([\s]$)", '', v)
    v = re.sub(r"\s+(?=[^A-Za-z0-9\s+])", '', v)
    # 大写变小写
    v = re.sub(r"[A-HJ-Z]", lambda x: x.group().lower(), v)
    # I me you ,could you ,can you 转换
    # 替换I和me
    v = re.sub(r'\b(I|me)\b', r'yyoouu', v)    
    # 替换can you和could you
    v = re.sub(r'\b(can|could) you\b', r'I \1', v)
     # 替换I和me
    v = re.sub(r'(yyoouu)+', r'you', v)    
    # 处理问号
    v = re.sub(r"\?", '!', v)

    print("AI: "+v)
