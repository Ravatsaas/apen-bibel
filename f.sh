#!/bin/sh

./flytt_fotnoter.py "$1" > /tmp/f
mv /tmp/f "$1"
