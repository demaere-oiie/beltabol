from errors import Chek
from semantic import Construct, Data, Lambda, Num, Str, PatSyntax
from semantic import Seq, Nil, Id, fresh, getlist, newBrand, List, Clo
from semantic import ListSep, Agg, Box, Env

class Program(Box):
    def __init__(self,s,p=None):
        self.s = s
        self.p = p

    def eval(self,env):
        assert isinstance(self.s,Box)
        self.s.eval(env)
        if self.p is not None:
            assert isinstance(self.p,Box)
            self.p.eval(env)

class DaIm(Box):
    def __init__(self,e,d):
        self.e = e
        self.d = d

    def eval(self,env):
        e = self.e
        if isinstance(e, Id):
            env[e.i] = self.d.eval(env)
        elif isinstance(e, App):
            f = e.f
            assert isinstance(f,Id)
            clo = Lambda(e.x, self.d).eval(env)
            clo.e[f.i] = clo
            env[f.i] = clo

def getalts(o):
    if isinstance(o,OpBAR): return getalts(o.l)+getalts(o.r)
    else: return [o]

class DaImalowda(Box):
    def __init__(self,e,d):
        self.e = e
        self.d = d
        self.lctx = False

    def eval(self,env):
        for a in getalts(self.d):
            if isinstance(a, App):
                i = a.f
                assert isinstance(i,Id)
                env[i.i] = Construct(newBrand(i.i), len(getlist(a.x)))
            elif isinstance(a, Id):
                env[a.i] = Data(newBrand(a.i),[])

class Showxa(Box):
    def __init__(self,e):
        self.e = e

    def eval(self,env):
        assert isinstance(self.e,Box)
        print("SHOWXA %s" % self.e.eval(env).__str__())

class Chu(Box):
    def __init__(self,c):
        self.c = c

    def eval(self,env):
        assert isinstance(self.c,Box)
        return self.c.eval(fresh(env))

class Fong(Box):
    def __init__(self,e,f):
        self.e = e
        self.f = f
        if self.f is not None:
            f = self.f
            assert isinstance(f,FDecls)
            if f.lctx:
                self.rev = f.mkrev(Fong(e,None))

    def eval(self,env):
        assert isinstance(self.e,Box)
        f = self.f
        assert isinstance(f,FDecls)
        env1 = fresh(env)
        if not f.lctx:
            f.eval(env1)
            return self.e.eval(env1)
        else:
            return List(self.rev.reval(env1))

    def reval(self,env):
        y = self.e.eval(env)
        return [y] if y is not None else []

class CDecls(Box):
    def __init__(self,l,ls=None):
        self.l = l
        self.ls = ls

    def eval(self,env):
        if self.l.select(env): return self.l.eval(env)
        if self.ls is None: return None
        env.reset()
        return self.ls.eval(env)

class CDecl(Box):
    def __init__(self,e,p):
        self.e = e
        self.p = p

    def select(self,env):
        assert isinstance(self.p,Box)
        b = self.p.eval(env)
        assert isinstance(b,Num)
        return b.v != 0

    def eval(self,env):
        assert isinstance(self.e,Box)
        return self.e.eval(env)

class FDecls(Box):
    def __init__(self,u,l=None):
        self.u = u
        self.l = l
        self.lctx = False
        if isinstance(u,FDecl):
            self.lctx = self.lctx or u.lctx
        if isinstance(l,FDecls):
            self.lctx = self.lctx or l.lctx

    def eval(self,env):
        if self.l is not None:
            self.l.eval(env)
        self.u.eval(env)

    def mkrev(self,acc):
        if self.l is None:
            return FDecls(self.u,acc)
        else:
            return self.l.mkrev(FDecls(self.u,acc))

    def reval(self,env):
        u = self.u
        assert isinstance(u,FDecl)
        if not u.lctx:
            u.eval(env)
            return self.l.reval(env)
        ll = u.e.eval(env)
        if isinstance(ll,List):
            s = ll.s
        elif isinstance(ll,Str):
            s = [Str(c) for c in ll.s]
        else:
            s = []
        rv = []
        for si in s:
            nenv = Env(env) # or do escape analysis?
            u = self.u
            assert isinstance(u,FDecl)
            u.i.match(si,nenv)
            rv.extend(self.l.reval(nenv))
        return rv


class FDecl(Box):
    def __init__(self,i,e,lctx=None):
        self.i = i
        self.e = e
        self.lctx = lctx is not None

    def eval(self,env):
        i = self.i

        if isinstance(i, Id):
            env[i.i] = self.e.eval(env)
        elif isinstance(i, App):
            clo = Lambda(i.x, self.e).eval(env)
            f = i.f
            assert isinstance(f,Id)
            clo.e[f.i] = clo
            env[f.i] = clo
	elif (  isinstance(i,PatSyntax) or
                isinstance(i,OpNDX) or
                isinstance(i,OpCAT) or
                isinstance(i,OpSPLICE) or
                isinstance(i,OpCONS) or
                isinstance(i,OpSNOC)):
            v = self.e.eval(env)
            if not i.match(v,env):
                print("TENSHA! Refutable binding failed to match!")
                assert False

class RDecl(Box):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        self.lctx = False

    def eval(self,env):
        f = self.l
        assert isinstance(f,FDecl)
        i = f.i
        assert isinstance(i,App)
        id = i.f
        assert isinstance(id,Id)
        self.l.eval(env)
        clo = env[id.i]
        assert isinstance(clo,Clo)
        if self.r is not None:
            self.r.eval(env)
        clo.e = fresh(env)

class App(PatSyntax):
    def __init__(self,f,x=Nil()):
        self.f = f
        self.x = x

    def eval(self,env):
        s = self.x.eval(env)
        return (self.f.eval(env)).apply(s,env)

    def match(self,v,env):
        q = self.f.eval(env)
        if isinstance(q,Construct):
            assert isinstance(v,Data)
            if v.b!=q.b: return False
            subs = getlist(self.x)
            if len(subs)!=q.a: return False
            #for w,s in zp(v.v,subs):
            #    print("%s?=%s %s" % (w,s,match(w,s,env)))
            for i in range(len(v.v)):
                w = v.v[i]
                s = subs[i]
                if not s.match(w,env):
                    return False
            return True
        elif isinstance(q,Clo):
            b = q.apply(v,env)
            if not isinstance(b,Num) or b.v!=1:
                return False
            return self.x.match(v,env)
        return False

    def __str__(self):
        return "%s(%s)" % (self.f,self.x)

class BinOp(Box):
    def __init__(self,l,r):
        self.l = l
        self.r = r

class OpAND(BinOp):
    def eval(self, env):
        ll = self.l.eval(env)
        rr = self.r.eval(env)
        return ll.mul(rr)

class OpNDX(BinOp):
    def eval(self, env):
        return self.l.eval(env).ndx(self.r.eval(env))

    def match(self, v, env):
        q = self.l.eval(env)
        if isinstance(q,List):
            for i in range(len(q.s)):
                if q.s[i].match(v,env) and self.r.match(Num(i),env):
                    return True
            return False
        elif isinstance(q,Str):
            for i in range(len(q.s)):
                if Str(q.s[i]).match(v,env) and self.r.match(Num(i),env):
                    return True
            return False
        elif isinstance(q,Num):
            if not isinstance(v,Num): return False
            if v.v != 0 and v.v != 1: return False
            if v.v == 0 and q.v == -1: return False
            if v.v == 1 and q.v == 0: return False
            i = 0
            while (q.v&(1<<i))>>i != v.v:
                i = i+1
            return self.r.match(Num(i),env)
        return False

class OpCAT(BinOp):
    def eval(self, env):
        return self.r.eval(env).rcat(self.l.eval(env))

    def match(self, v, env):
        if isinstance(v,Str):
            if len(v.s)==0: return False
            return (self.l.match(Str(v.s[0]),env) and
                    self.r.match(Str(v.s[1:]),env))
        elif isinstance(v,List):
            if len(v.s)==0: return False
            l = self.l
            if isinstance(l,List):
                l = len(l.s)
                if len(v.s)<l: return False
                return (self.l.match(List(v.s[:l]),env) and
                        self.r.match(List(v.s[l:]),env))
            else:
                return (self.l.match(v.s[0],env) and
                        self.r.match(List(v.s[1:]),env))
        elif isinstance(v,Num):
            if v.v==0: return False
            return (self.l.match(Num(v.v & 1),env) and
                    self.r.match(Num(v.v // 2),env))
        else:
            assert False

class OpMUL(BinOp):
    def eval(self, env):
        return self.l.eval(env).mul(self.r.eval(env))

class OpDIV(BinOp):
    def eval(self, env):
        return self.l.eval(env).div(self.r.eval(env))

class OpADD(BinOp):
    def eval(self, env):
        return self.l.eval(env).add(self.r.eval(env))

class OpSUB(BinOp):
    def eval(self, env):
        return self.l.eval(env).sub(self.r.eval(env))

class OpLE(BinOp):
    def eval(self, env):
        return self.l.eval(env).le(self.r.eval(env))

class OpLT(BinOp):
    def eval(self, env):
        return self.l.eval(env).lt(self.r.eval(env))

class OpGT(BinOp):
    def eval(self, env):
        return self.l.eval(env).gt(self.r.eval(env))

class OpGE(BinOp):
    def eval(self, env):
        return self.l.eval(env).ge(self.r.eval(env))

class OpEQ(BinOp):
    def eval(self, env):
        return self.l.eval(env).eq(self.r.eval(env))

class OpNE(BinOp):
    def eval(self, env):
        return self.l.eval(env).ne(self.r.eval(env))

class OpCOMMA(ListSep):
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def eval(self, env):
        return Seq(self.l.eval(env),self.r.eval(env))
    def match(self, v, env):
        vv = List(getlist(v))
        pp = List(getlist(Seq(self.l,self.r)))
        return pp.match(vv,env)

class OpBAR(BinOp):
    def eval(self, env):
        l = self.l.eval(env)
        r = self.r.eval(env)
        return Agg(l,r)

class OpMATCH(BinOp):
    def eval(self, env):
        l = self.l
        r = self.r
        v = l.eval(env)
        assert (isinstance(r,PatSyntax) or
                isinstance(r,OpNDX) or
                isinstance(r,OpCAT) or
                isinstance(r,OpSPLICE) or
                isinstance(r,OpCONS) or
                isinstance(r,OpSNOC))
        b = r.match(v,env)
        return Num(int(b))

class OpSPLICE(BinOp):
    def eval(self, env):
        l,r = self.l.eval(env), self.r.eval(env)
        if isinstance(l,Str) and isinstance(r,Str):
            return Str(l.s + r.s)
        elif isinstance(l,List) and isinstance(r,List):
            return List(l.s + r.s)
        return None

    def match(self, v, env):
        if isinstance(v,Str) and len(v.s)>1:
            m = len(v.s)//2
            return (self.l.match(Str(v.s[:m]),env) and
                    self.r.match(Str(v.s[m:]),env))
        elif isinstance(v,List) and len(v.s)>1:
            m = len(v.s)//2
            return (self.l.match(List(v.s[:m]),env) and
                    self.r.match(List(v.s[m:]),env))
        return False

class OpCONS(BinOp):
    def eval(self, env):
        l,r = self.l.eval(env), self.r.eval(env)
        if isinstance(r,List):
            return List([l] + r.s)
        elif isinstance(l,Str) and isinstance(r,Str):
            return Str(l.s + r.s)
        elif isinstance(l,Num) and isinstance(r,Num):
            if l.v == 0 or l.v == 1:
                return Num(2*r.v + l.v)
        return None

    def match(self, v, env):
        if isinstance(v,List) and len(v.s)>1:
            return (self.l.match(v.s[0],env) and
                    self.r.match(List(v.s[1:]),env))
        elif isinstance(v,Str) and len(v.s)>1:
            return (self.l.match(Str(v.s[0]),env) and
                    self.r.match(Str(v.s[1:]),env))
        elif isinstance(v,Num) and v.v>0:
            return (self.l.match(Num(v.v & 1),env) and
                    self.r.match(Num(v.v // 2),env))
        return False

class OpSNOC(BinOp):
    def eval(self, env):
        l,r = self.l.eval(env), self.r.eval(env)
        if isinstance(l,List):
            return List(l.s + [r])
        elif isinstance(l,Str) and isinstance(r,Str):
            return Str(l.s + r.s)
        return None
    def match(self, v, env):
        if isinstance(v,List) and len(v.s)>1:
            return (self.l.match(List(v.s[:-1]),env) and
                    self.r.match(v.s[-1],env))
        elif isinstance(v,Str) and len(v.s)>1:
            return (self.l.match(Str(v.s[:-1]),env) and
                    self.r.match(Str(v.s[-1]),env))
        return False

def mid(s):     
    l = len(s)-1
    assert l>0
    return s[1:l]

def exprOpr(l,o,r):
    s = o.getstr()
    if s[0]=='`': f = Id(mid(s))
    else:         f = Id("(%s)" % (s,))
    return App(f,Seq(l,r))

def exprNeg(p):
    return OpSUB(Num(0),p)

def exprList(p):
    return List(getlist(p))

def exprStr(p):
    return Str(mid(p.getstr()))

def exprId(p):
    s = p.getstr()
    if s[0] in "0123456789": return Num(int(s))
    return Id(s)

def exprNil():
    return List([])
