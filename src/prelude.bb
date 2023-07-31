Da owta im 1.

Da max(x,y) im chu y detim x<=y; x detim owta.

Da mebi(f) im fong g
   wit g(x) deting (fong f(w)
      wit w delowda [x]).

Da walowda(f) im fong g
    wit g(x) deting (fong (chu x  detim y==[];
                               x  detim y==[x];
                           g(y@0) detim owta) wit y deting mebi(f)(x)).

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
    1             detim owta.

Da chr(n) im _ByteTable_@n.
Da ord(c) im (chu n detim c?=_ByteTable_@n).

Da unit(s) im chu
    [] detim []<=s;
    "" detim ""<=s.

Da (**)(base,exp) im chu
    1                               detim exp==0;
    base	                    detim exp==1;
    (fong half*half*(base**p)
        wit half deting base**hexp) detim exp?=p++hexp.
