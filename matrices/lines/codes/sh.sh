#!/bin/bash
cd /sdcard/gokul/matrices/lines
texfot pdflatex main.tex
termux-open main.tex
cd /sdcard/gokul/matrices/lines/codes
python3 matrix.py  