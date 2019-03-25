# --------------

import yaml

with open(path,'r') as crkt_yaml:
   crkt = yaml.load(crkt_yaml)

# Find data type of the file
print(type(crkt),'is the data type of file')

# In which city, and at which venue the match was played and where was it played ?
print('Match was played in',crkt['info']['city'],'at',crkt['info']['venue'])

# Which are all the teams that played in the tournament ? How many teams participated in total?
print(crkt['info']['teams'][0],'&',crkt['info']['teams'][1],'played in this match')
print(len(crkt['info']['teams']),'teams participated in total')

# Which team won the toss and what was the decision of toss winner ?
print(crkt['info']['toss']['winner'],'team won the toss and the decision of toss winner was to',crkt['info']['toss']['decision']) 


# Find the first bowler and first batsman who played the first ball of the first inning
print(crkt['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'],'was first bowler and',crkt['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'],'was the first batsman who played the first ball of the first inning')




# How many deliveries were delivered in first inning ?
print(len(crkt['innings'][0]['1st innings']['deliveries']),'deliveries were delivered in first inning')

# How many deliveries were delivered in second inning ?
print(len(crkt['innings'][1]['2nd innings']['deliveries']),'deliveries were delivered in second inning')

# Which team won and how ?
print(crkt['info']['outcome']['winner'],'team won the match by scoring',crkt['info']['outcome']['by']['runs'],'runs')







