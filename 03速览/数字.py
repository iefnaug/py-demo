from decimal import Decimal, ROUND_UP, getcontext, ROUND_DOWN, ROUND_FLOOR

print(5 / 2)
print(5 // 2)
print(5 % 2)
print(int(2.33))
print(float(2.33))
print(2 ** 3)

"""
模式,说明,1.5 ➔,2.5 ➔,-1.5 ➔
ROUND_HALF_EVEN,银行家舍入法（默认）。舍入到最接近的偶数。减少累积误差。,2,2,-2
ROUND_HALF_UP,四舍五入。我们数学课上学的那种。,2,3,-2
ROUND_CEILING,向正无穷方向舍入。,2,3,-1
ROUND_FLOOR,向负无穷方向舍入。,1,2,-2
ROUND_UP,远离 0 的方向舍入。,2,3,-2
ROUND_DOWN,靠近 0 的方向舍入（截断）。,1,2,-1
"""
print(getcontext())
print(Decimal(3.22))
print(Decimal('3.22'))
print(float(Decimal('3.22')))

print(Decimal('2.121').quantize(Decimal('0.00'), rounding=ROUND_UP))
print(Decimal('2.126').quantize(Decimal('0.00'), rounding=ROUND_DOWN))
print(Decimal('2.126').quantize(Decimal('0.00'), rounding=ROUND_FLOOR))

getcontext().prec = 4
print(Decimal('3.1415926535') + Decimal('2.7182818285'))