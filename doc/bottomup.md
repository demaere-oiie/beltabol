# Da Beltabol fong but fo gova

This file is a bottom-up introduction to Beltabol, a novel eager functional language.

## Built-in Datatypes and simple Expressions

Beltabol currently has three built-in datatypes: integers, strings, and lists. All are totally ordered, and can either being treated in a basic fashion, operating upon each value as a whole, or (in an advanced fashion) can be further analyzed into parts: integers into bits, strings into strings of length 1, and lists into any datatype.

### Basics of Integers

Beltabol integers, like `0` or `42`, have the usual arithmetic operations with the usual precedence: `+`, `-`, `*`, and `/`. The last is integer division, so `5/2 == 2`.

They are also totally ordered, and have the usual set of relational operators: `<`, `<=`, `==`, `>=`, `>`, and `<>`. The relational operators produce integer `0` for false and integer `1` for true.  Nota Bene: all values, not only integers, can only be compared to values of the same type; all relational operators return 0 if given arguments of distinct types.

Limitation: for the time being, only decimal literals work.

Limitation: in principle, integers are multiple precision; at the current time, they are rpython ints, which wrap at a given bitwidth.

### Basics of Strings

Beltabol strings, like `"foo"` or `"Oye, setara setara!"` can be concatenated with the `++` operator, which is right associative and has precedence just below the arithmetic operators. The empty string is `""` and is the identity for `++`.

Strings are totally ordered in lexicographical order.

Limitation: currently, `ord` and `chr` are defined via a lookup table in the standard prelude, so they only have the printable ASCII range.

Limitation: currently there are no string escapes.

### Basics of Lists

Beltabol lists, like `[]` or `[0, "won", []]`, are sequences of items of any beltabol type. They can also be concatenated with `++`, and as a special case, `item++list` acts as a cons. The empty list is `[]` and is the identity for `++`.

Lists are totally ordered in lexicographical order.

### Advanced Integers

Integers have a substructure of (little-endian) sequences of bits. They can be synthesized using the `<:` cons operator, whose left hand side must be a bit (0 or 1), which is shifted into the least significant place, eg: `0<:4 == 8` and `1<:4 == 5`.

Integers may also be analyzed using the `@` indexing operator, which has a higher precedence than the arithmetic operators, and picks out the bit at that place (`n@0` is the least significant bit of `n`)

### Advanced Strings

Strings have a substructure of sequences of length-1 strings. They can be synthesized using the `<:` cons operator, the `>:` snoc operator, and `:=:`, the splice operator. Cons prepends a length-1 string to the front of the string, snoc appends a length-1 string to the back, and splice concatenates two strings, eg: `"b"<:"elta" == "belta"`; `"belt">:"a" == "belta"`; and `"bel":=:"ta" == "belta"`.

Strings may also be analyzed using the `@` indexing operator, which picks out the length-1 string at that place. (`"foobar"@1` == "o"`)

### Advanced Lists

Lists have a substructure of sequences of any beltabol datatype.  They can be synthesized using the `<:` cons operator, the `>:` snoc operator, and `:=:`, the splice operator, eg: `0<:["won", []] == [0,"won",[]]`; `[0,"won"]:>[] == [0,"won",[]]`; and `[0]:=:["won",[]] == [0,"won",[]]`.

Lists may also be anaylzed using the `@` indexing operator, which picks out the item at that place. (`[0,"won",[]]@2 == []`)

## User-defined Algebraic Datatypes

User-defined algebraic datatypes have an constructor, which is an identifier, and arguments of any Beltabol datatype; eg. in `Ptr(s,n)` `Ptr` is the constructor and `s` and `n` are arguments.

Example:
```
Da RetBelek imalowda Kuku() | Not(weting,gosh,val,richa).

Da sh(n) im chu
   ""                        detim n?=Kuku();
   "("++sh(a)++x++sh(b)++")" detim n?=Not("B",a,x,b);
   "<"++sh(a)++x++sh(b)++">" detim n?=Not("R",a,x,b).
```

Limitation: in principle, the algebraic datatypes are totally ordered, but this is currently unimplemented.

## Compound Expressions

There are two compound expressions, `chu` compounds and `fong` compounds.

```
    defn : CHU {cdecl SEMIC} cdecl
    defn : FONG expr {rdecls SEMIC} rdecls
```

When compound expressions occur as subexpressions of simple expressions, they must be fully parenthesized, eg: `2*(chu 2 detim p; 0 detim owta)`

### Chu

`Chu` is like Lisp's COND; each `cdecl` is of the form `expr DETIM guard` and evaluates the expression whose guard is the first to evaluate to 1.

The match operator, `?=`, which has a low precedence, may be used to extend the expression's environment. It takes a value on its left hand side, and a pattern on its right, and attempts to bind variables in the pattern in such a way as to match the value.

Guards may be composed of multiple clauses, joined by the low-precedence `&&` and operator: `(x \`rep\` ys) detim xs?=[x] && len(ys)==1;`

### Example patterns using the `?=` match operator

Integer matching: `0 detim n?=42;` or `m+mul(h,0++m) detim n?=1++n;`

String matching: `1 detim arg?="-v";` or `len(h)+len(t) detim s?=h:=:t;`

List matching: `0 detim xs?=[];` or `dfs(graph, h++seen, acc:>h, vedi(graph,h):=:t) detim vs?=h++t;`

### Fong

`Fong` is a bit like Lisp's LET; each `rdecl` is of the form `WIT binding DETING expr` where `binding` is bound to the value of `expr`.

```
Du chek (fong cclvi*cclvi
  wit cclvi deting xvi*xvi;
  wit xvi   deting iv*iv;
  wit iv    deting ii*ii;
  wit ii    deting 2)
im 65536.
```

To define functions, `binding` should be of the form `id(arguments...)`, as in the definition of `nawit(y,xs)` following:

```
Da nub(xs) im fong (chu
    h<:nub(nawit(h,t)) detim xs?=h<:t;
    []                 detim owta)
    wit nawit(y,xs) deting (chu
        (chu  nawit(y,t) detim h==y;
           h++nawit(y,t) detim owta) detim xs?=h++t;
         []                          detim owta).
```

In general, what in another language might be written as `let y=z in let v=w in x` would be expressed in Beltabol as `(fong x wit v deting w; wit y deting z)`. Note the change in order!

### Fong/delowda for list comprehensions

Using `delowda` instead of `deting` turns a `fong` compound expression into a list comprehension.

```
Da flatten(xss) im fong x
    wit x  delowda xs;
    wit xs delowda xss.

Du chek flatten([[0],[],[1,2]]) == [0,1,2].
```

In general, what in another language might be written as `[x | y<-z, v<-w]` would be expressed in Beltabol as `(fong x wit v delowda w; wit y delowda z)`. Note the change in order! To produce the effect of a guard, use a `delowda` clause which evaluates to either a length-0 list for failure or length-1 list for success.

### Fong/unte for mutual recursion

Use `unte` between `wit` definitions for mutual recursion:
```
(fong even(4)
  wit even(n) deting (chu 1        detim n==0;
                          odd(n-1) detim owta)
  unte
  wit odd(n) deting (chu 0         detim n==0;
                         even(n-1) detim owta)).
```

### Fong/imalowda for local algebraic types

```
(fong dubik("",eg) == gut
  wit eg         deting [Lit("a"),Ptr(0,5),Lit("b"),Ptr(4,6)];
  wit gut        deting "aaaaaabaabaab";
  wit dubik(a,c) deting (chu
        dubik(a++v  ,              t) detim c?=Lit(v)  ++t;
        dubik(a     ,              t) detim c?=Ptr(s,0)++t;
        dubik(a++a@s,Ptr(s+1,n-1)++t) detim c?=Ptr(s,n)++t;
              a                       detim owta);
  wit Mali       imalowda Lit(v) | Ptr(s,l))

```

## Statements

There are four statements:
```
    statement : DA expr IM defn DOT       $$ DaIm 1 3
    statement : DA expr IMALOWDA expr DOT $$ DaImalowda 1 3
    statement : DU CHEK expr IM expr DOT  $$ Chek 2 4 1 5
    statement : SHOWXA defn DOT           $$ Showxa 1
```

1. `Da ... im ...` binds definitions (at the top level)
2. `Da ... imalowda ...` creates algebraic datatypes
3. `Du chek ... im ...` is an equality test (run with `--test` option)
4. `Showxa ...` is used for print debugging

Limitation: Beltabol currently has no I/O; if streams are ever implemented, then probably `Mesach ...` will provide bytestream output)

```
Da four im 2+2.
Da peano imalowda Zero | Succ(n).
Du chek four im 4.
Showxa Succ(Succ(Zero)).
```

Note that compound expressions need not be parenthesized when occuring as `defn`s in the `Da/im` and `Showxa` statements, eg:

```
Da fak(n) im chu
    n*fak(n-1) detim 1<=n;
    1          detim owta.
```

## Standard prelude

|name|purpose|
|----|-------|
|owta| 1 (True)|
|max(x,y)|**max**imum of **x** and **y**||
|mebi(f)|returns fn returning [**f**(x)] on success and [] on failure|
|walowda(f)|returns fn returning the least fixpoint of **f**(**f**(...**f**(x)...))|
|sqrt(n)|integer square root of **n**||
|mod(i,j)|i **mod** j|
|len(v)|length of **v**alue|
|chr(n)|length-1 string with numeric value **n**||
|ord(c)|numeric value of length-1 string **c**|
|unit(v)|returns empty string or list as **v** is string or list||
|(**)(b,e)|raises int **b**ase to **e**xponent|

## See also

See the [other docs](bb.md) and the [brief introduction](https://drive.google.com/file/d/1zTGjy9KeW4cqagXHlVDwKmcZ1mEz6u-K/view).
