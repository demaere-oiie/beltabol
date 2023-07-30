Du chek 0++2 im 4.
Du chek 1++3 im 7.
Du chek "foo"++"bar" im "foobar".
Du chek 0++[1,2,3] im [0,1,2,3].
Du chek "f"++[1,2,3] im ["f",1,2,3].
Du chek [0,1]++[2,3] im [0,1,2,3].
Du chek (chu [p,h] detim 7?=p++h) im [1,3].
Du chek (chu [h,t] detim "foobar"?=h++t) im ["f","oobar"].
Du chek (chu [h,t] detim [[0],1,2,3]?=h++t) im [[0],[1,2,3]].
Du chek 1++0++2 im 9.
Du chek "foo"++"bar"++"bletch" im "foobarbletch".
Du chek "foo"++"bar"++["bletch"] im ["foo","bar","bletch"].
