// Kosaraju's algorithm for finding strongly connected components

// Ancillary fn's
Da nub(xs) im fong s2l,l2s $ xs
    wit s2l(xs) deting (chu h<:s2l(t) detim xs?=h<:t; [] detim owta);
    wit l2s(xs) deting (chu h<:l2s(t) detim xs?=h<:t; {} detim owta).

Da flatten(xss) im fong x
    wit x  delowda xs;
    wit xs delowda xss.

// represent graph as list of nodes and their neighbors
Da reverse_graph(graph) im fong collect(vertices(graph),res)
     wit res deting (fong [t,s]
        wit t      delowda ts;
        wit [s,ts] delowda graph).

Da vertices(graph) im fong nub(flatten(es))
    wit es deting (fong [s,t]
        wit t      delowda ts;
        wit [s,ts] delowda graph).

Da collect(vs,es) im fong [v, find_edges(v,es)]
    wit v delowda vs;
    wit find_edges(v,es) deting (fong w
        wit w     delowda (chu [t] detim v==s; [] detim owta);
        wit [s,t] delowda es).

Da vedi(graph, s) im chu
    []         detim graph?=[];
    ns         detim graph?=h++t && h?=[v,ns] && v==s;
    vedi(t, s) detim graph?=h++t.

// Kosaraju's algo
Da dfs(graph, seen, acc, vs) im chu
    dfs(graph,    seen, acc   , t) detim vs?=h++t && seen?=h<:_ ;
    dfs(graph, h++seen, acc:>h, vedi(graph,h):=:t)
                                   detim vs?=h++t;
    seen:acc                       detim owta.

Da pass(graph, vs) im fong wok(graph, {}, [], vs)
    wit wok(graph, seen, acc, vs) deting (chu
      acc   detim vs?=[];
     (fong wok(graph, ds, acc1, t)
        wit acc1  deting (chu acc detim da?=[]; [da]++acc detim owta);
        wit ds:da deting dfs(graph, seen, [], [h]))
	    detim vs?=h++t).

Da kosaraju(g) im pass(reverse_graph(g),flatten(pass(g,vertices(g)))).
    
Da example_graph im [[1,[2,3]], [2,[4]], [3,[4]], [4,[1]], [5,[6]], [6,[5]]].
Du chek kosaraju(example_graph) im [[1,4,2,3],[5,6]].
Du chek kosaraju([[0,[1]],[1,[2]],[2,[0]]]) im [[0,2,1]].
Du chek kosaraju([[0,[1]],[1,[2]],[2,[3]]]) im [[3],[2],[1],[0]].
