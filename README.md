# Twitch Plays Chess

A simple implementation of chess for playing with viewers!

## Description

Using an OBS browser capture, visualize your board on stream and play chess with your viewers!

## Getting Started

### Dependencies

* Python 3.7+
* [TwitchIO](https://github.com/TwitchIO/TwitchIO)
* [Python Chess](https://github.com/niklasf/python-chess)

### Installing

* Download the repository (using either git or .zip download and extract)
* run
```
pip install -r requirements.txt
```
* Create a .env file with the fields
```
HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = '{your_twitch_name}'
CHAN = '{your_twitch_channel}'
PASS = '{twitch_oauth_token}'
```
To get an oauth token, go to [Twitch Token Generator](https://twitchtokengenerator.com/).

### Executing program

Simply run
```
py main.py
```
and wait for it to connect. Then you'll be able to run the commands listed below.

## Commands

* ?help - Display the help screen
* ?newGame - Start a new game if one isn't already going
* ?move - Make a move in the current game if it is chat's turn (ex: ?move b2b4)
* ?listMoves - list all possible moves for the current playing side

## Authors

Dusk

[Linktree](https://linktr.ee/EternalDusk)

## Version History

* 0.1
    * Initial Release

## To-Do
- [ ] Add check square highlighting
- [ ] Add last move arrow
