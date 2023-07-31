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
