class Sports:
    def __init__(self, name, entry ):
        self.name = name
        self.entry = entry
                  
    def showInfo(self):
        print('종목 : %s' % ( self.name ))    
        print('엔트리 : %2d명' % ( self.entry ))
 
class BaseBall(Sports):
    def __init__(self, name, entry, hitrate):
        super().__init__(name, entry)
        self.hitrate = hitrate

    def showInfo(self):
        super().showInfo() 
        print('타율  : %f' % ( self.hitrate ))
 
class FootBall(Sports):
    def __init__(self, name, entry, goal):
        super().__init__(name, entry)
        self.goal = goal
        
    def showInfo(self):
        super().showInfo() 
        print('골수  : %d' % ( self.goal ))    
 
base = BaseBall('야구', 9, 0.235)
base.showInfo()
print('-' * 20)
foot = FootBall('축구', 11, 5)
foot.showInfo()
print('-' * 30)