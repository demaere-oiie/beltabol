Du chek (fong z
  wit z deting 2*y;
  wit y delowda [x+1,x-1];
  wit x delowda [z+1,z+2];
  wit z deting 0) im [4,0,6,2].

Da iota(n) im chu
    []               detim n<1;
    iota(n-1):>(n-1) detim owta.

Du chek (fong z
    wit z delowda iota(y);
    wit y delowda [4,0,1]) im [0,1,2,3,0].

Du chek (fong z
    wit z deting  iota(y);
    wit y delowda [4,0,1]) im [[0,1,2,3],[],[0]].

Du chek (fong z
    wit w delowda [];
    wit z deting  iota(y);
    wit y delowda [4,0,1]) im [].

Da foo im fong f
    wit f(x) deting x+y;
    wit y delowda [4,5,6].

Du chek (foo@0)(0) im 4.
Du chek (foo@2)(0) im 6.

Du chek (fong ord(c) wit c delowda "foo") im [102,111,111].

Da zip(xs,ys) im chu
    [x,y]<:zip(xt,yt) detim xs?=x<:xt && ys?=y<:yt;
    []                detim owta.

Du chek zip("foobar","bletc") im [["f","b"],["o","l"],["o","e"],
                                  ["b","t"],["a","c"]].

Du chek (fong x:=:y
    wit [x,y] delowda zip("foobar","bletch"))
im ["fb","ol","oe","bt","ac","rh"].

Da map(f) im fong g
    wit g(xs) deting (fong f(x) wit x delowda xs).

Da inc(n) im n+1.

Du chek map(inc) $ iota(3) im [1,2,3].

Da filter(p) im fong g
    wit g(xs) deting (fong x wit p(x) delowda xs).

Da even(n) im chu 1 detim n `mod` 2 == 0.

// du chek filter(even) $ iota(4) im [0,2].
