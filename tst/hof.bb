Da map(f) im fong g
    wit g(x) deting (chu
        g(h):=:g(t) detim x?=h:=:t;
        []          detim x?=[];
        [f(i)]      detim x?=[i];
        []          detim x?="";
        [f(x)]      detim owta).

Da reduce(f) im fong g
    wit g(x) deting (chu
        f(g(h),g(t)) detim x?=h:=:t;
        i            detim x?=[i];
        x            detim owta).

Da filter(p) im fong g
    wit g(x) deting (chu
        g(h):=:g(t) detim x?=h:=:t;
        x           detim x?=[i] && p(i);
        x           detim p(x);
        unit(x)     detim owta).

Da even(n) im chu 1 detim n?=0++_; 0 detim owta.

Du chek map(ord)("foobar") im [102,111,111,98,97,114].
Du chek reduce((:=:)) $ map(chr) $ map(ord) $ "foobar" im "foobar".
Du chek filter(even) $ map(ord) $ "foobar" im [102,98,114].

Da vowel(s) im chu 1 detim s?="aeiou"@_; 0 detim owta.

Du chek vowel("f") im 0.
Du chek vowel("o") im 1.

Du chek filter(vowel) $ "foobar" im "ooa".

Da false(n) im 0.

Du chek filter(false) $ "foobar" im "".
