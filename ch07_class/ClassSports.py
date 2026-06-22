class Sports:
    def __init__(self, name, entry, info):
        self.name = name
        self.entry = entry
        self.info = info
        
    def showinfo(self):
        print('종목 : {}'.format(self.name))
        print('엔트리 : {}'.format(self.entry))
        print('평균 실적 : {}'.format( self.info ))

baseball = Sports('야구', 9, 0.235)
baseball.showinfo()

print('-' * 20)

football = Sports('축구', 11, 5.0)
football.showinfo()