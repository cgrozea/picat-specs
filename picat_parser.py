#!/usr/bin/env python3
import lark
import sys
with open("picat.ebnf") as f:
    g=f.read()
l=lark.Lark(g,debug=False)
fn=sys.argv[1]
with open(fn) as f:
    text=f.read()
try:
    ax=l.parse(text+" ")
    print("parsed OK")
except Exception as e:
    print("Error:\n",e)
