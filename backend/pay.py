# FIX: 変数で値受け取り
# input(bill_w, bill_e, fee_gas, fee_i)
[bill_w, bill_e, fee_gas, fee_i] = [1, 2, 3, 4]
a:int = 15000
b:int = 10000
base = 60000
# 光熱費:int = 水 + 電気 + ガス + ネット
util_cost = bill_w + bill_e + fee_gas + fee_i
# 生活費:int = a + b
live_cost = a + b

# A:float = 光熱費 / 2 + 60,000[base]
# B:float = 生活費(total_a + total_b) / 2
# total_a, total_b の差分[diff]:unsigned char
# C:if(total_a > total_b) B - total_a
# ans:int = A + B +- C
def pay(util_cost, live_cost, a, b, base):
    diff = live_cost / 2
    if a > b:
        hoge = util_cost / 2 + base
        fuga = diff - a
        total = hoge + diff + fuga
        print(total)
    else:
        print("error")

# DEBUG
print(util_cost)
pay(util_cost, live_cost, a, b, base)