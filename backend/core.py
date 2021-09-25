
input(w_bill, e_bill, g_fee, i_fee)

rent = 60000
util_cost = sum(w_bill, e_bill, g_fee, i_fee)
live_cost = sum(x, y)

def pico_pay(util_cost, rent):
    diff = live_cost / 2
    if util_cost.isdecimal():
        hoge = util_cost/2 + rent
        total = hoge + diff
    print(total)

# 光熱費(int) = 水 + 電気 + ガス + ネット
# A:float = 光熱費 / 2 + 60,000(家賃)

# 生活費(int) = x + y
# B:float = 一人当たりの生活費 / 2
# B は差分(unsigned char)
# ans(int) = A + (+-)B
