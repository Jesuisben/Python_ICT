import somefolder.character.CharacterModule

newstring = "사과/딸기/감/배/오렌지"
result = somefolder.character.CharacterModule.character_split(newstring)
print(result)

sports = ["야구", "축구", "농구", "배구"]
symbol = "@"
result = somefolder.character.CharacterModule.list_join(sports, symbol)
print(result)

from somefolder.character.CharacterModule import character_split
newstring = "아메리카노/아이스라떼/카푸치노"
result = character_split(newstring)
print(result)

from somefolder.character.CharacterModule import list_join
sports = ["야구", "축구", "농구", "배구"]
symbol = "/"
result = list_join(sports, symbol)
print(result)