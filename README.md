To intregrate this bot, you need to get the api keys from the following websites

1. `PUBLIC Code compiler API` - https://www.jdoodle.com/compiler-api
2. `Chatbot API` - https://brainshop.ai/
3. `Spotify API` - https://developer.spotify.com/dashboard/applications
4. `Postgres SQL server` - Any sql server...
5. `Google Message analyser API` - https://developers.perspectiveapi.com/s/docs
6. `TOP.GG server update API` - https://top.gg/api/docs/

After storing all the api keys, you need to fill in the keys in the empty .env file.
Now everything is setup, you can create a new bot at https://discord.com/developers/applications
and fill in the DISCORD_TOKEN.

You also would have to edit the bot owner ids stored as the list botowners.
In the line botowners = [`Your discord id here`]
Line no. 76 in main.py

You also have to change the ids these channels:
Line no. 2429 in main.py

```
    channelerrorlogging = client.get_channel(ERROR LOGGING CHANNEL ID)
    channelbuglogging = client.get_channel(BUG LOGGING CHANNEL ID)
    channelbuildlogging = client.get_channel(OPTIONAL BUILD LOGS(DEPRECIATED) CHANNEL ID)))
    channeldev = client.get_channel(DEVELOPER TESTING CHANNEL ID)
    channelgitlogging = client.get_channel(GITHUB LOGS CHANNEL ID)
```

Also you have to add these tables into the OLD sql server

```
CREATE TABLE riotmatches
(discorduserid bigint PRIMARY KEY,accountpuuid text,matchids text[]);
CREATE TABLE callsettings
(settingbool boolean ,userid bigint PRIMARY KEY);
CREATE TABLE spamchannels
(channelid bigint PRIMARY KEY);
CREATE TABLE leveling
(messagecount bigint ,memberid bigint,guildid bigint);
CREATE TABLE snipelog
(timedeletion timestamp without time zone ,embeds text ,content text ,username text ,channelid bigint PRIMARY KEY);
CREATE TABLE developer
(bypass boolean ,userid bigint );
CREATE TABLE logchannels
(channelid bigint ,guildid bigint PRIMARY KEY);
CREATE TABLE botbuilds
(buildchanges text ,buildname text ,buildtime timestamp without time zone PRIMARY KEY);
CREATE TABLE customcommands
(commandoutput text ,commandname text ,guildid bigint );
CREATE TABLE polls
(messageid bigint PRIMARY KEY);
CREATE TABLE verifychannels 
(channelid bigint,guildid bigint PRIMARY KEY);
CREATE TABLE levelconfig
(messagecount bigint ,channelid bigint);
CREATE TABLE musicchannel
(channelid bigint ,guildid bigint);
CREATE TABLE antiraid
(channelid bigint ,guildid bigint);
CREATE TABLE prefixes
(prefix text ,guildid bigint PRIMARY KEY);
CREATE TABLE ticketchannels
(emoji text ,roleid bigint ,messageid bigint ,channelid bigint );
CREATE TABLE profanechannels
(channelid bigint PRIMARY KEY);
CREATE TABLE linkchannels
(channelid bigint PRIMARY KEY);
CREATE TABLE levelsettings
(setting boolean ,channelid bigint PRIMARY KEY);
CREATE TABLE verifymsg
(messageid bigint ,channelid bigint ,guildid bigint PRIMARY KEY);
CREATE TABLE pendingunmute
(epochtime bigint ,reason text ,memberid bigint ,channelid bigint ,guildid bigint);
CREATE TABLE leaderboard
(mention text PRIMARY KEY);
CREATE TABLE cautionraid
(guildid bigint PRIMARY KEY);
CREATE TABLE pendingunblacklist
(epochtime bigint ,reason text ,memberid bigint ,channelid bigint ,guildid bigint);
CREATE TABLE blacklistedusers
(roleslist bigint[] ,userid bigint ,guildid bigint);
CREATE TABLE mutedusers
(roleslist bigint[] ,userid bigint ,guildid bigint);
CREATE TABLE pendingtrivia
(channelid bigint PRIMARY KEY);
CREATE TABLE warnings
(messageid bigint ,warning text ,guildid bigint ,userid bigint );
CREATE TABLE dankcmds
(implemented boolean ,rawtext text );
CREATE TABLE commandguildstatus
(commandname text ,guildid bigint);
CREATE TABLE riotaccount
(accounttag text ,accountname text ,accountimage text ,accountregion text ,accountpuuid text ,discorduserid bigint PRIMARY KEY);
CREATE TABLE restrictedusers
(epochtime bigint ,memberid bigint PRIMARY KEY,guildid bigint);
CREATE TABLE riotseason (
    act text,
    episode text
);
CREATE TABLE riotparsedmatches (id text PRIMARY KEY, data bytea);
```

Similarly add this onto the new sql server

```
CREATE TABLE mceconomy
(memberid bigint PRIMARY KEY,balance bigint,inventory text);
```
I'll add the bot to my server for the emojis.

After doing this, you can run the bot with the command `python main.py`
