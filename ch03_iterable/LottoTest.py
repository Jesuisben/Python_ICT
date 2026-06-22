import random

lotto = set()
secondno = 0  #  이등 번호

while(len(lotto) < 7):
    su = random.randint(1, 45)
    if(len(lotto) == 6):
        #  1등 번호는 이미 모두 추출된 상태임
        #  2등 번호는 임시로 secondno에 할당해 두도록 합니다.
        secondno = su

    lotto.add(su)
# end while

#  2등 번호를 포함한 7개이므로, remove 메소드를 사용하여 2등 번호를 제거합니다.
lotto.remove(secondno)

print("금주의 로또 번호 : ", end='')
sorted_list = sorted(lotto)
print(sorted_list)
print("2등 번호 : " + str(secondno))