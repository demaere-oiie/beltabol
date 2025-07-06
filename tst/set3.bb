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
        h              detim owta).

Da xfold(g,c) im sfold((:=:),g,c).
Da elems im fong xfold(enlist,[]) wit enlist(x) deting [x].
Da smele im fong xfold(single,{}) wit single(x) deting {x}.
    
Du chek sort(elems({3,2,1})) im [1,2,3].

Da land(xs,ys) im chu
    (chu
        x<:land(x1,y1) detim y==x;
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
        
Da sand(xs,ys) im smele(land(sort(elems(xs)),sort(elems(ys)))).
Da sxor(xs,ys) im smele(lxor(sort(elems(xs)),sort(elems(ys)))).
Da sor(xs,ys)  im sxor(sand(xs,ys),sxor(xs,ys)).

Du chek sand({1,2,3,4},{2,4,6,8}) im {2,4}.
Du chek sxor({1,2,3,4},{2,4,6,8}) im {1,3,6,8}.
Du chek sor({1,2,3,4},{2,4,6,8}) im {1,2,3,4,6,8}.
