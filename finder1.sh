#!/bin/bash


COUNTER=0
#for i in {1..50000000}
while [ 1 -eq 1 ]
do
	COUNTER=$[$COUNTER +1]
	i=`date +%s`
	./scheduler.py > ./cands/cands$1/schedule.$i
	foocount=`cat ./cands/cands$1/schedule.$i | grep -c foo`
	if [ $foocount -gt 1 ]
	then
		#echo .
		if [ $foocount -lt 8 ]
		then
			echo $COUNTER " " $foocount
		else
			echo .
		fi
		rm ./cands/cands$1/schedule.$i
	else
		echo $COUNTER " " $foocount
	fi
done

