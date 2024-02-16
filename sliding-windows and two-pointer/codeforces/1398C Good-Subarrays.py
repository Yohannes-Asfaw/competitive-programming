for t in range(int(input())):
    n = int(input())
    nums = list(map(int,list(input())))
    rs = 0
    dic = {0:1}
    ctr = 0
    for i in range(n):
        rs += nums[i]
        i += 1
        if rs - i in dic:
            ctr += dic[rs-i]
        dic[rs-i] = dic.get(rs-i, 0) + 1
    print(ctr)