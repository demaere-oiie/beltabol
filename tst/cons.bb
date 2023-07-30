Du chek "foo":=:"bar" im "foobar".
Du chek [0,1]:=:[2,3] im [0,1,2,3].
Du chek (chu r detim "foobar"?=l:=:r) im "bar".
Du chek (chu r detim [0,1,2,3]?=l:=:r) im [2,3].
Du chek 1<:2 im 5.
Du chek "f"<:"oobar" im "foobar".
Du chek [0]<:[1,2,3] im [[0],1,2,3].
Du chek "f"<:[1,2,3] im ["f",1,2,3].
Du chek (chu [p,h] detim 4?=p<:h) im [0,2].
Du chek (chu t detim "foobar"?=h<:t) im "oobar".
Du chek (chu h detim [[0],1,2,3]?=h<:t) im [0].
Du chek (chu t detim [[0],1,2,3]?=h<:t) im [1,2,3].
Du chek (chu [h,t] detim [[0],1,2,3]?=h<:t) im [[0],[1,2,3]].
Du chek "fooba":>"r" im "foobar".
Du chek [0,1,2]:>[3] im [0,1,2,[3]].
Du chek [0,1,2]:>"r" im [0,1,2,"r"].
Du chek (chu h detim "foobar"?=h:>t) im "fooba".
Du chek (chu [h,t] detim [0,1,2,[3]]?=h:>t) im [[0,1,2],[3]].
Du chek 0<:1<:[2,3] im [0,1,2,3].
Du chek [0,1]:>2:>3 im [0,1,2,3].
Du chek 0<:[1,2]:>3 im [0,1,2,3].
