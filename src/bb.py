from errors import disperr, ParsingError
from parser import cooked, engmap, idem, genAST
from semantic import Env, Num, Str
import os

def Eval(src,map,env):
    try:
        genAST(src,map).eval(env)
    except ParsingError as err:
        disperr(src,err)
        return 1
    return 0

prenv = Env(None)
prenv["_ByteTable_"] = Str("".join(chr(n) for n in range(256)))
Eval(os.read(os.open("src/prelude.bb",os.O_RDONLY),2**16),idem,prenv)

usage = lambda n: """
Usage: %s [--help] [--lex] [--boring] [--noprelude] [--test]

    --help       print this text
    --lex        (debug) output the unparsed token stream
    --boring     use english, not Lang Belta, syntax
    --noprelude  don't initialise the environment
    --test       evaluate inline tests ("Du chek" statements)

Until better implemented, takes input from STDIN
""" % n

builtins = """
Da ($)(f,x) im f$x.
Da (|)(x,y) im x|y.
Da (,)(x,y) im x,y.
Da (<)(x,y) im x<y.
Da (<=)(x,y) im x<=y.
Da (==)(x,y) im x==y.
Da (>)(x,y) im x>y.
Da (<:)(x,y) im x<:y.
Da (:>)(x,y) im x:>y.
Da (:=:)(x,y) im x:=:y.
Da (++)(x,y) im x++y.
Da (+)(x,y) im x+y.
Da (-)(x,y) im x-y.
Da (*)(x,y) im x*y.
Da (/)(x,y) im x/y.
Da (@)(x,y) im x@y.
"""

def main(argv):
    if "--help" in argv:
        print usage(argv[0])
        return 0
    blt = Env(prenv if "--noprelude" not in argv else None)
    Eval(builtins,idem,blt)
    env = Env(blt)
    m = idem if "--boring" not in argv else engmap
    s = os.read(0,2**16)
    if "--lex" in argv:
        for t in cooked(s,m):
            print("%s %s" % (t.gettokentype(), t.getstr()))
    env["\0source\0"] = Str(s)
    env["Du chek"] = Num(int("--test" in argv))
    return Eval(s,m,env)

target = lambda *args: main

if __name__=="__main__":
    import sys
    main(sys.argv)
