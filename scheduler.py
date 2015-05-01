#!/cygdrive/c/Python27/python
import sys
import random
random.seed()

#designate Saturday weeks:
#"week" of opening day
opener=1
#"week" of jamboree
jambo=7
#WTF is this?
byegame=4
#week of Festival of Losers
FoL=10
#game number from week of FoL
FoLgamenum=3
unbooked=-1
nopref=-1
ignoreprefs=0
loopFail=0
loopcount=0
lastWeekofSeason=10

#error counters
catastrophic=0
prefvariance=0

class Game:
	'Common base class for all games in season'
	# day: 0=Wed 1=Thurs 2=Sat 3=bye
	# time: 0=Early|noon 1=Late|one 2=two 3=three 4=four 5=bye 

	def __init__(self,day,time):
		self.date=day
		self.time=time
		self.t1=unbooked
		self.t1name="foooooo"
		self.t2=unbooked
		self.t2name="foooooo"

	def displayGame(self):
		print "Game: date: ", self.date,"	time: ", self.time," team1: ", self.t1name,"	team2: ", self.t2name
	
	def setTeam1(self,mytnum,myteam):
		if (( self.t1 != -1 ) and (self.t1 != 10)):
			print "cGame: ERROR: team 1 is already booked: ",self.t1
			return
		else:
			#print "cGame: setting team1 to: [",myteam,"]"
			self.t1=mytnum
			self.t1name=myteam
			#print "cGame: team1: [",self.t1,"]"
			#print "cGame: team1 is now set to: [",self.t1,"]"

	def setTeam2(self,tnum,team):
		if (( self.t2 != unbooked ) and (self.t2 != 10)):
			print "cGame: ERROR: team 2 is already booked: ",self.t2
			return
		else:
			#print "cGame: setting team2 to: [",team,"]"
			self.t2=tnum
			self.t2name=team
			#print "cGame: team2 is now set to: [",self.t2,"]"

class Week:
	'Common base class for all weeks in season'

	def __init__(self,weeknum):
		self.week=weeknum
		self.bookedgames=0
		#print "cWeek: my week: ",self.week," opener: ",opener," jambo: ",jambo
		if ((self.week != opener) and (self.week != jambo)):
			#print "cWeek: creating normal week number: ",self.week
			self.game=[Game(0,0),Game(0,1),Game(1,0),Game(1,1),Game(3,5)];
		else:
			#print "cWeek: creating special saturday number: ",self.week
			self.game=[Game(2,0),Game(2,1),Game(2,2),Game(2,3),Game(2,4)];

	def resetbookedGamesCount(self):
		self.bookedgames = 0

	def incrbookedGamesCount(self):
		self.bookedgames += 1

	def getbookedGamesCount(self):
		return self.bookedgames

	def refreshbookingCount(self):
		week.resetbookedGamesCount()
		for agame in range(0,len(self.game)):
			if (week.game[agame].t1 == nopref):
				self.incrbookedGamesCount()
			if (week.game[agame].t2 == nopref):
				self.incrbookedGamesCount()
#		print "cWeek.refreshbookingCount: " , self.week , "bookedgames = " , self.bookedgames


	def displayWeek(self):
		if ((self.week != opener) and (self.week != jambo) and (self.week != lastWeekofSeason)):
			print "******************************************"
			#print "week : ", self.week
			if (self.week == 0 ):
				humRead="Wednesday May 28 && Thursday May 29"
			elif (self.week == 1):
				humRead="Opening Day"
			elif (self.week == 2):
				humRead="Wednesday June 4 && Thursday June 5"
			elif (self.week == 3):
				humRead="Wednesday June 11 && Thursday June 12"
			elif (self.week == 4):
				humRead="Wednesday June 18 && Thursday June 19"
			elif (self.week == 5):
				humRead="Wednesday June 25 && Thursday June 26"
			elif (self.week == 6):
				humRead="Wednesday July 2 && Thursday July 3"
			elif (self.week == 7):
				humRead="Jamboree"
			elif (self.week == 8):
				humRead="Wednesday July 9 && Thursday July 10"
			elif (self.week == 9):
				humRead="Wednesday July 16 && Thursday July 17"
			else:
				print "shouldn't be here in the branching but there you are..."
	
			print "schedule for week: ",humRead
			for thisgame in range(0,len(self.game)):
				if ( thisgame == 0 ):
					sys.stdout.write('Wednesday 7p	')
				elif ( thisgame == 1 ):
					sys.stdout.write('Wednesday 8p	')
				elif ( thisgame == 2 ):
					sys.stdout.write('Thursday 7p	')
				elif ( thisgame == 3 ):
					sys.stdout.write('Thursday 8p	')
				elif ( thisgame == 4):
					sys.stdout.write('Bye		')
				else:
					print "something wonky this way comes... thisgame == ",thisgame
				self.game[thisgame].displayGame()
		elif (self.week == lastWeekofSeason):
			print "******************************************"
			#print "week : ", self.week
			humRead="Wednesday July 23 && Thursday July 24"
			print "schedule for week: ",humRead
			for thisgame in range(0,len(self.game)):
				if ( thisgame == 0 ):
					sys.stdout.write('Wednesday 7p	')
				elif ( thisgame == 1 ):
					sys.stdout.write('Wednesday 8p	')
				elif ( thisgame == 2 ):
					sys.stdout.write('Thursday 7p	')
				elif ( thisgame == 3 ):
					sys.stdout.write('Bye1		')
				elif ( thisgame == 4):
					sys.stdout.write('Bye2		')
				else:
					print "something wonky this way comes... thisgame == ",thisgame
				self.game[thisgame].displayGame()
		else:
			print "******************************************"
			#print "week : ", self.week
			if (self.week == jambo):
				humRead="Jamboree"
			elif (self.week == 1 ):
				humRead="Opening Day"
			else:
				print "shouldn't be here but there you are..."
				
			print "schedule for week: ",humRead
			for thisgame in range(0,len(self.game)):
				if ( thisgame == 0 ):
					sys.stdout.write('Saturday Noon	')
				elif ( thisgame == 1 ):
					sys.stdout.write('Saturday 1p	')
				elif ( thisgame == 2 ):
					sys.stdout.write('Saturday 2p	')
				elif ( thisgame == 3 ):
					sys.stdout.write('Saturday 3p	')
				elif ( thisgame == 4):
					sys.stdout.write('Saturday 4p	')
				else:
					print "something wonky this way comes... thisgame == ",thisgame
				self.game[thisgame].displayGame()


	def checkBye(self):
		if (self.week == opener) or (self.week == jambo):
			# this is opener or jambo - no byes
			return 0
		elif (self.game[4].t1 == unbooked):
			#team 1 bye slot available
			return 1
		elif (self.game[4].t2 == unbooked):
			#team 2 bye slot available
			return 2
		elif (self.week == lastWeekofSeason):
			if (self.game[FoLgamenum].t1 == team10.tnum):
				return 1
			elif (self.game[FoLgamenum].t2== team10.tnum):
				return 2
		else:
			#no slots available
			return 0

class Team:
	'Common base class for all teams in league'
	'day of week pref: -1=none 1=Wed 2=Thurs'
	'bye pref: -1=none else =week in season <=11'
	'time pref: 0=early 1=late -1=none'

	teamnum=-1

	def __init__(self,teamname,daypref,byepref,timepref):
		self.opponents=[0,1,2,3,4,5,6,7,8,9,10]
		self.openweeks=[0,1,2,3,4,5,6,7,8,9,10]
		self.gamesplayed=0
		self.byes=0
		self.name=teamname
		self.dpref=daypref
		self.bpref=byepref
		self.tpref=timepref
		Team.teamnum += 1
		self.tnum=Team.teamnum
		self.opponents.remove(self.tnum)
		if (self.tnum != FoL):
			self.opponents.remove(FoL)

	def displayTeam(self):
		print "======================================="
		print "team name is: ", self.name
		print "team num is: ", self.tnum
		print "day pref is: ", self.dpref
		print "time of day pref is: ", self.tpref
		print "bye pref is: ", self.bpref
		print "opponents: ", self.opponents
		print "unscheduled weeks: ", self.openweeks
		print "total team count is: ", Team.teamnum

	def incrGamesPlayed(self):
		self.gamesplayed += 1

	def incrBye(self,ispref):
		if (self.byes == 2):
			print "cTeam.incrBye: ERROR: byes already maxed out for: ",self.name
			return
		else:
			print "cTeam.incrBye: current byes: ",self.byes
			self.byes += 1
			print "cTeam.incrBye: incremented byes: ",self.byes
			if (ispref == 1):
				self.bpref = nopref
			if (self.byes ==2):
				self.bpref = nopref

	def checkBye(self):
		print "cTeam.checkBye: self.byes: ", self.byes
		if (self.byes < 2):
			print "bcTeam.checkBye: yes remain"
			return 0
		elif (self.byes == 2):
			print "bcTeam.checkBye: yes maxed"
			return 1
		else:
			print "tcTeam.checkBye: oo many byes booked. how'd we get here?"
			return 2

	def checkWeek(self,weeknum):
		if ( self.openweeks.count(weeknum) == 0 ):
			#booked
			return 1
		else:
			#not booked
			return 0

	def bookWeek(self,weeknum):
		if ( self.checkWeek(weeknum) == 1):
			print "cTeam.bookWeek: Week ",weeknum," is already booked for: ",self.name
			return
		print "cTeam.bookWeek: removing week: ",weeknum," from team scheduling availability. Team: ", self.name
		self.openweeks.remove(weeknum)
		#self.incrGamesPlayed()
	
	def checkOpponent(self,tnum):
		print "cTeam.checkOpponent: checking availability of opponent: ",tnum
		print "cTeam.checkOpponent: available opponents: ",self.opponents
		if ( self.opponents.count(tnum) == 0 ):
			#opponent already booked)
			print "cTeam.checkOpponent: ",self.opponents.count(tnum),"already booked "
			return 1
		else:
			#opponent not yet booked
			print "cTeam.checkOpponent: ",self.opponents.count(tnum),"not yet booked " 
			return 0
	
	#mark an opponent as booked (and have them book me as well)
	def bookOpponent(self,opponent):
		print "cTeam.bookOpponent: opponent is type: ",type(opponent)
		if (self.checkOpponent(opponent.tnum) == 1):
			print "cTeam.bookOpponent: something went awry: team number: ",opponent.tnum," has already been booked"
			return
		self.opponents.remove(opponent.tnum)
		if (opponent.checkOpponent(self.tnum) == 0):
			opponent.bookOpponent(self)
	

def bookGame(team,week,gamenum,gslot,isbyepref):
#takes a team obj, a week obj, a gamenum (number of game in week), a gslot (home or away for game), and if the bye being booked was a preferred bye (0=no 1=yes)
#DOES NOT VERIFY THAT OPPONENT IS VALID zzzzzzzzzzzzzzzzzz this seems bad
# returns 0 if success
# returns 1 if fail

#handles bookkeeping by:
	# setting that team to play in that game that week
	# marking that week booked for that team
	# incrementing the bye counter if this booking is for a bye
	#book game

	print "bookGame: entering bookGame for gamenum: [",gamenum,"]"," for team: [",team.name,"]"," on week: [",week.week,"] in game slot: ",gslot
	print "bookGame: gamenum == ",gamenum, "is bye? ",byegame

	#if game is a bye
	if ((((week.week != opener ) and (week.week != jambo )) and (gamenum == byegame)) or ((gamenum == FoLgamenum ) and (week.week == lastWeekofSeason))):
		print "bookGame: week is a bye: "
		print "bookGame: perhaps date: " , week.week ," == opener? ", opener , " or jambo? " , jambo
		print "bookGame: gamenum is 4? ", gamenum , " if 3 and still booking, then this is probably last week of Season aka week 10"
		#check for available slots
		#if slot 1 free
		if ((gslot == 1) and ((week.game[gamenum].t1 == unbooked) or (week.game[gamenum].t1 == FoL))):
			# book game
			week.game[gamenum].setTeam1(team.tnum,team.name)
			# incrBye
			team.incrBye(isbyepref)
			team.bookWeek(week.week)
			print "bookGame: successfully booked bye: [",gamenum,"]"," for team: [",team.name,"]"," on week: [",week.week,"] in game slot: ",gslot
			return 0
		#elif slot 2 free
		elif ((gslot == 2) and ((week.game[gamenum].t2 == unbooked) or (week.game[gamenum].t2 == FoL))):
			# book game
			week.game[gamenum].setTeam2(team.tnum,team.name)
			# incrBye
			team.incrBye(isbyepref)
			team.bookWeek(week.week)
			print "bookGame: successfully booked bye: [",gamenum,"]"," for team: [",team.name,"]"," on week: [",week.week,"] in game slot: ",gslot
			return 0
		else:
			# print bye unavailable
			print "bookGame: ERROR? Bye request but unavailable"
			print "bookGame: failed to book bye: [",gamenum,"]"," for team: [",team.name,"]"," on week: [",week.week,"] in game slot: ",gslot
			return 1

	else: #week is not a bye...
		print "bookGame: requested booking is not a bye, game number: [",gamenum,"]"," for team: [",team.name,"]"," on week: [",week.week,"] in game slot: ",gslot

		#if slot 1 occupant free
		if ((gslot == 1) and (week.game[gamenum].t1 == unbooked)):

			#print "bookGame: gslot == 1 and team 1 for current game is not booked"

			#if opponent exists:
			if (week.game[gamenum].t2 != unbooked ):

				bgame=team.checkOpponent(week.game[gamenum].t2)
				if (bgame == 1):
					# this is not a bye
					print "bookGame: cannot book team: ",team.name,"for game: ",gamenum,"for team (1 or 2): ",gslot , "opponent has already been played"
					return 1

				print "bookGame: booking team: ",team.name,"for game: ",gamenum,"for team (1 or 2): ",gslot

				#set team to self
				week.game[gamenum].setTeam1(team.tnum,team.name)
				team.incrGamesPlayed()

				# remove opponent from opponents
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
				#team.bookOpponent(Teams[week.game[gamenum].t1])
				myteam=getTeamByNum(Teams,week.game[gamenum].t1)
				team.bookOpponent(myteam)


				# remove self from opponent's opponents
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
				#Teams[week.game[gamenum].t2].bookOpponent(team)
				myteam=getTeamByNum(Teams,week.game[gamenum].t2)
				myteam.bookOpponent(team)

				# bookWeek for self
				print "bookGame: attempting to book week: ",week.week
				team.bookWeek(week.week)
				print "bookGame: week booked: ",week.week
				return 0

			else: #no opponent in slot 2 
				#so no bookkeeping needed for t2
				#and you can't book your opponent yet

				print "bookGame: zz booking team: ",team.name," in week: ", week.week, " for game: ",gamenum," in slot: ",gslot

				#set team to self
				week.game[gamenum].setTeam1(team.tnum,team.name)
				team.incrGamesPlayed()

				# bookWeek for self
				print "bookGame: attempting to book week: ",week.week
				team.bookWeek(week.week)
				print "bookGame: week booked: ",week.week
				return 0

		#elif slot 2 occupant free
		elif ((gslot == 2) and (week.game[gamenum].t2 == unbooked)):
			#not a bye

			print "bookGame: gslot == 2 and team 2 for current game is not booked"

			#if opponent exists:
			if (week.game[gamenum].t1 != unbooked ):


				bgame=team.checkOpponent(week.game[gamenum].t1)
				if (bgame == 1):
					# this is not a bye
					print "bookGame: cannot book team: ",team.name,"for game: ",gamenum,"for team (1 or 2): ",gslot , "opponent has already been played"
					return 1

				print "bookGame: booking team: ",team.name,"for game: ",gamenum,"for team (1 or 2): ",gslot

				#set team to self
				week.game[gamenum].setTeam2(team.tnum,team.name)
				team.incrGamesPlayed()

				# remove opponent from opponents
				print "bookGame: team num: ",team.tnum
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
				#print "bookGame: opp num: ",Teams[week.game[gamenum].t1].tnum
				myteam=getTeamByNum(Teams,week.game[gamenum].t1)
				print "bookGame: opp num: ",myteam.tnum
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
				#team.bookOpponent(Teams[week.game[gamenum].t1])
				myteam=getTeamByNum(Teams,week.game[gamenum].t1)
				team.bookOpponent(myteam)

				# remove self from opponent's opponents
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
				#Teams[week.game[gamenum].t1].bookOpponent(team)
				myteam=getTeamByNum(Teams,week.game[gamenum].t1)
				myteam.bookOpponent(team)

				# bookWeek for self
				print "bookGame: attempting to book week: ",week.week
				team.bookWeek(week.week)
				print "bookGame: week booked: ",week.week

		#else game is not available
		else:
			#exit LOUDLY
			print "bookGame: ERROR: GAME IS COMPLETELY BOOKED!!!!!"
			print "bookGame: team: ", team.name , " week: " , week.week , " gamenum: " , gamenum , " gslot: " , gslot
			if (gslot == 1):
				print "bookGame: team in slot attempted to book: " , week.game[gamenum].t1
			else:
				print "bookGame: team in slot attempted to book: " , week.game[gamenum].t2
			return 1

def getTeamByNum(Teams,num):
# assumes Team[x].num exists in Team[]
# returns Team[x]
	for team in Teams:
		if (team.tnum == num):
			return team
	

def checkAvailablity(team,week,gamenum):
#takes a team, week and game and determines if this game is bookable
#based on opponents played, slots available, and team preferences
#returns 0 if unavailable due to preferences
#returns 1 if team 1
#returns 2 if team 2
#retuns 3 if unvailable due to catastrophic scheduling conflict

	print "checkAvailablity: For week: " , week.week , " in game: " , gamenum , " current home team num: " , week.game[gamenum].t1 , " current away team num: ", week.game[gamenum].t2
	print ""
	#print team.dpref week.weekgamenum ignoreprefs

	#check for DoW pref if it's not a bye game being checked on
	if ((team.dpref != nopref) and (team.dpref != week.game[gamenum].date) and (week.week != opener) and (week.week != jambo) and (gamenum != byegame) and (ignoreprefs == 0)):

		#day pref mismatch
		print "checkAvailablity: dpref mismatch: ",team.name," dpref: ",team.dpref," day of game: ",week.game[gamenum].date,"returning 0"

		return 0

	#check for time of day pref if it's not a bye game being checked on
	elif ((team.tpref != nopref) and (team.tpref != week.game[gamenum].time) and (week.week != opener) and (week.week != jambo) and (gamenum != byegame) and (ignoreprefs == 0)):

		#time of day pref mismatch
		print "checkAvailablity: time of day mismatch"," time pref: ",team.tpref," time of current game: ",week.game[gamenum].time

		return 0

	#check for avalibility in slot 1
	elif (week.game[gamenum].t1 == unbooked):

		#slot 1 available, no opponent in slot 2
		print "checkAvailablity: returning 1 because slot 1 is avail for booking"

		return 1

	#check for availability in slot 2
	elif (week.game[gamenum].t2 == unbooked):

			#team in slot 1 is an available opponent
			if (team.checkOpponent(week.game[gamenum].t1) == 0):
				print "checkAvailablity: returning 2 b/c team in slot 1 is an available opponent"
				return 2
			else:
				print "checkAvailablity: returning 3 b/c slot available but opponent has already been played"
				return 3

	else:

		#print "checkAvailablity: not sure how we got here. Returning 3"
		print "checkAvailablity: returning 3 b/c no slots available."
		return 3


def bookBye(team,week):
# returns 0 on success
# returns 1 for fail due to preferences
# returns 2 for fail due to catastrophic conflict

	print "bookBye: entering function bookBye with arguments team: ",team.name," and week: ",week.week
	print "bookBye: team bye pref is: ",team.bpref," number of byes booked: ",team.byes

	#does Week have available byes?  # is it a jambo or opener week?
	bgame=week.checkBye()

	if (bgame > 0): #if week has games available

		bgame=team.checkBye()

		if ( bgame == 0 ): #if team has byes available

			if (team.checkWeek(week.week) == 0): #if team not booked already for this week

				if (prefFail == 0): #if can fail based on preference

					#if bye isn't too close to byepref (which was prescheduled) and proximity is being honored
					if ( ( week.week != team.bpref-1 ) and ( ( week.week != team.bpref+1 ) or ( team.bpref == nopref ) ) ):

						#schedule bye
						#zzzzzzzzzzzz why am I checking week for byes a 2nd time (and not handling the returned value??
						#possibly to get the gslot of the free slot (1 or 2)
						bgame=week.checkBye()
						booked=bookGame(team,week,byegame,bgame,0)
						if (booked != 0) and (week.week==lastWeekofSeason):
							booked=bookGame(team,week,FoLgamenum,bgame,0)
							if (booked != 0):
								print "bookBye: booking of bye still failed. might should do something about this... ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
			
						clearPrefFail()

						if (booked == 1):

							print "bookBye: attempt to book game failed"
							incrPrefVar()
							setPrefFail()
							return 1

						else:

							print "bye successfully booked"
							return 0

				else: #proximity preference is not being honored

					#schedule bye
					bgame=week.checkBye()
					booked=bookGame(team,week,byegame,bgame,0)
					if (booked != 0) and (week.week==lastWeekofSeason):
						booked=bookGame(team,week,FoLgamenum,bgame,0)
						if (booked != 0):
							print "bookBye: booking of bye still failed. might should do something about this... ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
					clearPrefFail()

					if (booked == 1):

						print "bookBye: returning 2 b/c attempt to book game failed"
						incrCata()
						return 2

					else:

						print "bookBye: returning 0 b/c bye successfully booked"
						return 0

			else: #team already booked this week
				print "bookBye: returning 2 b/c team is already booked this week (bye or otherwise)"
				incrCata()
				return 2

		else: #team has no byes available
			print "bookBye: returning 2 b/c team has already booked 2 byes"
			incrCata()
			return 2

	else: #week has no byes available
		print "bookBye: returning 2 b/c week has already booked 2 byes"
		incrCata()
		return 2
	
def incrCata():
	global catastrophic
	catastrophic += 1

def incrPrefVar():
	global prefvariance 
	prefvariance += 1

def setPrefFail():
	global prefFail
	prefFail=1

def clearPrefFail():
	global prefFail
	prefFail=0

def preschedGame(Sched,weeknum,gamenum,team1,team2):
	#schedule team 1
	print "preschedGame: SSSSSSSSSSSSSSSSSSSSSSS Start SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"

	print "prescheduling: ",team1.name," for week: ",weeknum," for game: ",gamenum
	print "prescheduling: ",team2.name," for week: ",weeknum," for game: ",gamenum

	booked=bookGame(team1,Sched[weeknum],gamenum,1,0)
	if (booked == 1):
		print "prescheduling: booking failed. might need to do something here..... TZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

	booked=bookGame(team2,Sched[weeknum],gamenum,2,0)
	if (booked == 1):
		print "prescheduling: booking failed. might need to do something here..... OZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

	print "prescheduling: scheduled Week " , weeknum , " game " , gamenum , " now has teams: " , Sched[weeknum].game[gamenum].t1 , " and " , Sched[weeknum].game[gamenum].t2
	print "prescheduling: scheduled Team " , Sched[weeknum].game[gamenum].t1 , " no longer has week " , weeknum , "available for scheduling: " , team1.openweeks
	print "prescheduling: scheduled Team " , Sched[weeknum].game[gamenum].t2 , " no longer has week " , weeknum , "available for scheduling: " , team2.openweeks
	print "prescheduling: scheduled Team " , Sched[weeknum].game[gamenum].t1 , " no longer has team " , Sched[weeknum].game[gamenum].t2 , "as an available opponent: " , team1.opponents
	print "prescheduling: scheduled Team " , Sched[weeknum].game[gamenum].t2 , " no longer has team " , Sched[weeknum].game[gamenum].t1 , "as an available opponent: " , team2.opponents


def preschedBye(Sched,weeknum,team):
	#print "preschedBye: BYEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
	#print "preschedBye: prescheduling a bye for team: " , team.name , " for week: " , weeknum
	bgame=checkAvailablity(team,Sched[weeknum],byegame) 
	booked=bookGame(team,Sched[weeknum],byegame,bgame,1)
	if (booked == 1):
		print "preschedBye: booking failed. might need to do something here..... ZZJZZZZZZZZZZHZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

#Team def:
#bye pref: 0=none else =week in season <=11
# Game Def:
# day: 0=Wed 1=Thurs 2=Sat 3=bye
# time: 0=Early|noon 1=Late|one 2=two 3=three 4=four 5=bye -1=nopref

#def __init__(self,teamname,daypref,byepref,timepref):
#create teams
#----------------------------------------
#Weds
#----------------------------------------
team0=Team("Sesamee  ", 1, 0,-1)
team2=Team("nerds    ", 1,-1,-1)
team3=Team("Neandr   ", 1,-1, 1)
team4=Team("Fowl     ", 1,-1, 1)
team5=Team("Bearly   ", 1,-1,-1)
#----------------------------------------
#Thurs
#----------------------------------------
team1=Team("WHAK     ", 2,-1, 1)
team6=Team("Magic    ", 2, 5, 0)
team7=Team("Sextras  ", 2,-1, 1)
#----------------------------------------
#None
#----------------------------------------
team8=Team("Amathong ",-1,-1,-1)
team9=Team("CULT     ",-1,-1,-1)
#----------------------------------------
#team 10 is Festival of Losers
#----------------------------------------
team10=Team("FoL   ",nopref,nopref,nopref)

#make list of teams for to iterate over
Teams=[team0,team1,team2,team3,team4,team5,team6,team7,team8,team9];

#create schedule
Weeks=[Week(0),Week(1),Week(2),Week(3),Week(4),Week(5),Week(6),Week(7),Week(8),Week(9),Week(10)];

#schedule FOL
Weeks[FoL].game[FoLgamenum].setTeam1(FoL,"FOL   ")
Weeks[FoL].game[FoLgamenum].setTeam2(FoL,"FOL   ")


# day: 0=Wed 1=Thurs 2=Sat 3=bye
# time: 0=Early|noon 1=Late|one 2=two 3=three 4=four 5=bye
#bookGame(team,week,gamenum,gslot,isbyepref)
#preschedGame(Weeks,7,3,team5,team8)

#openers (wed prefs vs thurs prefs)
#########################################
#team1 vs. team4
preschedGame(Weeks,1,2,team1,team4)
#team6 vs. team5
preschedGame(Weeks,1,3,team6,team5)
#team7 vs. team0
preschedGame(Weeks,1,4,team7,team0)


#jambo (wed prefs vs thurs prefs)
#########################################
#team1 vs team0
preschedGame(Weeks,7,2,team1,team0)
#team6 vs team2
preschedGame(Weeks,7,3,team6,team2)
#team7 vs team3
preschedGame(Weeks,7,4,team7,team3)

## Bye week requests:
#def preschedBye(Sched,weeknum,team):
#########################################
#bye pref: week 0 sessamee
preschedBye(Weeks,0,team0)

#bye pref: week 0 Magic
preschedBye(Weeks,0,team6)

# one off week/game requests:
#########################################
##ToD Week 0 Rogers
##bookGame(team7,Weeks[0],3,1,1)

##PRJ Week 2 Weds
##bookGame(team3,Weeks[2],0,1,1)


Teams=[team0,team1,team2,team3,team4,team5,team6,team7,team8,team9];

random.shuffle(Teams)

#########################################################
#### 			MAIN main Main
#########################################################


#iterate over all teams in the league
print "MAIN: MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  MAIN MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
for team in Teams:
	print "MAIN: TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT Team: ", team.name , " TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
	byestart=random.randint(0,10)

	while ((byestart == jambo) or (byestart == opener)):
		byestart=random.randint(0,10)

	if (team.bpref != nopref):
		byestart=team.bpref

	print "MAIN: byestart for team: ",team.name," = ",byestart

	#for each team iterate over every week in the season:
	for week in Weeks:
		week.refreshbookingCount()
	sortedWeeks=sorted(Weeks, key=lambda Week: Week.bookedgames) 

	#pushing week 10 to end of list (4 byes that week...)
	for week in sortedWeeks:
		if (week.week == 10):
			sortedWeeks.remove(week)
			sortedWeeks.append(week)

	print "MAIN: processing order of weeks for team: ",team.name
	for week in sortedWeeks:
		print "MAIN: Week: " , week.week , " the unbooked games count was: " , week.getbookedGamesCount()

	#print "MAIN: initializing prefFail to 0 for team: " , team.name , "000000000000000000000000000000000000000000000000000000000000000000"
	prefFail=0
	weekcounter = 0
	while weekcounter < len(Weeks):

		#print "MAIN: ---------------------- prefFail: ", prefFail , " ----------------ignoreprefs ", ignoreprefs , " -------------------------------------"

		week=sortedWeeks[weekcounter]
		if (team.gamesplayed == 9):
			byestart=week.week

		print "MAIN: WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW Actual Week: ", week.week , " WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
		print "MAIN: ----------------------------------------- Iteration: ",weekcounter," -------------------------------------------------- weekcounter = ",weekcounter
		print "MAIN: ------------------------------------------------------------------------------------------------------------ loopcount =   ",loopcount
		print "MAIN: ------------------------------------------------------------------------------------------------------------ len(Weeks) =   ",len(Weeks)
		print ""
		print "MAIN: scheduling week:      ",week.week," for team: ",team.name, "  team num: ", team.tnum , "      games played: ",team.gamesplayed,"      byes booked: ",team.byes
		print "MAIN: available weeks:     ", team.openweeks 
		print "MAIN: available opponents: ", team.opponents 
		print ""

		#if week available for this team
		if ( team.checkWeek(week.week) == 1):
			print "MAIN: week unavailable for team: ",team.name
			weekcounter += 1
			continue

		#if this is a preferred byeweek book the bye(if possible)
		if ( week.week == byestart ):
			booked=bookBye(team,week)
			print "MAIN: is team: ", team.name , " booked for week: " , week.week , "? (0 yes, non-0 no)" , booked
			if (booked == 0):
				if ( team.checkWeek(week.week) == 1):
					print "MAIN: bye booked successfully"
					print "MAIN: week now booked for team: ",team.name, "flipping bits back for prefFail, ignoreparts, and loopFail and continuing to next week"
					weekcounter += 1
					ignoreprefs=0
					prefFail=0
					continue
			else:
				print "MAIN: failed to book bye on prefered week - I might want to do something about this... 2ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"


		#determine if normal week or saturday (4 games vs. 5)
		if ((week.week == opener) or (week.week == jambo)):
			#print "MAIN: This is either opening day 2 or Jamboree 8: ",week.week
			numgames=5
		else:
			numgames=4


		#if all 9 games haven't been scheduled
		if (team.gamesplayed < 9):

			#given the current teams' preferences
			#try to find an available game in the given week

			loopFail=0
			for thisgame in range(0,numgames): #iterate over games in week

				print "MAIN: GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG Game Number: ", thisgame , "  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"

				print "MAIN: calling checkavailability for team: ",team.name," for game: ",thisgame
				print ""
				bgame=checkAvailablity(team,week,thisgame) 
				print ""
				print "MAIN: checkAvailablity returned: ",bgame, " [0 == unavail on prefs] [1 == team1 avail] [2 == team2 avail] [3 == catastrophic]"
				print ""

				#if unavailable due to preference conflict, set loopFail == 1
				if (bgame == 0):
					print "MAIN: setting loopFail to 1 0000000000000000000000000"
					loopFail = 1
					print "MAIN: setting ignoreprefs to 1"
					#ignoreprefs = 1

				if ((bgame == 3) or (bgame == 0)):
					print "MAIN: Main: game: ",thisgame," was not available for booking for team: ",team.name," in week: ",week.week," trying next game"
					print ""

				elif ((bgame == 1) or (bgame == 2)):
					print "MAIN: booking game: ",team.name," in week: ",week.week," for game: ",thisgame
					booked=bookGame(team,week,thisgame,bgame,0)
					if (booked == 1):

						print "MAIN: booking failed, probably should do something here... KZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

					else:

						print "MAIN: game booked successfully, attempting to break out of game check loop"
						break
				else:
					print "MAIN: ERROR: not sure how we got here... (main) "

		print "out of game check loop"

		#if week now booked for this team
		if ( team.checkWeek(week.week) == 1):
			print "MAIN: week now booked for team: ",team.name, "flipping bits back for prefFail, ignoreparts, and loopFail and continuing to next week"
			weekcounter += 1
			ignoreprefs=0
			prefFail=0
			continue

		
		print "MAIN: week still not booked for team: ", team.name , " attempting to book a bye"
		booked=bookBye(team,week)
		print "MAIN: is team: ", team.name , " booked for week: " , week.week , "? (0 yes, non-0 no)" , booked
		if (booked == 0):
			if ( team.checkWeek(week.week) == 1):
				print "MAIN: bye booked successfully"
				print "MAIN: week now booked for team: ",team.name, "flipping bits back for prefFail, ignoreparts, and loopFail and continuing to next week"
				weekcounter += 1
				ignoreprefs=0
				prefFail=0
				continue
		else:
			print "MAIN: ERROR: failed to book bye - I might want to do something about this... 2ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
			print "MAIN: ERROR: failed to book bye and no games failed due to preferences. This is catastrophic"


		# week still not booked disabling preferences for future iteration
		if (loopFail == 1):
			print "MAIN: loopFail was 1, flipping bits for prefFail, ignoreparts, and loopFail 44444444444444444444444444444444444444444444444444444"
			prefFail = 1
			ignoreprefs = 1
			loopFail = 0

		print "MAIN: checking for need to reiterate with preferences turned off. 00000000000000000000000000000"
		print "MAIN: week booked for team? [0 == no] [1 == yes]: " , team.checkWeek(week.week)
		print "MAIN: prefFail? [1 == bookings skipped based on preferences] [0 == bookings not skipped based on preferences]: ", prefFail
		print "MAIN: loopcount: [ if < 5 we'll attempt to book this same week again]: ", loopcount

		if ((team.checkWeek(week.week) != 1) and (prefFail == 1) and (loopcount < 5)):
			print "MAIN: Week still not booked, but some games were skipped based on preferences, iterating over this week again"
			# not incrementing loop counter
			print "MAIN: this is the ",loopcount," iteration of this week for this team"
			loopcount+=1
		else:
			print "MAIN: either the team just booked a bye or we've exceed the max iterations of the week, moving on to next week"
			weekcounter += 1
			prefFail=0
			print "MAIN: setting ignoreprefs to 0"
			print "MAIN: uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
			ignoreprefs=0
			loopcount=0





for week in Weeks:
	week.displayWeek()

print "*****************"
print "* unrecoverable errors: ",catastrophic, " *"
print "* preference variance: ",prefvariance, " *"
print "*****************"



print "*****************"

#for week in Weeks:
	#print "Week: " , week.week , " the booked games count was: " , week.bookedgames
#	print "Week: " , week.week , " the booked games count was: " , week.getbookedGamesCount()


print "------------------- sorting ---------------"
#for week in sortedWeeks:
	#print "Week: " , week.week , " the booked games count was: " , week.bookedgames
#	print "Week: " , week.week , " the booked games count was: " , week.getbookedGamesCount()

