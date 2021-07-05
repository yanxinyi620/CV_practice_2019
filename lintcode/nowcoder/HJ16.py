# ---------------------------------------
# 0-1 背包问题

# w: 每个物品重量列表; v: 每个物品价值列表
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]

# n: 前n个物品; c: 总重量上限
n = len(w)
c = 10

# 1. 动态规划解法
dp = [[0]*(c+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, c+1):
        if j-w[i-1]>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
print(dp[n][c])

# 2. 递归解法




# ---------------------------------------
# HJ16, 购物车问题

'''input()
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
'''

N, m = map(int, input().split())
primary, annex = {}, {}
for i in range(1, m+1):
    v, p, q = map(int, input().split())
    if q==0:
        primary[i] = [v, p]
    else:
        if q in annex:
            annex[q].append([v, p])
        else:
            annex[q] = [[v, p]]

dp = [0]*(N + 1)
for key in primary:
    w, v_ = [], []
    w.append(primary[key][0])  # 1: 主件
    v_.append(primary[key][0]*primary[key][1])
    if key in annex:  # 存在附件
        w.append(w[0]+annex[key][0][0])  # 2: 主件+附件1
        v_.append(v_[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:  # 附件个数为2
            w.append(w[0]+annex[key][1][0])  # 3: 主件+附件2
            v_.append(v_[0]+annex[key][1][0]*annex[key][1][1])
            w.append(w[0]+annex[key][0][0]+annex[key][1][0])  # 4: 主件+附件1+附件2
            v_.append(v_[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    for j in range(N,-1,-10):  # 物品的价格是10的整数倍
        for k in range(len(w)):
            if j-w[k]>=0:
                dp[j] = max(dp[j], dp[j-w[k]]+v_[k])
print(dp[N])

