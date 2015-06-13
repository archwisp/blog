# A Lesson From Cyber-Raid 0: Protect Your Nagios Server
A few weeks ago, I participated as a Red Team member in Cyber-Raid 0; a mock
hack/defend event held in Kansas City. It was a fun event even if there were a
few issues with how the rules were defined and enforced.

### Teams

There were 4 teams of defenders (Blue Teams) which represented companies, and
one big team of attackers (Red Team) continually attacking the Blue Teams.

### Setup

Six networks were accessible by the Red Team, all connected by one Cisco ASA:
one for the Red Team, one for each of the four Blue Teams, and one for the
scoring server. The Red Team was responsible for providing all of their own
equipment. Blue team members were responsible for providing a windows laptop
with which they would manage their VSX servers. The infrastructure was
provided by White Wolf Security and the entire game network was completely
isolated from the internet... sort of ;)

### Scoring

Blue Team scoring was handled by the score-bot connecting to services and
verifying that they were running. If a service could not be contacted, points
were added to the Blue Team responsible for that server. The objective of the
Blue Teams was to keep their respective scores as low as possible. Red Team
members scored points by executing the provided Phone-Home program on one of
the Blue Team servers. The more points the Red Team scored, the better.

### Rules

There were essentially no rules but to keep the game fun, a few simple rules
were laid out: 1) No "layer-two shenanigans". 2) Traffic cannot be blocked
from the "WAN" based on source IP. 3) No communication between Red and Blue
team members.

### Replay

We were notified that some people who took part in this event did not want
that information shared, so I will not include any identifying information in
my recounting of events.

First thing in the morning was breakfast followed by a "Briefing" where the
rules and concept of the game were laid out, followed by by questions. After
that, the teams split into their respective rooms isolated from one another.
The Blue Teams were given an hour to become familiar with their systems and we
were given the addresses of our network, the Blue Teams' class C networks, and
the scoring server. We were given no other information about the target
systems.

The first hiccup in the game came here: the Red Team could not connect to the
scoring server because of a routing problem. Once the router was working as it
was supposed to, each us registered our "Hacker Handle" and received an
account on the scoring server from which we could download the Phone Home
program.

Before we get to the action, I'll start off by saying that the Red Team room
was not very organized. A few teams showed up together and tended to work
together but there were quite a few of us who arrived alone and sort of
teamed-up based on who we were sitting near. This disorganization ultimately
proved to be a extremely counterproductive in the long-run because we ended up
working against each other.

Once everything was connected, I think everyone on the Red Team fired off a
network scan. Me and the guys I was working with separated the networks up and
started doing SYN scans with decoys which ended up working pretty well. We
Identified a mix of about a dozen Windows and Debian servers on each of the
networks. After we collected all of the host info, I started poking around
with telnet on Blue Team 1's network and... "WTF, I can't connect to any of
those services". We tried talking with the organizers and explaining that the
servers were inaccessible, but one of the helpers replied with some BS about
clever techniques. Well, we would later find out that they added a blanket
deny firewall policy to all traffic coming from the Red Team's network. (Did
you see rules #2?) If the Red Team had been more organized, we would have
collaborated and realized that nobody could connect to the services and raised
more of a fuss. So that was the state of the game for about half of the day.
We sat around trying to hack the ASA server between us and them; ultimately
getting nowhere.

Apparently, one of the groups on the Red Team had taken the more aggressive
approach of just telling Metasploit to attack whatever it could find and got a
phone-home script running in the moments before the Great Wall came down.
Unfortunately, the scoring server was not working at the time, so no points
were credited to them.

After the lunch break, things were looking brighter; Apparently, the game
organizers had caught on to the shenanigans and told them to open up specific
services; as would be the case in a real-world network. Well, it turns out
that even though the incoming policies were opened up, outgoing traffic was
still denied, so even when someone found a vulnerability, they couldn't
connect back and get a shell. In my opinion, that approach is perfectly
reasonable. I highly recommend egress filtering of all but the necessary ports
specifically for this reason. It is especially effective when you do filtering
on either a VLAN or a host-by-host basis.

### Finally, Some Progress

The first thing we managed to leverage was an "Open Source Application For
Disaster Management". When we first stumbled upon it, all of the security was
disabled and we could plainly see the application's configuration; including
the database login credentials. Unfortunately, the Database server was not
accessible from the "WAN", so that didn't go anywhere right away.

I continued exploring the application and found a few input sanitation
vulnerabilities which occupied me until the end of day one. Ultimately, I was
able to get a compressed malicious file uploaded to the server but couldn't
find the means to decompress it. I also wasted more time after I found a list
of "flags" on the scoring server which you could use to earn points by
acquiring key bits of sensitive information. What the organizers didn't
announce officially was that these flags were not working. So after trying a
few with no success, I asked, and they confirmed that they were in fact, not
working.

In the mean-time, some of the other Red Team groups discovered PHPMyAdmin
running on a few of the servers. So that, combined with the login credentials
from the "Open Source Application For Disaster Management", the they had
access to the MySQL database; including the ability to browse the local file
system of the database server.

#### Lesson 1) Don't run PHPMyAdmin on a server accessible via HTTP from a
lower security zone than the DB server. (in case you didn't already know)

What most of the Red Team didn't know was that one of the smaller groups had
managed to leverage the PHPMyAdmin avenue to get access to most of the servers
on all of the networks and started racking up points. The first thing they did
once they gained access to the MySQL server was to grab the /etc/passwd file,
as most of the other groups did. Where they went one step further was, instead
of discarding the file because shadow passwords were enabled, they scanned the
list of user names looking for services. One of these user names stood out:
nagios. Well, they found the Nagios server and tried the default password:
nagios; Success! This proved to be the only successful avenue of scoring for
the remainder of the game.

#### Lesson 2) Nagios needs an account for every service which needs to be
checked and those user names/passwords are stored in plain-text. If someone
gets into it, they get into everything. (in case you didn't already know)

### Day 2

Well, day two was a bit of a disappointment because a lot of the Blue Team
members didn't show up and two of the networks were completely down. This
meant that there were only two instances of any given service running;
including the one I was investigating. Remember the "Open Source Application
For Disaster Management"? Well, I had download the source code and was looking
for vulnerabilities. Unfortunately, one of Blue Teams realized that the MySQL
service had been compromised and they changed the password which left the
application crippled in a "Can't connect to the database" state. I still don't
know if they had point scored against them for this because the score-bot
would just be checking whether it could connect to the service or not. So this
left one more instance of the "Open Source Application For Disaster
Management" running. And just as I was about to test a vulnerability that I
found, the database for that service disappeared; someone had inadvertently
deleted it; another case of disorganization. From then on, with about 3 hours
left in the game, we were just kinda poking and prodding but nothing came to
fruition.

### Conclusion

Overall, it was a fun experience; It gave me a chance to sit in the attacker's
seat and focus all of my attention on gaining access. I also got to meet and
work with a lot of talented people; it sure is a small world. At the end of
the day, all of the Red Team agreed that we should have started sharing
information at the beginning of the game and organized ourselves. Ultimately,
the only significant scores posted were leveraged via the Nagios server. If we
had been sharing information, maybe we would have made good use of the lost
time and found another avenue of attack. I guess we'll never know.

I look forward to participating again next year.
