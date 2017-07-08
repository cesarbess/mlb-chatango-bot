# mlb-chatango-bot
This bot has the goal to be the one and only chatango chat bot that is truly useful and not just a stupid and annoying AI.  If like me, you enjoy watching MLB games online with the company of several fans of the same team as you, or even rivals and chat along with it, this bot can make your group experience better.

It simply communicates between mlbgame.py library and the ch.py library and delivers realtime information about any team of your choice.

Instructions:

Under bot.py file set your desired bot account information in bot_account and bot_password properties. Also set the desired rooms you want it to be in on the rooms list property.

Run the bot.py file from terminal and it's up.

Command List:

    !score team_name - posts the score for the team name in the argument
    !pitching team_name - posts the current pitcher for the current game of the team in argument
    !batting team_name - posts the current pitcher for the current game of the team in argument
    !line team_name -  posts the pitching line for the starting pitcher of the game from the team in argument
    !record team_name posts the current W/L record for the team in arguments
    !time team_name - posts the start time of today’s game of the team in arguments
    !last_ab team_name - posts the description for the last at bat occurred in current inning of teams game in argument
    !ondeck team_name - posts the current player on deck on team_name game
    !inhole team_name - posts the current player in the hole on team_name game
    !dueup team_name - posts the due up batters oon team_name game

Note:

    #team_name = should be underscore e.g: !score cubs
    #information is in nearly real time
    #more commands to come
