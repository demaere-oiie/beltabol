// after https://www.fmjlang.co.uk/fmj/interpreter.pdf Fig. 6

Da zip(xs,ys) im chu
    (x:y)<:zip(xt,yt) detim xs?=x<:xt && ys?=y<:yt;
    []                detim owta.

Da rev(xs) im chu
    x<:rev(xh)  detim xs?=xh:>x;
    xs          detim owta.

Du chek rev([]) im [].
Du chek rev([0,1,2]) im [2,1,0].

Da pascal(n) im chu
    []    detim n<1;
    [[1]] detim n==1;
    (fong [pk]++ps
        wit pk deting (fong x+y wit x:y delowda zip(pj,rev(pj)));
        wit pj deting 0++ps@0;
        wit ps deting pascal(n-1))
          detim owta.

Du chek pascal(0) im [].
Du chek pascal(1) im [[1]].
Du chek pascal(5) im [
    [1,4,6,4,1],
     [1,3,3,1],
      [1,2,1],
       [1,1],
        [1]
    ].
