#!/usr/bin/env bb

// Wa 'fokeshowng' ere BELTABOL.
Da gcd(n,m) im chu
    gcd(n,m-n) detim n<m;
    gcd(n-m,m) detim n>m;
    max(n,m)   detim owta.

Du chek gcd(6*7,5*6) im 6.
