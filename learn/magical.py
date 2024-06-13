int_num = 50
float_num = 7.5
str_val = 'abc'

print(int_num.__mul__(str_val))
# NotImplemented
print(str_val.__mul__(int_num))
# abcabcabcabcabcabcabcabcabcabca...
print(int_num.__mul__(float_num))
# NotImplemented
print(float_num.__mul__(int_num))
# 375.0
print(help(bool.__abs__))
