# scheduler
kickball scheduler

scheduler.py attempts to generate a schedule
finder1.sh runs scheduler.py taking a number as an argument which routes the generated schedules in to cands/cand<number>

so executing:
/root_dir/finder1.sh 7
will result in candidate schedules being created in:
/root_dir/cands/cands7

The problem:
There are 10 teams who play every other team in the league exactly once, for a total of 9 games.
Every team has 2 bye weeks.
Every team either has 1 game or 1 bye every week.
9 games plus 2 byes means there are 11 weeks in the season.
Every normal week there are 4 games. 8 teams play and 2 have byes.
There are 3 non-normal weeks.
2 are "Saturday Weeks", in which there are 5 games, all 10 teams play, no byes.
1 is The week of Festival of Losers(FoL).  6 teams play regular games. 2 teams have byes. 2 teams play the FoL. 

Teams can and do specify scheduling preferences:
- day of week preference (Weds/Thurs)
- time of day preference (Early Game/Late Game)
- bye week prefence (ie We all have a wedding to attend in week 7, please put one of our byes on that week)

The architecture:
Scheduler.py is object oriented.
Teams are a class.
- opponents (teams not yet played)
- openweeks (weeks not yet scheduled)
- byes (number of byes scheduled)
- name (actual team name)
- dpref (preferred day of week)
- tpref (preferred time of day)
- bpref (preferred bye week)
Weeks are a class.
- week num (0-10)
- number of games booked
Games are a class.
- time of day
- day of week
- team1.name
- team1.isbooked
- team2.name
- team2.isbooked

the scheduling process:
some games and byes get prescheduled:
- by request
- because it's nice to have weds pref teams play thurs pref teams on Saturdays to minimize not getting a pref.

Scheduler.py randomizes the ordering of the list of teams and the ordering of the weeks, and then iterates over the list of teams one at a time, booking a team's entire season, taking multiple passes if necessary.  
- On the first pass it respects team preferences. If the team is fully booked after the first pass. YAY. 
- If not, it ignores the preferences and tries to book all the remaining weeks.  
- If that fails, the schedule fails.

Finder1.sh invokes scheduler.py in a never ending while loop, so that theoretically, eventually it will try all possible combinations of team orderings and week orderings to find a combination that allows a successfull scheduling of the season.


