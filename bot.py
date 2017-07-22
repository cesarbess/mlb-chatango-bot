import ch
import mlb
import mlb_data
import mlbgame
import commands

bot_account = "botthrowaway"
bot_password = "123456789"

class bot(ch.RoomManager):

    def onMessage(self, room, user, message):
        try:
            cmd, args, player = message.body.split(" ", 2)
        except:
            try:
                cmd, args = message.body.split(" ", 1)
                player = None
            except:
                    cmd = message.body
                    args = None
                    player = None

        if cmd[0] == "!":
            prfx = True
            cmd = cmd[1:]
        else:
            prfx = False

        if prfx:
            print(cmd, args, player)
            room.message(commands.get_message_from_command(cmd, args, player))

rooms = ["testingbotfam"]
username = bot_account
password = bot_password

bot.easy_start(rooms,username,password)
