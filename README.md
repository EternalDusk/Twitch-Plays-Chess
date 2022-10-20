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
python main.py
```
and wait for it to connect. Then you'll be able to run the commands listed below.

## Commands

* ?help - Display the help screen
* ?newgame - Start a new game if one isn't already going
* ?move - Make a move in the current game if it is chat's turn (ex: ?move b2b4)
* ?listmoves - list all possible moves for the current playing side

## Authors

Dusk - [Linktree](https://linktr.ee/EternalDusk)

## Version History

* 0.2
    * Prevented other chatters from playing an already running game
    * Added an X overlayed onto the checkmated king
    * Changed all commands to be all lowercase
    * Fixed redundant code in the move function for drawing the current board state

* 0.1
    * Initial Release

## To-Do
- [ ] Add check square highlighting
- [ ] Add last move arrow
- [ ] Add X overlayed onto both kings in state of draw
- [ ] Display the current turn (highlight playing turn's moveable pieces)
- [ ] Add a twitch overlay component allowing players to directly interact with the chess board through screen
