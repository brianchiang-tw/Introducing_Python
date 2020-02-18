n = 42
f = -7.03
s = 'string cheese'

# 42 -7.030000 string cheese
print('%d %f %s'% (n, f, s) )

# align to the right
#        42  -7.030000 string cheese
print('%10d %10f %10s'%(n, f, s) )

# align to the right with sign
#       +42  -7.030000 string cheese
print('%+10d %+10f %+10s'%(n, f, s) )

# align to the left
# 42         -7.030000  string cheese
print('%-10d %-10f %-10s'%(n, f, s))

# align to the right, with maximal character width is 4
#      0042    -7.0300       stri
print('%10.4d %10.4f %10.4s'%(n, f, s) )

# align to the left, with maximal character width is 4
# 0042 -7.0300 stri
print('%.4d %.4f %.4s'%(n, f, s) )

# align width by argument
#      0042    -7.0300       stri
print('%*.*d %*.*f %*.*s'%( 10, 4, n, 10, 4, f, 10 ,4 ,s) )


##########################################

# 42 -7.03 string cheese
print('{} {} {}'.format(n, f, s) )

# -7.03 string cheese 42
print('{2} {0} {1}'.format(s, n, f) )

# 42 -7.03 string cheese
print('{n} {f} {s}'.format( n = 42, f = -7.03, s= 'string cheese') )

d = { 'n':42, 'f':-7.03, 's': 'string cheese'}
# 42 -7.03 string cheese other
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other') )

# 42 -7.030000 string cheese
print('{0:d} {1:f} {2:s}'.format( n, f, s) )

# 42 -7.030000 string cheese
print('{n:d} {f:F} {s:s}'.format( n=42, f=-7.03, s='string cheese') )

#         42  -7.030000 string cheese
print('{0:10d} {1:10f} {2:10s}'.format( n, f, s) )

# align to the right
#         42  -7.030000 string cheese
print('{0:>10d} {1:>10f} {2:>10s}'.format( n, f, s) )

# align to the left
# 42         -7.030000  string cheese
print('{0:<10d} {1:<10f} {2:<10s}'.format( n, f, s) )

#    42     -7.030000  string cheese
print('{0:^10d} {1:^10f} {2:^10s}'.format( n, f, s) )

# padding
# !!!!!!BIG SALE!!!!!!
print('{0:!^20s}'.format('BIG SALE'))