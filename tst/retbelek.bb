// cf Okasaki, "Red-Black Trees in a Functional Setting", JFP 1999
// https://www.cs.tufts.edu/~nr/cs257/archive/chris-okasaki/redblack99.pdf

Da RetBelek imalowda Kuku() | Not(weting,gosh,val,richa).

Da sh(n) im chu
   ""                        detim n?=Kuku();
   "("++sh(a)++x++sh(b)++")" detim n?=Not("B",a,x,b);
   "<"++sh(a)++x++sh(b)++">" detim n?=Not("R",a,x,b).

Da duimgut(n) im chu
    Not("R",Not("B",a,x,b),y,Not("B",c,z,d))
            detim n?=Not("B",Not("R",Not("R",a,x,b),y,c),z,d);
    Not("R",Not("B",a,x,b),y,Not("B",c,z,d))
            detim n?=Not("B",Not("R",a,x,Not("R",b,y,c)),z,d);
    Not("R",Not("B",a,x,b),y,Not("B",c,z,d))
            detim n?=Not("B",a,x,Not("R",Not("R",b,y,c),z,d));
    Not("R",Not("B",a,x,b),y,Not("B",c,z,d))
            detim n?=Not("B",a,x,Not("R",b,y,Not("R",c,z,d)));
    n                        detim owta.

Da erefo(x,t) im fong dubelek(ef(t))
  wit ef(t) deting (chu
      Not("R",Kuku(),x,Kuku())   detim t?=Kuku();
      duimgut(Not(c,ef(a),y,b))  detim t?=Not(c,a,y,b) && x <  y;
      t                          detim t?=Not(_,_,y,_) && x == y;
      duimgut(Not(c,a,y,ef(b)))  detim t?=Not(c,a,y,b) && x >  y);
  wit dubelek(t) deting (chu Not("B",a,y,b) detim t?=Not(_,a,y,b)).

// (((<(<0>1)2(3)>4(5))6((7)8(9)))W(((X)Y<(Z)a(b)>)c((d)e(f))))
Da gut im "(<((<0>1)2<(3)4(5)>)6((7)8(9))>W<((X)Y<(Z)a(b)>)c((d)e(f))>)".

Du chek (fong sh(efr("0123456789abcdefWXYZ0123"))
  wit efr(xs) deting (chu
    erefo(h,efr(t)) detim xs?=h++t;
    Kuku()          detim owta)) im gut.
