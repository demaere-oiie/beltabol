// "pattern matching" ere BELTABOL
Du chek (fong dubik("",eg) == gut
  wit eg         deting [Lit("a"),Ptr(0,5),Lit("b"),Ptr(4,6)];
  wit gut        deting "aaaaaabaabaab";
  wit dubik(a,c) deting (chu
        dubik(a++v  ,              t) detim c?=Lit(v)  ++t;
        dubik(a     ,              t) detim c?=Ptr(s,0)++t;
        dubik(a++a@s,Ptr(s+1,n-1)++t) detim c?=Ptr(s,n)++t;
              a                       detim owta);
  wit Mali       imalowda Lit(v) | Ptr(s,l)) im 1.
