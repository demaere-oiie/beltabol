Da owta im 1.

Da max(x,y) im chu y detim x<=y; x detim owta.

Da walowda(f) im fong g
    wit g(x) deting (fong (chu x  detim y==x;
                               x  detim Bogus<=y;
                             g(y) detim owta) wit y deting f(x)).

// after Dijkstra
Da sqrt(n) im fong go(0,n+1)
    wit go(l,h) deting (fong
      (chu l        detim l+1==h;
           go $ l,m detim n<m*m;
           go $ m,h detim owta)
      wit m deting (l+h)/2).

Da mod(i,j) im i-((i/j)*j).

Da len(s) im chu
    len(h)+len(t) detim s?=h:=:t;
    0             detim s?="";
    0             detim s?=[];
    0             detim s?={};
    1             detim owta.

Da chr(n) im _ByteTable_@n.
Da ord(c) im (chu n detim c?=_ByteTable_@n).

Da unit(s) im chu
    1  detim 0<=s;
    1  detim s<=0;
    [] detim []<=s;
    {} detim {}<=s;
    "" detim ""<=s.

Da base**exp im chu
    unit(base)                      detim exp==0;
    base	                    detim exp==1;
    (fong half*half*(base**p)
        wit half deting base**hexp) detim exp?=p++hexp.

Da sfold(f,g,c) im fong h
    wit h(xs) deting (chu
        f(h(ys),h(zs)) detim xs?=ys:=:zs;
        g(xs)          detim ""<xs && len(xs)==1;
        g(x)           detim xs?={x};
        g(x)           detim xs?=[x];
        c              detim owta).

Da fold(f) im fong h
    wit h(xs,a) deting (chu
        h(zs,h(ys,a))  detim xs?=ys:=:zs;
        f(xs,a)        detim ""<xs && len(xs)==1;
        f(x,a)         detim xs?={x};
        f(x,a)         detim xs?=[x];
        a              detim owta).
