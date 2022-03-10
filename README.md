# World of Warcraft In-game Sentiment Using Trade Chat
#### *Author: Edel Prado*
<p></p>


<img width=100% src="images\header.PNG">
<p></p>

## <b><u>Overview</u></b>

World of Warcraft has been slowly losing its player base the past five years because of a multitude of issues in game design and communication with consumers. To better improve the game and decrease player negative sentiment, Blizzard Entertainment, the creators of World of Warcraft, should focus on gathering player feedback and what better way to do that than to gather it from inside the game. This specifically being the chat channel called Trade Chat.
## <b><u>Business Problem</u></b>
World of Warcraft has been the top massive multiplayer online game since it was released on November 23, 2004, but it has been struggling to keep active players for the past five years. With the new content patch 9.2, Eternity’s End, many players are returning to the game. To keep the attention of their subscribers, Blizzard Entertainment, the creators of World of Warcraft, should be looking to gather player feedback on the newly released patch update to keep it’s player base content.
## <b><u>The Data</u></b>
*What is Trade Chat?* <p></p>
Trade chat is a chat channel that can be seen by all players in any major player hubs per server. In my case, the server was Area 52 which is the most player populated server currently. The channel was meant for trading between players, but has become infamous for trolling as well as harassment. 

*How does this relate to player feedback?* <p></p>
Most players see Trade Chat as a way to let off steam and sometimes the topic they are venting about is the game, World of Warcraft, itself. 

Through the use of the in-game chat command "/chatlog", I collected roughly 24 hours of data. This came out to be 4,448 chat entries. I then manually classified each entry by text topic and sentiment. Here you can see what my raw data looked like.

<img width=65% src="images\chat_example.PNG">

## <b><u>Findings</u></b>
### <u>Sentiment Analysis</u> 
For the sentiment analysis of game related text, we see that about 41% of the chat had negative sentiment during the launch of patch 9.2, Eternity’s End.

<img width=55% src="images\sent_chart.PNG">


### <u>Topic Analysis</u>
*So what exactly are the players complaining about?* <p></p>
Here we have some of the top topics found in negative chat. In our server stability topic, we have words such as ‘dc’ meaning disconnect, ‘broken’, ‘lag’, and ‘org’ and ‘oribos’ which are major cities in the game. In our armor set aesthetic, we have words such as ‘sets’, ‘looks’, ‘portapotty’, and ‘priest’ and ‘hunter’ which are classes in World of Warcraft. The third topic is interesting since it tells us that there may be a bug with a quest called “A Hasty Voyage”. It looks like players would fall through the map or get stuck somehow. This can be seen as a major find since this quest is what allows you to enter the new content of patch 9.2.

<img width=80% src="images\topic_chart.PNG">

## <b><u>Models</u></b>
Since I'm not able to clone myself, I created three models. My first model is a multiclass model to classify the topic of the text as chat, game, or service. The next model is a sentiment model that labels the text as either negative or non-negative sentiment. My final model is my topic model that is only fed negative game classified text to create player feedback on the current state of World of Warcraft.
### <u>Multiclass Model</u>

<img width=55% src="images\multiclass_chart.PNG">

<img width=45% src="images\multi_logreg.PNG">

### <u>Sentiment Model</u>

<img width=55% src="images\sentiment_chart.PNG">

<img width=45% src="images\sent_logreg.PNG">

### <u>Topic Model</u>

<img width=80% src="images\topic_clusters.PNG">


## <b><u>Suggestions</u></b>
For our suggestions based on player feedback, Blizzard Entertainment should focus on three areas. 
1. Increase server stability during launch of new content. 

2. Have players vote for their class armor set appearance to help reduce the amount of negative sentiment towards it. 

3. Debug the quest called “A Hasty Voyage” to allow players to enter the new zone introduced in patch 9.2, Eternity's End without issues.

## <b><u>Future Research</u></b>
Moving into future reasearch, I would focus on the following:

1. Gather data from all servers and regions to highlight topics with the most negative sentiment. This will also allow us to find the differences between player interests per region and it could help my models better predict topic and sentiment.

2. Place a non-player character, better known as NPC, in all major player hubs where players can be given sentiment based multiple choice questions on current and new game features. This will allow for a constant and friction less flow of player feedback.

3. Adapt my models to track harassment and block it so as to not deter newer players from World of Warcraft. 
## <b><u>For More Information</u></b>
Please review my step by step analysis in my jupyter notebook or my presentation.

Feel free to contact me through the below links if you have any questions.

Edel Prado | Data Scientist: 
[ [LinkedIn](https://www.linkedin.com/in/edel-prado-jr/) ] [ [Email](edel.prado.jr@gmail.com) ]


<b>Repository Structure:<b>
```
├── data                         <- Both sourced externally and generated from code 
├── images                       <- Both sourced externally and generated from code 
├── .gitignore                   <- gitignore      
├── README.md                    <- The top-level README for reviewers of this project
├── presentation.pdf             <- PDF version of project presentation
└── index.ipynb                  <- Narrative documentation of analysis and modeling