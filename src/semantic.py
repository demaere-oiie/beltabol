from rply.token import BaseBox

class Box(BaseBox):
    _attrs_ = []

    def le(self,other):
        if isinstance(self,Balk): return Num(1)
        if isinstance(other,Bogus): return Num(1)
        return self.xle(other)

    def ge(self,other):
        return other.le(self)

    def lt(self,other):
        return Num(int(self.le(other).v>other.le(self).v))

    def gt(self,other):
        return other.lt(self)

    def eq(self,other):
        return self.le(other).mul(other.le(self))

    def ne(self,other):
        if not isinstance(self, type(other)): return Num(0)
	return Num(1-self.eq(other).v)

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

    def match(self,v,env):
        return isinstance(v,Nil)

class Null(PatSyntax):
    def __init__(self):
        pass

    def eval(self,env):
        return self

    def apply(self,other,env):
        return self

    def match(self,v,env):
        return isinstance(v,Null)

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

    def xle(self,other):
        if not isinstance(other,Seq): return Num(0)
        if self.l.lt(other.l).v == 1: return Num(1)
        if self.l.le(other.l).v == 0: return Num(0)
        if self.r.le(other.r).v == 1: return Num(1)
        return Num(0)

    def __str__(self):
        return "%s,%s" % (self.l.__str__(),self.r.__str__())

class Agg(Box):
    def __init__(self,l,r):
        self.l = l
        self.r = r

class Pair(PatSyntax):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        return self

    def apply(self,other,env):
        return Bogus()

    def xle(self,other):
        if not isinstance(other,Pair): return Num(0)
        if other.l.lt(self.l).v == 1: return Num(1)
        if self.l.eq(other.l).v == 0: return Num(0)
        if self.r.le(other.r).v == 1: return Num(1)
        return Num(0)

    def __str__(self):
        return "%s: %s" % (self.l.__str__(), self.r.__str__())

class Bogus(Box):
    def __str__(self):
       return "Bogus"

    def xle(self,other):
        return Num(0)

class Balk(Box):
    def __str__(self):
        return "Balk"

    def xle(self,other):
        return Num(1)

def getlist(o):
    if isinstance(o,ListSep): return getlist(o.l)+getlist(o.r)
    if isinstance(o,Nil):   return []
    else: return [o]

def getset(o):
    if isinstance(o,ListSep): return getset(o.l)+getset(o.r)
    if isinstance(o,Null):   return []
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

    def eval(self,env):
        return self

    def xle(self,other):
        if not isinstance(other,Data): return Num(0)
        if self.b > other.b: return Num(0)
        if self.b < other.b: return Num(1)
        for i in range(len(self.v)):
            x = self.v[i]
            y = other.v[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==1: return Num(0)
        return Num(1)

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
    def __init__(self,c,e,n):
        self.c = c
        self.e = e
        self.n = n

    def xle(self,other):
        if not isinstance(other,Clo): return Num(0)
        return self.c.eq(other.c).mul(self.e.eq(other.e))

    def apply(self,other,env):
        return Bogus()

    def xpply(self,other,env):
        frm = self.c.a
        env = fresh(self.e)
        #print("%s(%s)" % (self.n,other.__str__()))
        if frm.match(other,env): return self.c.e.eval(env)
        else:                    return None

    def __str__(self):
        return "{Clo:%s}" % (self.n,)

class Lambda(Box):
    def __init__(self,a,e,n):
        self.a = a
        self.e = e
        self.b = newBrand("(lambda)")
        self.n = n

    def xle(self,other):
        if not isinstance(other,Lambda): return Num(0)
        if self.b==other.b: return Num(1)
        return Num(0)

    def eval(self,env):
        return Set([Clo(self,fresh(env),self.n)])

class Set(PatSyntax):
    def __init__(self,s):
        self.s = s

    def canon(self):
        return self.eval(Env(None))

    def rcat(self,other):
        if isinstance(other,Set):
            return Set(other.s+self.s).eval(Env(None))
        else:
            return Set([other]+self.s).eval(Env(None))

    def eval(self,env):
        t = []
        for x in self.s:
            y = x.eval(env)
            f = True
            if isinstance(y,Pair) and isinstance(y.r,Balk):
                for z in t:
                    if isinstance(z,Pair) and y.l.eq(z.l).v: f = False
            else:
                for z in t:
                    if y.eq(z).v: f = False
            if f: t = t+[y]
        return Set(t)

    def ndx(self,other):
        for x in self.s:
            if isinstance(x,Pair) and x.l.eq(other).v==1:
                return x.r
        return Bogus()

    def xle(self,other):
        if not isinstance(other,Set): return Num(0)
        for t in self.s:
          b = False
          for u in other.s:
            if t.eq(u).v: b = True
          if b == False:
            return Num(0)
        return Num(1)

    def match(self,v,env):
        if isinstance(v,Set) and len(v.s)==1 and len(self.s)==1:
            return self.s[0].match(v.s[0],env)
        return self.eq(v).v == 1

    def apply(self,other,env):
        def isect(x,y):
            if x is None: return y
            if y is None: return x
            if x==y: return x
            if isinstance(x,Num) and isinstance(y,Num):
                if x.le(y).v == 1: return x
                else:              return y
            return None
        t = None
        for x in self.s:
            if isinstance(x,Pair):
                print "Pair"
                if x.l.eq(other).v==1:
                    print "Match"
                    u = x.r
                    t = isect(t,u)
            elif isinstance(x,Clo):
                u = x.xpply(other,env)
                t = isect(t,u)
            else:
                print x
                return Bogus()
        if t is None: t=Bogus()
        return t


    def __str__(self):
        return "{%s}" % (",".join([x.__str__() for x in self.s]),)

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

    def xle(self,other):
        if not isinstance(other,List): return Num(0)
        for i in range(len(self.s)):
            x = self.s[i]
            if i>=len(other.s): return Num(0)
            y = other.s[i]
            if x.lt(y).v==1: return Num(1)
            if x.gt(y).v==1: return Num(0)
        return Num(1)

    def eval(self,env):
        return List([x.eval(env) for x in self.s])

    def __str__(self):
        return "%s" % ([x.__str__() for x in self.s],)

class Str(PatSyntax):
    def __init__(self,s):
        self.s = s

    def rcat(self,other):
        assert isinstance(other,Str)
        return Str(other.s+self.s)

    def ndx(self,other):
        assert isinstance(other,Num)
        return Str(self.s[other.v])

    def xle(self,other):
        if not isinstance(other,Str): return Num(0)
        return Num(1) if self.s<=other.s else Num(0)

    def eval(self,env):
        return self

    def match(self,v,env):
        return isinstance(v,Str) and self.s==v.s

    def __str__(self):
        return "\"%s\"" % (self.s,)

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

    def xle(self,other):
        if not isinstance(other,Num): return Num(0)
        return Num(1) if self.v<=other.v else Num(0)

    def __eq__(self, other):
        return isinstance(other,Num) and self.v == other.v

    def __str__(self):
        return "%d" % (self.v,)

class Id(PatSyntax):
    def __init__(self,i):
        self.i = i
        assert isinstance(self.i,str)

    def eval(self,env):
        r = env.get(self.i,None)
        if r is None:
            print("NULL %s" % (self.i,))
        return r

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

    def eq(self,other):
        if len(self.d)!= len(other.d): return Num(0)
        for k,v in self.d.items():
            if other.d[k] != v: return Num(0)
        return Num(1)

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

