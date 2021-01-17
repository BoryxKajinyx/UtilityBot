import discord
token_in=open('token.txt','r')
token_string=token_in.read(59)

client = discord.Client()
guild = discord.Guild

items = []
countries = []

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!'):

        cmd = message.content.split()[0].replace("!","")
            
        if cmd == 'story':

            data = []
            string = ''
  
            def is_command (msg):
                if len(msg.content) == 0:
                    return False
                elif msg.content.split()[0] == '!story':
                    return True
                else:
                    return False

            async for msg in message.channel.history(limit=100000):
                if msg.author != client.user:
                    if not is_command(msg): 
                        data.insert(0, msg.content)
            for x in data:
                items.append(x)
            string=''
            for y in items:
                string=string + str(y)
                string=string + ' '
            
        file=open('story.txt','w')
        file.write(str(string))
        print(string)
        file.close
        await client.delete_message(message)
    elif message.content.startswith('!members'):
        x = message.guild.members
        for member in x:
           countries.append(member[:4]) 
        await client.delete_message(message)
        file=open('countries.txt','w')
        file.write(str(countries))
        print(countries)
        file.close

    

client.run(str(token_string))