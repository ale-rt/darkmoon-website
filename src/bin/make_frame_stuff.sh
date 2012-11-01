#!/bin/bash
# bash shell script
SOURCEDIR='./img/'
DESTDIR='../../img/'
convert -resize 8 $SOURCEDIR/fside-orig.png $DESTDIR/frame-e.png
convert -rotate 90 -resize 8 $SOURCEDIR/fside-orig.png $DESTDIR/frame-s.png
convert -rotate 180 -resize 8 $SOURCEDIR/fside-orig.png $DESTDIR/frame-w.png
convert -rotate 270 -resize 8 $SOURCEDIR/fside-orig.png $DESTDIR/frame-n.png

convert -resize 8 $SOURCEDIR/fcorner-orig.png $DESTDIR/frame-se.png
convert -rotate 90 -resize 8 $SOURCEDIR/fcorner-orig.png $DESTDIR/frame-sw.png
convert -rotate 180 -resize 8 $SOURCEDIR/fcorner-orig.png $DESTDIR/frame-nw.png
convert -rotate 270 -resize 8 $SOURCEDIR/fcorner-orig.png $DESTDIR/frame-ne.png
