// Kelowda we kang gif-peye wit pish ke?
// "how many ways can we make change with casino chips?"

Da we(peyeting,pish) im chu
    1                     detim peyeting==0;
    0                     detim pish==[0];
    we(peyeting,mali)     detim pish?=bik++mali && bik>peyeting;
    we(peyeting,mali)+
    we(peyeting-bik,pish) detim pish?=bik++mali;
    0                     detim owta.

Da pish im [50,20,10,5,2,1,0].

Du chek we(0,pish) im 1.
Du chek we(1,pish) im 1.
Du chek we(5,pish) im 4.
Du chek we(11,pish) im 12.
Du chek we(20,pish) im 41.
Du chek we(50,pish) im 451.
