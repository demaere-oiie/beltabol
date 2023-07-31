from rply.token import BaseBox

class Box(BaseBox):
    _attrs_ = []

class PatSyntax(Box):
    def match(self,v,env): 
        return False

class Nil(PatSyntax):
    def __init__(self):
        pass

    def eval(self,env):
        return self

    def apply(self,other,env):
        return other

    def match(self,other,env):
        return isinstance(other,Nil)

    def eq(self,other):
        return Num(1 if isinstance(other,Nil) else 0)

class ListSep(Box):
    pass

class Seq(ListSep):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        return Seq(self.l.eval(env), self.r.eval(env))

    def apply(self,other,env):
        t = self.r.apply(other,env)
        return self.l.apply(t,env) if t is not None else t

    def match(self,other,env):
        if not isinstance(other,Seq): return False
        ss = getlist(self)
        vv = getlist(other)
        if len(ss)!=len(vv): return False
        for i in range(len(ss)):
            x = ss[i]
            y = vv[i]
            if not x.match(y,env):
                return False
        return True

    def eq(self,other):
        x = getlist(self)
        y = getlist(other)
        if len(x) != len(y): return Num(0)
        for i in range(len(x)):
            if x[i].eq(y[i]).v==0:
                return Num(0)
        return Num(1)

    def __str__(self):
        return "%s,%s" % (self.l,self.r)

class Agg(Box):
    def __init__(self,l,r):
        self.l = l
        self.r = r

class Bogus(Box):
    pass

def getlist(o):
    if isinstance(o,ListSep): return getlist(o.l)+getlist(o.r)
    if isinstance(o,Nil):   return []
    else: return [o]

def commasep(xs):
    if not xs: return ""
    if len(xs)==1: return xs[0].__str__()
    h = len(xs)//2
    return "%s,%s" % (commasep(xs[:h]),commasep(xs[h:]))

class Data(Box):
    def __init__(self,b,v):
        self.b = b
        self.v = v

    def le(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b > other.b: return Num(0)
        if self.b < other.b: return Num(1)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==1: return Num(0)
        return Num(1)

    def lt(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b > other.b: return Num(0)
        if self.b < other.b: return Num(1)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==1: return Num(0)
        return Num(0)

    def ge(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b > other.b: return Num(1)
        if self.b < other.b: return Num(0)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            if x.lt(y).v==1: return Num(0)
            if x.gt(y).v==1: return Num(1)
        return Num(1)

    def gt(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b > other.b: return Num(1)
        if self.b < other.b: return Num(0)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            if x.lt(y).v==1: return Num(0)
            if x.gt(y).v==1: return Num(1)
        return Num(0)

    def eq(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b != other.b: return Num(0)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            b = x.eq(y)
            assert isinstance(b,Num)
            if b.v==0:
                return Num(0)
        return Num(1)

    def ne(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b != other.b: return Num(1)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            b = x.eq(y)
            assert isinstance(b,Num)
            if b.v==0:
                return Num(1)
        return Num(0)

    def __str__(self):
        if len(self.v)==0: return brands.d[self.b]
        return "%s(%s)" % (brands.d[self.b],commasep(self.v))
         

class Construct(Box):
    def __init__(self,b,a):
        self.b = b
        self.a = a

    def eval(self,env):
        return self

    def apply(self,other,env):
        l = getlist(other)
        if len(l) == self.a: return Data(self.b,l)
        elif self.a == 1:    return Data(self.b,[other])
        else:                return None

    def __str__(self):
        if self.a==0: return brands.d[self.b]
        return "{%s/%d}" % (brands.d[self.b],self.a)

class Clo(Box):
    def __init__(self,c,e):
        self.c = c
        self.e = e

    def apply(self,other,env):
        frm = self.c.a
        env = fresh(self.e)
        if frm.match(other,env): return self.c.e.eval(env)
        else:                    return None

class Lambda(Box):
    def __init__(self,a,e):
        self.a = a
        self.e = e

    def eval(self,env):
        return Clo(self,fresh(env))

class List(PatSyntax):
    def __init__(self,s):
        self.s = s

    def rcat(self,other):
        if isinstance(other,List):
            return List(other.s+self.s)
        else:
            return List([other]+self.s)

    def match(self,v,env):
        if not isinstance(v,List): return False
        if len(self.s)!=len(v.s): return False
        for i in range(len(self.s)):
            x = self.s[i]
            y = v.s[i]
            if not x.match(y,env):
                return False
        return True

    def ndx(self,other):
        assert isinstance(other,Num)
        return self.s[other.v]

    def le(self,other):
        if not isinstance(other,List): return Num(0)
        for i in range(len(self.s)):
            x = self.s[i]
            if i>=len(other.s): return Num(0)
            y = other.s[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==1: return Num(0)
        return Num(1)

    def lt(self,other):
        if not isinstance(other,List): return Num(0)
        if len(self.s)==0:
            if len(other.s)==0: return Num(0)
            return Num(1)
        for i in range(len(self.s)):
            x = self.s[i]
            if i>=len(other.s): return Num(0)
            y = other.s[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==0: return Num(0)
        return Num(0)

    def ge(self,other):
        if not isinstance(other,List): return Num(0)
        for i in range(len(self.s)):
            x = self.s[i]
            if i>=len(other.s): return Num(1)
            y = other.s[i]
            if x.gt(y).v==1: return Num(1)
            if x.lt(y).v==1: return Num(0)
        return Num(1)

    def gt(self,other):
        if not isinstance(other,List): return Num(0)
        for i in range(len(self.s)):
            x = self.s[i]
            if i>=len(other.s): return Num(1)
            y = other.s[i]
            if x.gt(y).v==1: return Num(1)
            if x.lt(y).v==1: return Num(0)
        return Num(0)

    def eq(self,other):
        if not isinstance(other,List): return Num(0)
        if len(self.s) != len(other.s): return Num(0)
        for i in range(len(self.s)):
            x = self.s[i]
            y = other.s[i]
            if x.eq(y).v==0: return Num(0)
        return Num(1)

    def ne(self,other):
        if not isinstance(other,List): return Num(0)
        if len(self.s) != len(other.s): return Num(1)
        for i in range(len(self.s)):
            x = self.s[i]
            y = other.s[i]
            if x.eq(y).v==1: return Num(0)
        return Num(1)

    def eval(self,env):
        return List([x.eval(env) for x in self.s])

    def __str__(self):
        return "List(%s)" % ([x.__str__() for x in self.s],)

class Str(PatSyntax):
    def __init__(self,s):
        self.s = s

    def rcat(self,other):
        assert isinstance(other,Str)
        return Str(other.s+self.s)

    def ndx(self,other):
        assert isinstance(other,Num)
        return Str(self.s[other.v])

    def le(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s<=other.s else Num(0)

    def lt(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s<other.s else Num(0)

    def ge(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s>=other.s else Num(0)

    def gt(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s>other.s else Num(0)

    def eq(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s==other.s else Num(0)

    def ne(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s!=other.s else Num(0)

    def eval(self,env):
        return self

    def match(self,v,env):
        return isinstance(v,Str) and self.s==v.s

    def __str__(self):
        return "Str(%s)" % (self.s,)

class Num(PatSyntax):
    def __init__(self,v):
        self.v = v

    def eval(self,env):
        return self

    def match(self,v,env):
        return isinstance(v,Num) and self.v==v.v

    def ndx(self,other):
        assert isinstance(other,Num)
        return Num(1 if self.v & (1<<other.v) else 0)

    def rcat(self,other):
        if isinstance(other,Num) and other.v in (0,1):
            return Num(2*self.v+other.v)
        else:
            assert False

    def mul(self,other):
        assert isinstance(other,Num)
        return Num(self.v * other.v)

    def div(self,other):
        assert isinstance(other,Num)
        return Num(self.v // other.v)

    def sub(self,other):
        assert isinstance(other,Num)
        return Num(self.v - other.v)

    def add(self,other):
        assert isinstance(other,Num)
        return Num(self.v + other.v)

    def le(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v<=other.v else Num(0)

    def lt(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v<other.v else Num(0)

    def ge(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v>=other.v else Num(0)
    def gt(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v>other.v else Num(0)

    def eq(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v==other.v else Num(0)

    def ne(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v!=other.v else Num(0)

    def __eq__(self, other):
        return isinstance(other,Num) and self.v == other.v

    def __str__(self):
        return "Num(%d)" % (self.v,)

class Id(PatSyntax):
    def __init__(self,i):
        self.i = i
        assert isinstance(self.i,str)

    def eval(self,env):
        return env.get(self.i,None)

    def match(self,v,env):
        if self.i == "_": return True
        elif self.i in brands.d.values():
            q = self.eval(env)
            assert isinstance(q,Data)
            return isinstance(v,Data) and v.b==q.b and len(v.v)==0
        else:
            env[self.i] = v
            return True
    
    def __str__(self):
        return "Id(%s)" % (self.i,)

class Env(object):
    def __init__(self,prev):
        self.d = {"\0kludge":Nil()}
        self.p = prev

    def get(self, key, default):
        if key in self.d:
            return self.d[key]
        if self.p is None:
            return default
        return self.p.get(key,default)

    def reset(self):
        self.d.clear()

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, val):
        self.d[key] = val

def fresh(env):
    return Env(env)

class Brands:
    def __init__(self,i):
        self.i = i
        self.d = dict()

    def next(self,name):
        self.i += 1
        self.d[self.i] = name
        return self.i

brands = Brands(2000)
    
def newBrand(s):
    return brands.next(s)

