#!/bin/bash
python3 -m py_compile $PYFILE
chmod +x $PYFILE'c'
cd __pycache__
mv *.pyc "$PYFILE""c"
mv "$PYFILE""c" ..
