# 打印九九乘法表  Ywx
for value in range(1, 10):
    for v in range(1, value+1):
        cheng = v * value
        print(str(v) + "*" + str(value) + "=" + str(cheng) + '\t', end="")
    print("\n") 