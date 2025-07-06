Da Regex imalowda Eps | Lit(c) | Seq(s,t) | Alt(p,q) | Rep(r).

Da or(x,y) im chu 0 detim x?=0 && y?=0; 1 detim owta.
Da zerr(r) im chu
  1                   detim r?=Eps;
  0                   detim r?=Lit(c);
  or(zerr(p),zerr(q)) detim r?=Alt(p,q);
  zerr(s)*zerr(t)     detim r?=Seq(s,t);
  1                   detim r?=Rep(x).

Da seq(s,t) im chu
  t                         detim s?=Eps;
  Seq(u,Seq(v,t))           detim s?=Seq(u,v);
  Seq(s,t)                  detim owta.
Da seqs(rs,t) im chu {seq(r,t)}:=:seqs(rs1,t) detim rs?=r<:rs1; {} detim owta.
Da lit(c,d) im chu {Eps} detim c==d; {} detim owta.
Da seqx(c,s,t) im
  seqs(m1(c,s),t):=:(chu m1(c,t) detim zerr(s)?=1; {} detim owta).
Da m1(c,r) im chu
  {}                        detim r?=Eps;
  lit(c,d)                  detim r?=Lit(d);
  m1(c,p):=:m1(c,q)         detim r?=Alt(p,q);
  seqx(c,s,t)               detim r?=Seq(s,t);
  m1(c,seq(x,Rep(x)))       detim r?=Rep(x);
  {}                        detim owta.
Da match(c,rs) im chu match(c,rs1):=:m1(c,r) detim rs?=r<:rs1; {} detim owta.
Da matches(s,rs) im chu matches(s1,match(t,rs)) detim s?=t<:s1; rs detim owta.

Da anyeps(rs) im chu or(zerr(r),anyeps(ps)) detim rs?=r<:ps; 0 detim owta.
Da req(s,r) im anyeps(matches(s,{r})).

Du chek zerr(Eps) im 1.
Du chek zerr(Lit("a")) im 0.
Du chek zerr(Alt(Eps,Lit("a"))) im 1.
Du chek seqs({Lit("a"),Lit("b")},Lit("c")) im {Seq(Lit("a"),Lit("c")),Seq(Lit("b"),Lit("c"))}.
Du chek lit("a","a") im {Eps}.
Du chek lit("a","b") im {}.
Du chek anyeps({}) im 0.
Du chek anyeps({Eps}) im 1.
Du chek anyeps({Lit("a")}) im 0.
Du chek req("",Eps) im 1.
Du chek req("a",Eps) im 0.
Du chek req("",Lit("a")) im 0.
Du chek req("a",Lit("a")) im 1.
Du chek req("b",Lit("a")) im 0.
Du chek req("",seq(Eps,Eps)) im 1.
Du chek req("a",Alt(Lit("a"),Lit("b"))) im 1.
Du chek req("b",Alt(Lit("a"),Lit("b"))) im 1.
Du chek req("c",Alt(Lit("a"),Lit("b"))) im 0.
Du chek req("ab",seq(Lit("a"),Lit("b"))) im 1.
Du chek req("ac",seq(Lit("a"),Lit("b"))) im 0.
Du chek req("a",seq(Lit("a"),Lit("b"))) im 0.
Du chek req("",Rep(Lit("a"))) im 1.
Du chek req("a",Rep(Lit("a"))) im 1.
Du chek req("aaa",Rep(Lit("a"))) im 1.
Du chek req("aba",Rep(Lit("a"))) im 0.
Du chek req("",Rep(Seq(Lit("a"),Lit("b")))) im 1.
Du chek req("abaababb",Rep(Alt(Lit("a"),Lit("b")))) im 1.
Du chek req("abaacabb",Rep(Alt(Lit("a"),Lit("b")))) im 0.
Du chek req("abc",seq(Seq(Lit("a"),Lit("b")),Lit("c"))) im 1.
Du chek req("abc",Seq(Lit("a"),Seq(Lit("b"),Lit("c")))) im 1.
Du chek req("ab",Rep(Seq(Lit("a"),Lit("b")))) im 1.
Du chek req("ababab",Rep(Seq(Lit("a"),Lit("b")))) im 1.
Du chek req("ababa",Rep(Seq(Lit("a"),Lit("b")))) im 0.
