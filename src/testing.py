from rply import Token
from semantic import Box, Num, Str

def index(s,c):
        n=0
        while n<len(s) and s[n]!=c:
            n += 1
        return n

class Chek(Box):
    def __init__(self,x,y,c,d):
        self.x = x
        self.y = y
        assert isinstance(c,Token)
        self.alpha = c.getsourcepos().lineno
        self.omega = d.getsourcepos().lineno

    def prlines(self,src,a,o):
        assert isinstance(src,Str)
        s=src.s
        n=1
        while n<a:
            s=s[index(s,'\n')+1:]
            n=n+1
        while n<o:
            t = s[:index(s,'\n')]
            print("> %s" % (t,))
            s=s[index(s,'\n')+1:]
            n=n+1

    def eval(self,env):
        b = env.get("Du chek",Num(0))
        assert isinstance(b,Num)
        if not b.v:
            return
        assert isinstance(self.x,Box)
        assert isinstance(self.y,Box)
        xv = self.x.eval(env)
        yv = self.y.eval(env)
        b = xv.eq(yv)
        assert isinstance(b,Num)
        if not b.v:
            if self.alpha==self.omega:
                print("Chek na gut: %d" % (self.alpha,))
            else:
                print("Chek na gut: %d-%d" % (self.alpha,self.omega))
            self.prlines(env["\0source\0"],self.alpha,self.omega+1)
            print(xv.__str__())
            print(yv.__str__())
