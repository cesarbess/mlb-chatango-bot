import ch
import mlb
import mlb_data
import mlbgame

bot_account = "botthrowaway"
bot_password = "123456789"

class bot(ch.RoomManager):

    def onMessage(self, room, user, message):
        try:
            cmd, args = message.body.split(" ", 1)
        except:
            cmd, args = message.body, ""
        if cmd[0] == "!":
            prfx = True
            cmd = cmd[1:]
        else:
            prfx = False
        if prfx:
            if cmd.lower() == "score" and args != "":
                room.message(mlb.get_team_score(args))
            elif cmd.lower() == "pitching" and args != "":
                room.message(mlb.get_current_pitcher(args))
            elif cmd.lower() == "pitching" and args != "":
                room.message(mlb.get_current_pitcher(args))
            elif cmd.lower() == "batting" and args != "":
                room.message(mlb.get_current_batter(args))
            elif cmd.lower() == "line" and args != "":
                room.message(mlb.get_pitching_line(args))
            elif cmd.lower() == "record" and args != "":
                room.message(mlb.get_team_record(args))
            elif cmd.lower() == "time" and args != "":
                room.message(mlb.get_game_time(args))
            elif cmd.lower() == "lastab" and args != "":
                room.message(mlb.get_last_ab(args))
            elif cmd.lower() == "ondeck" and args != "":
                room.message(mlb.get_ondeck_batter(args))
            elif cmd.lower() == "inhole" and args != "":
                room.message(mlb.get_inhole_batter(args))
            elif cmd.lower() == "dueup" and args != "":
                room.message(mlb.get_due_up_batters(args))
            elif cmd.lower() == "starting" and args != "":
                room.message(mlb.get_starting_pitcher(args))


rooms = ["testingbotfam"]
username = bot_account
password = bot_password

bot.easy_start(rooms,username,password)
