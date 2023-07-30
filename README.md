# BELTABOL

Inspired by some [The Expanse](https://en.wikipedia.org/wiki/The_Expanse_(TV_series)#Language) fanfiction, BELTABOL is an [rpython](https://rpython.readthedocs.io/en/latest/)-powered eager functional [completely incomprehensible](https://www.mcmillen.dev/language_checklist.html) programming language, making it possible to write code such as:

```
Da gcd im fong max,walowda(wok)
    wit wok(n,m) deting (chu
        (n,m-n) detim n<m;
        (n-m,m) detim n>m;
        (n,  m) detim owta).
```
or:
```
Da filter(p) im fong g
    wit g(x) deting (chu
        g(h):=:g(t) detim x?=h:=:t;
        x           detim x?=[i] && p(i);
        x           detim p(x);
        unit(x)     detim owta).
```

(in fact, the higher-order function `walowda` from the first example is written in BELTABOL itself, and provided in the standard prelude.)

For those who really must have it, a `--boring` flag to the (interpreter)[doc/terp.md] allows the use of english keywords:
```
Print "aaaaaabaabaab".
Print calc expand("",eg)
  where eg          := [Lit("a"),Ptr(0,5),Lit("b"),Ptr(4,6)];
  where expand(a,c) := (pick
        expand(a++v  ,              t) when c?=Lit(v)  ++t;
        expand(a     ,              t) when c?=Ptr(s,0)++t;
        expand(a++a@s,Ptr(s+1,n-1)++t) when c?=Ptr(s,n)++t;
               a                       when otherwise);
  where Comp        ::= Lit(v) | Ptr(s,l).

```

## goals

The main idea is to play with rpython and [rply](https://rply.readthedocs.io/en/latest/); in fact the staged nature of rpython worked out very nicely, as one can use full python metagprogramming to aid with the grammar/ast interface (cf the [parser](https://github.com/demaere-oiie/beltabol/blob/4acd8c2364740ef7a4d8ae466dc7aadedd4bad46/src/parser.py#L51-L115) source), while sticking with rpython for the (tree walking) interpreter results in ~50 times performance improvement compared to cpython.

## current state

Minimal [documentation](doc/bb.md) is available. While the language is expected to be extended, the semantics of the currently implemented fragment should stay reasonably constant.

## dependencies

- [rply](https://rply.readthedocs.io/en/latest/additional/license.html) and
- [rpython](https://rpython.readthedocs.io/en/latest/)
