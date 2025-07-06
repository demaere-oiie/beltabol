Da add(n,m) im fong wok(n,m,0)
    wit wok(n,m,c) deting (chu
        c               detim n==0 && m==0;
           wok( c, m,0) detim n==0;
           wok( n, c,0) detim m==0;
        0++wok(n1,m1,0) detim n?=0++n1 && m?=0++m1 && c==0;
        1++wok(n1,m1,0) detim n?=0++n1 && m?=1++m1 && c==0;
        1++wok(n1,m1,0) detim n?=1++n1 && m?=0++m1 && c==0;
        1++wok(n1,m1,0) detim n?=0++n1 && m?=0++m1 && c==1;
        0++wok(n1,m1,1) detim n?=1++n1 && m?=1++m1 && c==0;
        0++wok(n1,m1,1) detim n?=0++n1 && m?=1++m1 && c==1;
        0++wok(n1,m1,1) detim n?=1++n1 && m?=0++m1 && c==1;
        1++wok(n1,m1,1) detim n?=1++n1 && m?=1++m1 && c==1).

Du chek add(3,7) im 10.