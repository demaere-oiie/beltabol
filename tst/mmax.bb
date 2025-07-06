Da mmin(x,y) im chu
  x     detim x==y;
  Balk  detim owta.

Da mmax(x,y) im chu
  x     detim y==Balk;
  y     detim x==Balk;
  x     detim x==y;
  Bogus detim owta.

Da merge(xs,ys) im chu
    (chu
        y<:merge(xs,y1) detim y<=x;
        x<:merge(x1,ys) detim owta
    ) detim xs?=x<:x1 && ys?=y<:y1;
    xs:=:ys detim owta.

Da sort(x) im chu
    merge(sort(h),sort(t)) detim x?=h:=:t;
    x                      detim owta.

Da sfold(f,g,c) im fong h
    wit h(xs) deting (chu
        f(h(ys),h(zs)) detim xs?=ys:=:zs;
        g(x)           detim xs?={x};
        g(x)           detim xs?=[x];
        c              detim owta).

Da xfold(g,c) im sfold((:=:),g,c).
Da elems im fong xfold(enlist,[]) wit enlist(x) deting [x].
Da smele im fong xfold(single,{}) wit single(x) deting {x}.

Du chek smele([(1:2),(3:4)]) im {1:2,3:4}.

Da land(xs,ys) im chu
    (chu
        x<:land(x1,y1) detim x==y;
           land(x1,ys) detim x<=y;
           land(xs,y1) detim owta
    ) detim xs?=x<:x1 && ys?=y<:y1;
    [] detim owta.

Da lxor(xs,ys) im chu
    (chu
           lxor(x1,y1) detim x==y;
        x<:lxor(x1,ys) detim x<=y;
        y<:lxor(xs,y1) detim owta
    ) detim xs?=x<:x1 && ys?=y<:y1;
    xs:=:ys detim owta.

Da dand(xs,ys) im smele(land(sort(elems(xs)),sort(elems(ys)))).
Da dxor(xs,ys) im smele(lxor(sort(elems(xs)),sort(elems(ys)))).
Da dor(xs,ys)  im dxor(dand(xs,ys),dxor(xs,ys)).

Da d0 im {1:2,3:4,5:6}.
Da d1 im {1:1,3:4,7:8}.

Da rev(xs) im chu
  rev(zs):=:rev(ys) detim xs?=ys:=:zs;
  xs                detim owta.

Du chek dand(d0,d1) im {3:4}.
Du chek dxor(d0,d1) im {1:2,5:6,1:1,7:8}.
Du chek dor(d0,d1)  im {3:4,1:2,5:6,1:1,7:8}.
