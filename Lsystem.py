# coding:utf-8
import rhinoscriptsyntax as rs

#************************
# LSystem class
#************************
class LSystem():
    def __init__(self,numIters,startStr,rules,angle,step):
        self.numIters = numIters
        self.startStr = startStr
        self.rules = rules
        self.angle = angle
        self.step = step
        
        self.resultStrs = []
        self.resultStrs.append(self.startStr)
        
        print("numIters={}".format(self.numIters))
        print("startStr={}".format(self.startStr))
        print("rules={}".format(self.rules))
        print("angle={}".format(self.angle))
        print("step={}".format(self.step))
        
        print("---------")
        self.iterations(self.startStr)
        print("---------")
        
        print("resultStrs={}".format(self.resultStrs))
    
    # inputがルールのkeyに適合すればvalに置換してoutputを返す
    # そうじゃなければ、そのままinputをoutputとして返す
    def replace(self,input):
        output = ""
        for key,val in self.rules.items():
            if(input == key):
                output = val
                break
            else:
                output = input
        return output
        
    def replaceProccess(self,oldStr):
        newStr = ""
        for char in oldStr:
            replacedChar = self.replace(char)
            newStr = newStr+replacedChar
        return newStr
        
    def iterations(self,oldStr):
        newStr = ""
        for i in range(self.numIters):
            print("n={0}".format(i))
            newStr = self.replaceProccess(oldStr)
            print("newStr={0}".format(newStr))
            oldStr = newStr
            self.resultStrs.append(newStr)
            
    def draw(self,input,oldPt):
        angle = 0
        num = []  # stack for the brackets
        for char in input:
            if(char == "F"):
                newPt = [0,1,0]
                newPt = rs.VectorRotate(newPt,angle,[0,0,1])
                newPt = rs.VectorScale(newPt,self.step)
                newPt = rs.VectorAdd(newPt,oldPt)
                rs.AddLine(oldPt,newPt)
                oldPt = newPt
            elif(char == "+"):
                angle += self.angle
            elif(char == "-"):
                angle -= self.angle
            elif(char == "["):
                num.append((oldPt, angle))
            elif(char == "]"):
                oldPt, angle = num.pop()
            elif(char == "X"):
                pass
                
                
        

#************************************
# main
#************************************
if __name__ == '__main__':
    # globals
    
#    numIters = 4
#    # ω:初期文字列
#    startStr = 'A'
#    # P:置換規則
#    rules = {}
#    rules['B'] = 'A'
#    rules['A'] = 'AB'
#    # val
#    angle = 90
#    step = 300
    
#    # コッホ曲線
#    numIters = 3
#    # ω:初期文字列
#    startStr = '-F'
#    # P:置換規則
#    rules = {}
#    rules['F'] = 'F+F-F-F+F'
#    # val
#    angle = 90
#    step = 300
    
#    # コッホ島
#    numIters = 3
#    # ω:初期文字列
#    startStr = 'F-F-F-F'
#    # P:置換規則
#    rules = {}
#    rules['F'] = 'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'
#    # val
#    angle = 90
#    step = 300
    
#    # tree
#    numIters = 4
#    # ω:初期文字列
#    startStr = 'F'
#    # P:置換規則
#    rules = {}
#    rules['F'] = 'F[+F]F[-F]F'
#    # val
#    angle = 25.7
#    step = 300
    
    # tree
    numIters = 6
    # ω:初期文字列
    startStr = 'X'
    # P:置換規則
    rules = {}
    rules['X'] = 'F[+X]F[-X]+X'
    rules['F'] = 'FF'
    # val
    angle = 20
    step = 300
    
    # instance
    ls = LSystem(numIters,startStr,rules,angle,step)
    
    # draw
    rs.EnableRedraw(False)
#    ls.draw("FFF-FF+F",[0,0,0],0)
    ls.draw(ls.resultStrs[-1],[0,0,0])
    rs.EnableRedraw(True)