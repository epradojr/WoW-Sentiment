# World of Warcraft In-game Sentiment Using Trade Chat
#### *Author: Edel Prado*
<p></p>


<img width=100% src="images\header.PNG">
<p></p>

## <b><u>Overview</u></b>

World of Warcraft has been slowly losing its player base the past five years because of a multitude of issues in game design and communication with consumers. To better improve the game and decrease player negative sentiment, Blizzard Entertainment, the creators of World of Warcraft, should focus on gathering player feedback and what better way to do that than to gather it from inside the game. This specifically being the chat channel called Trade Chat.
## <b><u>Business Problem</u></b>
World of Warcraft has been the top massive multiplayer online game since it was released on November 23, 2004, but it has been struggling to keep active players for the past 5 years. With the new content patch 9.2, Eternity’s End, many players are returning to the game. To keep the attention of their subscribers, Blizzard Entertainment, the creators of World of Warcraft, should be looking to gather player feedback on the newly released patch update to keep it’s player base content.
## <b><u>The Data</u></b>
*What is Trade Chat?* <p></p>
Trade chat is a chat channel that can be seen by all players in any major player hubs per server. In my case, the server was Area 52 which is the most player populated server currently. The channel was meant for trading between players, but has become infamous for trolling as well as harassment. 

*How does this relate to player feedback?* <p></p>
Most players see Trade Chat as a way to let off steam and sometimes the topic they are venting about is the game, World of Warcraft, itself. 

Through the use of the in-game chat command "/chatlog", I collected roughly 24 hours of data. This came out to be 4,448 chat entries. I then manually classified each entry by text topic and sentiment. Here you can see what my raw data looked like.

<img width=65% src="images\chat_example.PNG">

## <u>Findings</u>
### <u>Sentiment Analysis</u> 
For the sentiment analysis of game related text, we see that about 41% of the chat had negative sentiment during the launch of patch 9.2, Eternity’s End.

<img width=65% src="images\sent_chart.PNG">


### <u>Topic Analysis</u>
*So what exactly are the players complaining about?* <p></p>
Here we have some of the top topics found in negative chat. In our server stability topic, we have words such as ‘dc’ meaning disconnect, ‘broken’, ‘lag’, and ‘org’ and ‘oribos’ which are major cities in the game. In our armor set aesthetic, we have words such as ‘sets’, ‘looks’, ‘portapotty’, and ‘priest’ and ‘hunter’ which are classes in World of Warcraft. The third topic is interesting since it tells us that there may be a bug with a quest called “A Hasty Voyage”. It looks like players would fall through the map or get stuck somehow. This can be seen as a major find since this quest is what allows you to enter the new content of patch 9.2.

<img width=80% src="images\topic_chart.PNG">

## <u>Models</u>

## <u>Suggestions</u>

## <u>Future Research</u>

## <u>For More Information</u>
Please review my step by step analysis in my jupyter notebook or my presentation.

Feel free to contact me through the below links if you have any questions.
[LinkedIn](https://www.linkedin.com/in/edel-prado-jr/) | [Email](edel.prado.jr@gmail.com)


**Repository Structure:**
```
├── data                         <- Both sourced externally and generated from code 
├── images                       <- Both sourced externally and generated from code 
├── .gitignore                   <- gitignore      
├── README.md                    <- The top-level README for reviewers of this project
├── presentation.pdf             <- PDF version of project presentation
└── index.ipynb                  <- Narrative documentation of analysis and modeling