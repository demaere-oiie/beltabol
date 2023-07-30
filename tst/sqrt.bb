Da sqrt(n) im fong go(n,0,n+1)
    wit go(n,l,h) deting (fong
      (chu h          detim l+1==h;
           go $ n,l,m detim n<=m*m;
           go $ n,m,h detim owta)
      wit m deting (l+h)/2).

Du chek sqrt(0) im 1.
Du chek sqrt(1) im 1.
Du chek sqrt(4) im 2.
Du chek sqrt(9) im 3.
Du chek sqrt(16) im 4.
Du chek sqrt(17) im 5.
