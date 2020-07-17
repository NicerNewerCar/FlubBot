# FlubBot
Flubbot V1.3
This is the code of Flub bot - A Discord bot I am working on for the Official Flub Discord Server: https://discord.gg/W9XWFGs
This code requires a py file called botkey which contains two variables, a discord bot token called 'bot_token' which can be generated from
https://discord.com/developers/ , and an API key to the deep Dream api, called 'API_Key' which can be generated from https://deepai.org/

FlubBot Requires the following python packages to function:
``````````````````````````````````````````````````````````````````````````````````````
Discord
Pillow
Random
Requests
``````````````````````````````````````````````````````````````````````````````````````

Current Features:
``````````````````````````````````````````````````````````````````````````````````````
Flub bot has a 10% chance to reply to a message sent in a discord server.
He has a 5% chance to run an image, posted by a user, through the deep dream API four times. 
This can also be done manually by use the caption '$flube' when uploading a photo onto discord, however when you do it manually
flub bot runs the images through the API ten times.
Using the command 'flubxra' flubbot randomly selects a quote from a list of quotes from xra to be spoken
``````````````````````````````````````````````````````````````````````````````````````
Future Plans:
``````````````````````````````````````````````````````````````````````````````````````
We would like to enable voice chat on flub bot, where he can join a channel of a user who calles him using the token '$flub'
and play some sort of audio clip for the user.
Another feature we would like to add, is whenever a user uploads an image to the server flub bot should have some low chance of taking
that image and hiding a "flub" in that image.
``````````````````````````````````````````````````````````````````````````````````````