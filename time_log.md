Monday: Creating Trello and loggin doc. 1.5 hours.
Tusday: Setup. Installing python dependencies, pandas, matplotlib, numpy, creting the github repo, and making some research, 2 h. 

Data set to analize: 
I choose basketball data set in different seasons. this contains the following columns: 
Games	MinutesPlayed	FieldGoals	FieldGoalsAttemps	FieldGoals%	3Points	3PAttemps	3Points%	2Points	2PAttemps	2Points%	FreeThrows	FTAttemps	FT%	OffensiveReBounds	DeffensiveReBounds	TotalRB	AST	STL	BLK	TurnOVers	PersonalFouls	PTS

What does each column represent?
Each column represents a statistic that helps describe how a team plays throughout the season. These stats reflect tendencies, pace, efficiency, and overall style of play. For example, minutes played can indicate roster usage and game involvement over the season.

What does better mean for each stat?
“Better” does not always mean “good” or “bad.” Many statistics simply describe how a team plays rather than how strong the team is. Some stats are more meaningful than others; for example, 3P% (three-point percentage) is more informative than total 3P made because it reflects efficiency rather than volume.

Are these per-game or aggregated values?
These are seasonal statistics, so they represent aggregated values across the season, not per-game averages.

Are team and opponent stats comparable?
Yes. Team and opponent stats are comparable because they describe different aspects of the same games and help explain contrasting behaviors and performance styles between teams.


second day: 
Reviewing information of how to use pandas and downloading the databases

Basics of Pandas

I would be using Jupyter notebook to display the information i am getting. 

pandas head(): prints the first five rows of the data. 

pandas tail(): prints the last five rows of the data. 

info() general information of the dataframe

describe()Generate descritive stadistics. central tendency, etc

columns the list of the different columns that the files has. 

index, gives you the amount of indexes that you can work it 

df["column"]: access all the values inside the column. 

df.iloc: locate by using index location. rows.


Filtering: 

df[df["column"] == "something"] you can also add multiple filters

isin: we can set a column and look for a value if that value that match with something we set.

update data: 

loc(): locate using a label

delete

drop(): this command hels us to drop rows. inseide the parentesis you set the index. 

dropna(): drop everything that contains null values or NA. 

fillna(): instead of removing we can set something to a different value. 

.rename() change the name of columns

Analize DATA: 


I analize the data and notice that to work my idea, I would need to merge the dataframes in one documents. 

Right now i have season 24 and season 25, both with team and opp info. 

So i would merge the season 24 with the information of opp and team. I would do the same with the season 24 and 25. 

I would use the pd.merge() to accomplish this. 

To save your data to processed data: 

index=False. this is important because if not, when save the data will add a new column. 


pd.concat(): This is like merge, but instead of putting everyhting to left or right, this would merge in rows. 

pd.sample(): is a function that allows to take randombly an amount of data from the table. 


Questions that I will analize: 


1. Dominance & Performance

Who are the top contenders based on Net Rating? (¿Quiénes son los principales contendientes basados en el diferencial de puntos?)

  During the seasion 24-25 and 25-26 the top contenders on net rating is Oklahoma city Thunder. 

Which teams have the most efficient offense vs. the most suffocating defense? (¿Qué equipos tienen la ofensiva más eficiente vs. la defensa más asfixiante?)

I need to create lines of reference. Using mean or average in points. 
  During both seasons 24-25 and 25-26 the team that scores more points is Oklahoma Thunders, but also is the team that accepts less points. If we notice they appear in the right upper quadrant of the plot. That mean that they score a points and receive less points. So this result with the net rating, put them as the best team. 

Is there a high correlation between Total Rebounds (TRB) and Win Percentage?

https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20is,relationship%20between%20two%20quantitative%20variables.

  To know this we will use Pearson correlation. This correlation explains how good a variable explains another one. If the correlation value is close to 1, is a strong correlation, if the value is -1 their correlation is negative. 
  We will use the net rating and the TBR to see the correlation between those variables and winning percentage. 
  There is no correlation between the TBR and the net rating. This can be explaining because in the modern Basketball teams care more about shooting than rebounding. 





2. Shooting & Scoring Efficiency (Eficiencia de Tiro)
Aquí analizamos qué tan bien aprovechan sus oportunidades.

Who leads the league in True Shooting Percentage (TS%)? (¿Quién lidera la liga en el porcentaje de tiro real?)

Does a higher 3-Point Attempt Rate (3PAr) lead to more points scored per game? (¿Un mayor volumen de intentos de triple genera más puntos por partido?)

Which teams are the most disciplined (lowest Turnover Percentage)? (¿Qué equipos son los más disciplinados o tienen menos pérdidas de balón?)

3. Team vs. Opponent Analysis (Análisis Comparativo)
Esta es la parte más rica de tus datos, pues tienes ambos lados de la moneda.

Which teams force their opponents into the lowest Field Goal Percentage (FG%)? (¿Qué equipos fuerzan a sus oponentes al porcentaje de tiro más bajo?)

How does a team's Offensive Rebound (ORB) performance affect their Opponent's Second Chance Points? (¿Cómo afecta el rebote ofensivo de un equipo a los puntos de segunda oportunidad del oponente?)

Year-over-Year Evolution: Which team showed the biggest improvement in Defensive Rating? (Evolución año tras año: ¿Qué equipo mostró la mayor mejora en su rating defensivo?)



