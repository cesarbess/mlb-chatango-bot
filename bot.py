import ch

bot_account = "mlbrobot"
bot_password = "123456789"

class bot(ch.RoomManager):

    def onMessage(self, room, user, message):
        print("[{0}] {1}: {2}".format(room.name, user.name.title(), message.body))
        try:
            cmd, args = message.body.split(" ", 1)
        except:
            cmd, args = message.body, ""
        if cmd[0] == "!":
            prfx = True
            cmd = cmd[1:]
        else:
            prfx = False
        print(cmd)
        print(args)
        if prfx:
            if cmd.lower() == "hi":
                room.message("hi @"+user.name)

rooms = ["testingbotfam"]
username = bot_account
password = bot_password

bot.easy_start(rooms,username,password)
