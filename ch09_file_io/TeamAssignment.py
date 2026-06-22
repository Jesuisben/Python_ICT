import random

# 파일에서 명단 읽기
with open("names.txt", "r", encoding="utf-8") as file:
    people = [line.strip() for line in file.readlines()]

# 인원 수 확인
if len(people) != 28:
    raise ValueError("파일에 정확히 28명의 이름이 있어야 합니다.")

# 랜덤 섞기
random.shuffle(people)

# 6개의 조로 배정 (5,5,5,5,4,4명)
group_sizes = [5, 5, 5, 5, 4, 4]
groups = []
start = 0

for size in group_sizes:
    groups.append(people[start:start + size])
    start += size

import time

# 결과 출력
for i, group in enumerate(groups, 1):
    time.sleep(3)  # 3초 대기
    print(f'조 {i}:')
    for person in group:
        print(f'  - {person}')
    print()  # 조 간 구분을 위해 한 줄 띄우기
