#!/bin/sh

LABEL=`cat $1`

convert -background 'rgb(242, 242, 242)' -fill black \
-font Courier -pointsize 42 \
label:"$LABEL" tmp.png

#convert -size 1656x250 -background white -fill black \
#-gravity Center -extent 1676x260 
#label:"what what what what what what what what" test.png

