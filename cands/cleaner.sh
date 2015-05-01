#!/bin/bash

mypath=cands$1
foocount=$2

if [ $foocount -eq 5 ]
then
	mkdir $mypath/1
	mkdir $mypath/2
	mkdir $mypath/3
	mkdir $mypath/4
else
	ls -1 $mypath | head -600 | while read i ; 
	do
		filefoocount=`grep -c foo $mypath/$i`
		if [ $filefoocount -eq $foocount ]
		then
			echo "count $filefoocount :moving $mypath/$i to $mypath/$foocount/"
			mv $mypath/$i $mypath/$foocount/
		fi
	done 
fi
