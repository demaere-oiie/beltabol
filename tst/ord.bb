Du chek 0<0 im 0.
Du chek 0<1 im 1.
Du chek 1<0 im 0.
Du chek 1<1 im 0.
Du chek 0<=0 im 1.
Du chek 0<=1 im 1.
Du chek 1<=0 im 0.
Du chek 1<=1 im 1.
Du chek 0==0 im 1.
Du chek 0==1 im 0.
Du chek 1==0 im 0.
Du chek 1==1 im 1.
Du chek ""<"" im 0.
Du chek ""<"a" im 1.
Du chek ""<"b" im 1.
Du chek "a"<"" im 0.
Du chek "a"<"a" im 0.
Du chek "a"<"b" im 1.
Du chek "b"<"" im 0.
Du chek "b"<"a" im 0.
Du chek "b"<"b" im 0.
Du chek ""<="" im 1.
Du chek ""<="a" im 1.
Du chek ""<="b" im 1.
Du chek "a"<="" im 0.
Du chek "a"<="a" im 1.
Du chek "a"<="b" im 1.
Du chek "b"<="" im 0.
Du chek "b"<="a" im 0.
Du chek "b"<="b" im 1.
Du chek ""=="" im 1.
Du chek ""=="a" im 0.
Du chek "a"=="b" im 0.
Du chek "b"=="b" im 1.
Du chek []<[] im 0.
Du chek []<[1] im 1.
Du chek []<[2] im 1.
Du chek [1]<[] im 0.
Du chek [1]<[1] im 0.
Du chek [1]<[2] im 1.
Du chek [2]<[] im 0.
Du chek [2]<[1] im 0.
Du chek [2]<[2] im 0.
Du chek []<=[] im 1.
Du chek []<=[1] im 1.
Du chek []<=[2] im 1.
Du chek [1]<=[] im 0.
Du chek [1]<=[1] im 1.
Du chek [1]<=[2] im 1.
Du chek [2]<=[] im 0.
Du chek [2]<=[1] im 0.
Du chek [2]<=[2] im 1.
Du chek []==[] im 1.
Du chek []==[0] im 0.
Du chek [0]==[1] im 0.
Du chek [1]==[1] im 1.

// in order to obtain a total order, constructors increase left to right
Da foo imalowda Bar(a,b) | Bletch(c).
Du chek Bar(0,0) < Bar(0,0) im 0.
Du chek Bar(0,0) < Bar(0,1) im 1.
Du chek Bar(0,0) < Bletch(0) im 1.
Du chek Bar(0,0) < Bletch(1) im 1.
Du chek Bar(0,1) < Bar(0,0) im 0.
Du chek Bar(0,1) < Bar(0,1) im 0.
Du chek Bar(0,1) < Bletch(0) im 1.
Du chek Bar(0,1) < Bletch(1) im 1.
Du chek Bletch(0) < Bar(0,0) im 0.
Du chek Bletch(0) < Bar(0,1) im 0.
Du chek Bletch(0) < Bletch(0) im 0.
Du chek Bletch(0) < Bletch(1) im 1.
Du chek Bletch(1) < Bar(0,0) im 0.
Du chek Bletch(1) < Bar(0,1) im 0.
Du chek Bletch(1) < Bletch(0) im 0.
Du chek Bletch(1) < Bletch(1) im 0.
Du chek Bar(0,0) <= Bar(0,0) im 1.
Du chek Bar(0,0) <= Bar(0,1) im 1.
Du chek Bar(0,0) <= Bletch(0) im 1.
Du chek Bar(0,0) <= Bletch(1) im 1.
Du chek Bar(0,1) <= Bar(0,0) im 0.
Du chek Bar(0,1) <= Bar(0,1) im 1.
Du chek Bar(0,1) <= Bletch(0) im 1.
Du chek Bar(0,1) <= Bletch(1) im 1.
Du chek Bletch(0) <= Bar(0,0) im 0.
Du chek Bletch(0) <= Bar(0,1) im 0.
Du chek Bletch(0) <= Bletch(0) im 1.
Du chek Bletch(0) <= Bletch(1) im 1.
Du chek Bletch(1) <= Bar(0,0) im 0.
Du chek Bletch(1) <= Bar(0,1) im 0.
Du chek Bletch(1) <= Bletch(0) im 0.
Du chek Bletch(1) <= Bletch(1) im 1.

Du chek 0 <= "a" im 0.
Du chek 0 >  "a" im 0.
Du chek "a" <= [0] im 0.
Du chek "a" >  [0] im 0.
Du chek [0] <= Bletch(0) im 0.
Du chek [0] >  Bletch(0) im 0.
