from rply import LexerGenerator, Token

rsvd = {t:t.upper() for t in """
Da Du Showxa chek chu detim deting fong im imalowda unte wit 
""".split()}

Tab = lambda s: [l.split() for l in s.split('\n') if ' ' in l]

oper = dict(Tab('''
    @   NDX
    *   MUL
    /   DIV
    +   ADD
    -   SUB
    ++  CAT
    <   LT
    <=  LE
    ==  EQ
    >   GT
    :=: SPLICE
    :>  SNOC
    <:  CONS
    ?=  MATCH
    ,   COMMA
    |   BAR
    $   DOLLAR
    &&  AND
    ;   SEMIC
    .   DOT
'''))

lg = LexerGenerator()

for typ,pat in Tab(r'''
    CMT //[^\n]*
    CMT ^#![^\n]*
    STR "[^"]*"
    NAM \([!?$&+*-/,:;<=>|@#%^]+\)
    OPR `[_\w]+`
    LPN \(
    RPN \)
    LBR \[
    RBR \]
    OPR [!?$&+*-/,:;<=>|@#%^]+
    NAM [_\w]+
'''):
    lg.add(typ,pat)

lg.ignore('\s+')
lexer = lg.build()

################################################################################

def cook(t):
    assert isinstance(t,Token)
    if   t.name == 'NAM': t.name = rsvd.get(t.value,'NAM')
    elif t.name == 'OPR': t.name = oper.get(t.value,'OPR')
    return t

xlat = dict(Tab("""
    Please Du
    confirm chek
    Def Da
    Print Showxa
    pick chu
    <- delowda
    when detim
    := deting
    calc fong
    as im
    ::= imalowda
    otherwise owta
    and unte
    where wit
"""))

def engmap(t):
    if t.value in xlat:
        t.name  = 'NAM'
        t.value = xlat[t.value]
    return t

def cooked(s,m):
    for t in lexer.lex(s):
        if t.name != 'CMT':
            yield cook(m(t))
