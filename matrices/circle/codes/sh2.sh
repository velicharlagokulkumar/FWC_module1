#!/bin/bash
cd /sdcard/gokul/matrices/circle
texfot pdflatex main.tex
termux-open main.tex
cd /sdcard/gokul/matrices/circle/codes
python3 matrix.py  