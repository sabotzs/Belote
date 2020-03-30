import json
import sys
import os
from team import Team
from card import Card
from player import Player
from pprint import pprint


def print_jsonable_round(round,contract,team_one,team_two):
    if type(team_one) != Team or type(team_two) != Team:
        raise TypeError('Only teams are allowed')
    if type(contract) != str:
        raise TypeError('Contract must be string')

    data_helper = {'contract':contract, team_one.name: (info_as_dic(team_one.first), info_as_dic(team_one.second)),
                                team_two.name:(info_as_dic(team_two.first), info_as_dic(team_two.second))}
    round_str = "round" + str(round)
    data = round_str, data_helper

    return data

def info_as_dic(person):
    if type(person) is not Player:
        raise TypeError('wrong type of Player')
    else:
        help_dict = {
        'cards' : str(card_json(person.hand)),
        'announcemenets' : str(ann_json(person.announcements)),
        'score' : person.points
        }
    dic = {
    person.name : help_dict
    }
    return dic

def card_json(cards):
    list_of_cards = []
    for i in range(len(cards)):
        list_of_cards.append(str(cards[i]))
    return list_of_cards

def ann_json(ann):
    list_of_ann = []
    for i in range(len(ann)):
        list_of_ann.append(str(ann[i]))
    return list_of_ann




