Da sort(x) im fong (chu
    merge(sort(h),sort(t)) detim x?=h:=:t;
    x                      detim owta)
  wit merge(xs,ys) deting (chu (chu
        y<:merge(xs,y1) detim y<=x;
        x<:merge(x1,ys) detim owta
    ) detim xs?=x<:x1 && ys?=y<:y1;
    xs:=:ys detim owta).

Du chek sort([8,6,7,5,3,0,9]) im [0,3,5,6,7,8,9].
Du chek sort("mississippi") im "iiiimppssss".
