from lexer import cooked, engmap, oper, rsvd
from rply import ParserGenerator
from syntactic import Program, DaIm, DaImalowda, Showxa, Chek
from syntactic import Chu, CDecls, CDecl
from syntactic import Fong, FDecls, FDecl, RDecl
from syntactic import App, OpAND, OpNDX, OpCAT, OpMUL, OpDIV
from syntactic import OpADD, OpSUB, OpLE, OpLT, OpGT, OpEQ
from syntactic import OpCOMMA, OpBAR, OpMATCH, exprOpr
from syntactic import OpSPLICE, OpCONS, OpSNOC, exprNeg
from syntactic import exprList, exprStr, exprId, exprNil

################################################################################
def gram(s):
    vs = s.split('$$')
    prd = vs[0]
    xs = vs[1].split()
    funsrc = "lambda p: {}({})".format(xs[0],
                ",".join("p[{}]".format(n) for n in xs[1:]))
    pg.production(prd)(eval(funsrc))

def Gram(s):
    [gram(l) for l in s.split('\n') if '$$' in l]
################################################################################

idem = lambda p: p

pg = ParserGenerator(list(rsvd.values()) +
                     list(oper.values()) +
                     "OPR NAM LPN RPN LBR RBR STR".split(),
    precedence=[
        ('left', ['SEMIC']),
        ('left', ['UNTE']),
        ('left', ['AND']),
        ('right', ['DOLLAR']),
        ('left', ['BAR']),
        ('left', ['COMMA']),
        ('nonassoc', ['MATCH']),
        ('nonassoc', ['LT', 'LE', 'EQ', 'GT']),
        ('right', ['CONS']),
        ('left', ['SNOC']),
        ('left', ['SPLICE']),
        ('left', ['OPR']),
        ('right', ['CAT']),
        ('left', ['ADD', 'SUB']),
        ('left', ['MUL', 'DIV']),
        ('right', ['LPN']),
        ('left', ['NDX']),
    ])

Gram("""
    start : program             $$ idem 0

    program : statement program $$ Program 0 1
    program : statement         $$ Program 0

    ### Top-level statements #################################

    statement : DA expr IM defn DOT       $$ DaIm 1 3
    statement : DA expr IMALOWDA expr DOT $$ DaImalowda 1 3
    statement : DU CHEK expr IM expr DOT  $$ Chek 2 4 1 5
    statement : SHOWXA defn DOT           $$ Showxa 1

    ### Compound expressions #################################

    defn : CHU cdecls       $$ Chu 1
    defn : FONG expr fdecls $$ Fong 1 2
    defn : expr             $$ idem 0

    cdecls : cdecl SEMIC cdecls $$ CDecls 0 2
    cdecls : cdecl              $$ CDecls 0

    cdecl : expr DETIM expr     $$ CDecl 0 2

    fdecls : rdecls SEMIC fdecls   $$ FDecls 0 2
    fdecls : rdecls                $$ FDecls 0
    rdecls : fdecl UNTE rdecls     $$ RDecl 0 2
    rdecls : fdecl                 $$ idem 0

    fdecl : WIT expr DETING expr   $$ FDecl 1 3
    fdecl : WIT expr DELOWDA expr  $$ FDecl 1 3 2
    fdecl : WIT expr IMALOWDA expr $$ DaImalowda 1 3

    ### Simple expressions ###################################

    expr : expr LPN expr RPN $$ App 0 2
    expr : expr LPN RPN      $$ App 0
    expr : expr DOLLAR expr  $$ App 0 2

    expr : expr SPLICE expr $$ OpSPLICE 0 2
    expr : expr CONS expr   $$ OpCONS 0 2
    expr : expr SNOC expr   $$ OpSNOC 0 2
    expr : expr MATCH expr  $$ OpMATCH 0 2
    expr : expr COMMA expr  $$ OpCOMMA 0 2
    expr : expr BAR expr    $$ OpBAR 0 2
    expr : expr AND expr    $$ OpAND 0 2
    expr : expr NDX expr    $$ OpNDX 0 2
    expr : expr CAT expr    $$ OpCAT 0 2
    expr : expr MUL expr    $$ OpMUL 0 2
    expr : expr DIV expr    $$ OpDIV 0 2
    expr : expr ADD expr    $$ OpADD 0 2
    expr : expr SUB expr    $$ OpSUB 0 2
    expr : expr LE expr     $$ OpLE 0 2
    expr : expr LT expr     $$ OpLT 0 2
    expr : expr GT expr     $$ OpGT 0 2
    expr : expr EQ expr     $$ OpEQ 0 2
    expr : expr OPR expr    $$ exprOpr 0 1 2

    expr : LPN defn RPN     $$ idem 1
    expr : SUB expr         $$ exprNeg 1

    ### Values ###############################################

    expr : LBR expr RBR    $$ exprList 1
    expr : LBR RBR         $$ exprNil
    expr : STR             $$ exprStr 0
    expr : NAM             $$ exprId 0
""")

parser = pg.build()

def genAST(src, map):
    return parser.parse(cooked(src, map))
