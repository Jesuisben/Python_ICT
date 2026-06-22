import re

print('다음 주소 목록에서 숫자로 시작하는 마지막 상세 주소를 추출해 보세요.')
'''
힌트 
참고용 메타 문자
\d : 숫자 1개를 의미합니다.
\S : white character 문자가 아닌 것들을 의미합니다.

외따옴표는 특수 문자이므로 \' 의 형식으로 사용해야 합니다.

열거한 메타 문자를 적절히 사용하여 처리하면 됩니다.
문자열에서 지정한 문자열을 제거하려면 rstrip() 함수를 사용하면 좋습니다. 
'''

addressList = ["('강원원주시웅비2길8');",
          "('강원도철원군서면와수로181번길7-16');",
          "('강원평창군봉평면태기로68');",
          "('강원강릉시강변로410번길36');"]

regex = "\d\S*\'"
pattern = re.compile(regex)
for address in addressList:
    mymatch = pattern.search(address)
    print(mymatch.group().rstrip("\'"))  # 외따옴표 스트립

# 출력 결과
# 2길8
# 181번길7-16
# 68
# 410번길36