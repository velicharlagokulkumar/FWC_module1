#!/bin/bash
cd /sdcard/gokul/matrices/conics
texfot pdflatex main.tex
termux-open main.tex
cd /sdcard/gokul/matrices/conics/codes
python3 matrix.py  