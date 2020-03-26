#!/bin/sh
export IFS=":"
sort $1 -t : -k 3 | while read a b c d e f; do echo "$a $c,$b"; done

