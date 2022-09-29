#!/bin/bash
cd /sdcard/gokul/optimization/basic
texfot pdflatex main.tex
termux-open main.tex
cd /sdcard/gokul/optimization/basic/codes
python3 matrix.py  