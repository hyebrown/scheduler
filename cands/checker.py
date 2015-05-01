#!/cygdrive/c/Python27/python
import sys, random, getopt, re


#Wed:
#PRJ
#Noon
#BFC

#Thurs:
#NiN
#Bling
#CDS
#ANAL

#Saturday Noon   cGame: date:  2         time:  0  team1:  NiNiNinjas    team2:  ToDare
#Saturday 1p     cGame: date:  2         time:  1  team1:  ANAL          team2:  PacRimJob
#Saturday 2p     cGame: date:  2         time:  2  team1:  BlingItOn     team2:  Nooners
#Saturday 3p     cGame: date:  2         time:  3  team1:  CirqueDuSuck  team2:  BFCOC
#Saturday 4p     cGame: date:  2         time:  4  team1:  Kneadmoor     team2:  Goat

#echo "================================"
#echo "     $1 "

#for i in PacRimJob Nooners BFCOC
#do
#	mismatch=`cat $1 | grep Thursday | grep $i | wc -l`
#	echo "$i : $mismatch"
#done

#for i in NiNiNinjas BlingItOn CirqueDuSuck ANAL
#do
#	mismatch=`cat $1 | grep Wednesday | grep $i | wc -l`
#	echo "$i : $mismatch"
#done



def countgames(file,team,day):
	print "iterating over ", team , " and " , day
	gamecount=0
	for line in file:
		if re.search(day,line):
			if re.search(team,line):
				gamecount +=1
				print gamecount
	return gamecount


def main(argv):

	Teams=["PacRimJob","Goat","CirqueDuSuck","ToDare","NiNiNinjas","ANAL","Kneadmoor","BlingItOn","Nooners","BFCOC"]
	Days=["Wednesday","Thursday","Saturday"]
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
		   inputfile = arg
		elif opt in ("-o", "--ofile"):
		   outputfile = arg
	print 'Input file is "', inputfile
	print 'Output file is "', outputfile


	with open(inputfile) as f:
		print countgames(inputfile,"PacRimJob","Wednesdays")
		for team in Teams:
			for day in Days:
				gcount=countgames(f,team,day)
				print team," has ",gcount," games booked on ",day," this season"



	print "got here"
	return



























if __name__ == "__main__":
	main(sys.argv[1:])
