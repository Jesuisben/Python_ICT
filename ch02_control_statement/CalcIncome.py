salary = int(input('월급 입력: '))
annual_salary = 0 # 연봉

if salary >= 500:
    annual_salary = 12 * salary
else:
    annual_salary = 13 * salary

tax = 0 # 세금
if annual_salary >= 10000:
    tax = 0.2 * annual_salary
elif annual_salary >= 7000:
    tax = 0.15 * annual_salary
elif annual_salary >= 5000:
    tax = 0.12 * annual_salary
elif annual_salary >= 1000:
    tax = 0.1 * annual_salary
else:
    tax = 0 * annual_salary

print('급여: %d' % salary)
print('연봉: %.2f' % annual_salary)
print('세금: %.2f' % tax)