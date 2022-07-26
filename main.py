from twitchio.ext import commands
from twitchio import Message
import os
import random
import re
from dotenv import load_dotenv
import chess
import chess.svg


load_dotenv()

class Bot(commands.Bot):

    #chess game details
    #new board
    board = chess.Board()
    chatColor = chess.WHITE
    chatPlayer = ""
    gameOngoing = False

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=os.getenv("PASS"), prefix='?', initial_channels=['#dusk_ai'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message: Message):
        if message.echo:
            return
        print(message.author.name + ": " + message.content)
        await self.handle_commands(message)

    @commands.command()
    async def move(self, ctx: commands.Context):
        if (self.gameOngoing == True):
            if (ctx.author.name == self.chatPlayer or ctx.author.name == "dusk_ai"):
                if (re.match('\?move [a-h][0-8][a-h][0-8]', ctx.message.content)):
                    if (chess.Move.from_uci(ctx.message.content[-4:]) in self.board.legal_moves):
                        self.board.push(chess.Move.from_uci(ctx.message.content[-4:]))

                        if (self.board.is_game_over()):
                            self.gameOngoing = False
                            await ctx.send('Good Game!')

                            svg_render = chess.svg.board(self.board, squares=chess.SquareSet([chess.parse_square(chess.square_name(self.board.king(self.board.turn)))]), size=None, coordinates=True)
                            imagefile = open('board.svg', "w")
                            imagefile.write(svg_render)
                            imagefile.close()
                        else:
                            svg_render = chess.svg.board(self.board, size=None, coordinates=True)
                            imagefile = open('board.svg', "w")
                            imagefile.write(svg_render)
                            imagefile.close()
                    else:
                        await ctx.send('Invalid move! Check your piece positions.')
                else:
                    await ctx.send('Invalid move! Send moves in uci format. Ex: ?move b2b4')
            else:
                await ctx.send('A match is already being played by ' + self.chatPlayer)
        else:
            await ctx.send('There is no game currently playing! Use ?newgame')

    @commands.command()
    async def listmoves(self, ctx: commands.Context):
        if (self.gameOngoing == False):
            await ctx.send('There is no game currently playing! Use ?newgame')
        else:
            await ctx.send("Current player to move: White" if self.board.turn == chess.WHITE else "Current player to move: Black")
            moves = ""
            for move in self.board.legal_moves:
                moves += str(move) + ", "

            #print(self.board.legal_moves)
            await ctx.send(moves[:-2])

    @commands.command()
    async def endgame(self, ctx: commands.Context):
        if (ctx.author.name == "dusk_ai"):
            self.gameOngoing = False
            await ctx.send("Admin ended the game.")

    @commands.command()
    async def newgame(self, ctx: commands.Context):
        if (self.gameOngoing == False):
            self.board = chess.Board() #create blank board
            self.gameOngoing = True #turn on new game

            if (random.randint(0, 1) == 1): #chat is white
                self.chatColor = chess.WHITE
                self.chatPlayer = ctx.author.name
                svg_render = chess.svg.board(self.board, size=None, coordinates=True)
                imagefile = open('board.svg', "w")
                imagefile.write(svg_render)
                imagefile.close()

                await ctx.send(f'{ctx.author.name} started a new game and plays White')
            else: #chat is black
                self.chatColor = chess.BLACK
                self.chatPlayer = ctx.author.name
                svg_render = chess.svg.board(self.board, size=None, coordinates=True)
                imagefile = open('board.svg', "w")
                imagefile.write(svg_render)
                imagefile.close()

                await ctx.send(f'{ctx.author.name} started a new game and plays Black')

        else:
            await ctx.send('A game is already going! Use ?move to play moves!')

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send("?help - Display the help screen\n   ?newgame - Start a new game if one isn't already going\n   ?move - Make a move in the current game if it is chat's turn (ex: ?move b2b4)\n   ?listmoves - list all possible moves for the current playing side")


bot = Bot()
bot.run()