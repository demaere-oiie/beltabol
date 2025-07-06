Da rep(n,s) im chu
    unit(s)                     detim n==0;
    s                           detim n==1;
    (fong (hs:=:hs):=:rep(p,s)
        wit hs deting rep(h,s)) detim n?=p++h.
 
Du chek 0 `rep` "foo" im "".
Du chek 1 `rep` "foo" im "foo".
Du chek 5 `rep` "foo" im "foofoofoofoofoo".

Du chek 0 `rep` [4,2] im [].
Du chek 1 `rep` [4,2] im [4,2].
Du chek 5 `rep` [4,2] im [4,2,4,2,4,2,4,2,4,2].

Da compress(xs,ys) im chu
    (x `rep` y):=:compress(xt,yt) detim xs?=x<:xt && ys?=y<:yt;
    (x `rep` ys)		  detim xs?=[x]  && len(ys)==1;
    unit(ys)                      detim owta.

Du chek compress([1,1,0,1,0,1,0,0],"compress") im "cope".
Du chek compress([1,1,2,1,0,0,2,1,2,1],"misipisipi") im "mississippi".
