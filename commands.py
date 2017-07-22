import mlb
import favorite_team

dictionary = {

    "score": mlb.get_team_score,
    "pitching": mlb.get_current_pitcher,
    "batting": mlb.get_current_batter,
    "line": mlb.get_pitching_line,
    "record": mlb.get_team_record,
    "time": mlb.get_game_time,
    "lastab": mlb.get_last_ab,
    "ondeck": mlb.get_ondeck_batter,
    "inhole": mlb.get_inhole_batter,
    "dueup": mlb.get_due_up_batters,
    "starting": mlb.get_starting_pitcher,
    "stats": mlb.get_player_stats,
    "seasonstats": mlb.get_player_season_stats,

}

def get_message_from_command(cmd, args, player):
    if cmd != None and args != None and player == None:
        return dictionary[cmd](args)
    elif cmd != None and args == None and player == None:
        return dictionary[cmd](favorite_team.short_name)
    else:
        return dictionary[cmd](args, player)
