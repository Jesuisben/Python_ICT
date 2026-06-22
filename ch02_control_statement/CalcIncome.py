print("테스트 케이스 01")
salary01 = int(input("월급 입력: "))
print("급여: %d" % salary01)

if salary01 >= 500:
    annualSalary01 = salary01 * 12.0
else:
    annualSalary01 = salary01 * 13.0

print("연봉: %.2f" % annualSalary01)

if annualSalary01 >= 10000:
    tax = annualSalary01 * 0.2
elif annualSalary01 >= 7000:
    tax = annualSalary01 * 0.15
elif annualSalary01 >= 5000:
    tax = annualSalary01 * 0.12
elif annualSalary01 >= 1000:
    tax = annualSalary01 * 0.1
else:
    tax = annualSalary01 * 0

print("세금: %.2f" % tax)

# salary = int(input('월급 입력: '))
# annual_salary = 0 # 연봉
#
# if salary >= 500:
#     annual_salary = 12 * salary
# else:
#     annual_salary = 13 * salary
#
# tax = 0 # 세금
# if annual_salary >= 10000:
#     tax = 0.2 * annual_salary
# elif annual_salary >= 7000:
#     tax = 0.15 * annual_salary
# elif annual_salary >= 5000:
#     tax = 0.12 * annual_salary
# elif annual_salary >= 1000:
#     tax = 0.1 * annual_salary
# else:
#     tax = 0 * annual_salary
#
# print('급여: %d' % salary)
# print('연봉: %.2f' % annual_salary)
# print('세금: %.2f' % tax)
