import discord

# Defina as intenções que o bot irá utilizar
intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logado como {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient(intents=intents)  # Passa o objeto de intenções ao criar a instância do cliente
client.run('MTEzMzU0MDA3Njk2MjQ0NzM4MA.GW-gFc.-NBC62XzNNwdnfDioFC5vAGm-AE0Iya5UcfM-Q') 
# TOKEN de acesso do BOT
