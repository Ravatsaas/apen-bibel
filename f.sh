#!/bin/sh

for i in "$@"
do
	echo "$i"
	./flytt_fotnoter.py "$i" > /tmp/f
	mv /tmp/f "$i"
done
