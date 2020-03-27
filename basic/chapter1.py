print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('010', '9740', '2999', sep='-')
print('jihwan', 'gmail.com', sep='@')
print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()
print()


# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()
print('Learn Python', file=sys.stdout)

# format 사용(d : 3, s : 'python', f : 3.1412323)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()
# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()
# %f
print('%f' % (3.14232555555342))
print('%1.8f' % (3.14232555555342))

print('{:f}'.format(3.14232555555342))
print('%06.2f' % (3.14232555555342))
print('{:06.2f}'.format(3.14232555555342))
