SOURCES = src/bb.py src/errors.py src/lexer.py src/parser.py\
          src/semantic.py src/syntactic.py

EXE = bin/bb

$(EXE): $(SOURCES)
	rpython src/bb.py
	mkdir -p bin
	mv bb-c bin/bb

test:
	sh regress

test-c: $(EXE)
	sh regress-c

clean:
	rm -f src/*.pyc
	rm -f $(EXE)
	[ -d bin ] && rmdir bin || touch .
