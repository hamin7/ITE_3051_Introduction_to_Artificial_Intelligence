# ITE_3051_Introduction_to_Artificial_Intelligence

https://github.com/fantasykbo/record

https://cinema4dr12.tistory.com/1098

Title:

Proposal:
Modern sports are data-based sports.
Among them, MLB is based on high-level data technologies such as Sabermetrics.
These data technologies are also easily accessible when we watching the MLB game of Korean players' such as Ryu Hyun-jin, Choo Shin-soo and Choi Ji-man.
However, there is a limitation that it is one-way data providing. That means we are only able to access data that broadcaster and commentators provided. We cannot get the data that we are wondering. 
So we want to provide user-friendly baseball data using NUGU AI speakers in voice to provide a lot of interesting information that users want.
We will use official MLB-Data-API(https://appac.github.io/mlb-data-api-docs/) and other APIs to build the application. And we will use NUGU API and speaker too. For server side, we will use AWS EC2(provisional).
First, we provide game schedule for requested teams and players. And then if users ask some data, application will provide data in voice.
In particular, we will provide a variety of interesting data, including basic stats, and situational statistic data etc focusing on Korean players
We will also provide a voice function that explains baseball's stat analysis terms to help users understand them and other external element data.
Finally, by these provided data, we build simple algorithm to predict the winner, and tell the users when asked.
Below is a brief list of data to be provided.

1.	Basic game schedule
By teams, by players.
2.	Basic stat
Season pitching stats, career hitting stats, Season Team stats etc…
3.	Player’s situational statistic data
Pitcher vs Batter stat, Pitcher vs Opponent, Player’s situational records, Pitchers’ situational pitching patterns etc…
4.	Game external element
Park factor, monthly game stats
5.	Explain baseball’s stat terms
ERA+, WHIP, BABIP, OPS etc…
6.	Winner prediction.






API
(https://rapidapi.com/theapiguy/api/mlb-data, http://mlb.mlb.com/stats/sortable_batter_vs_pitcher.jsp#season=2019)
