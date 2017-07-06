from __future__ import print_function
import time
import sys, os
import mlbgame
import helper
import xml.etree.ElementTree as ET
import mlb_data

#!score team_name command return
def get_team_score( team_name ):
    game = mlb_data.get_todays_game(team_name)
    if game:
        return(str(game[0]))
    else:
        return("Sorry, looks like there's no " + team_name + " game today")

#!pitching team_name command return
def get_current_pitcher( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't started yet"

    xml = mlb_data.get_game_data_overview(team_name)
    tree = ET.parse(xml)
    root = tree.getroot()

    for data in root:
        for current_pitcher in data.iter('current_pitcher'):
            player_id = current_pitcher.attrib['id']
            current_pitcher = current_pitcher.attrib['first_name'] + " " + current_pitcher.attrib['last_name'] + " is pitching. His record is " + current_pitcher.attrib['wins'] + "-" + current_pitcher.attrib['losses'] + "  with a " + current_pitcher.attrib['era'] + " ERA " + 'http://gdx.mlb.com/images/gameday/mugshots/mlb/'+player_id+'@4x.jpg'
            return current_pitcher
