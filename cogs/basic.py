from discord.ext import commands
from datetime import datetime as d

class Basic(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    
    #Définir une nouvelle commande
    @commands.command(
        name = 'ping',
        description = 'Cette commande permet de tester le temps de réponse du bot',
        aliases = ['p']
    )
    async def ping_command(self,ctx):
        start = d.timestamp(d.now()) 
        #Prend l'horodatage de quand la commande a été utilisée

        msg = await ctx.send(content = 'Pinging...')
        #Envoie un message à l'utilisateur dans le salon dans lequel la commande a été exécutée
        #Notifies l'utilisateur le pinging a commencé

        await msg.edit(content=f"Pong!\nL'aller-retour du message a pris {(d.timestamp( d.now() ) - start ) * 1000}ms.")
        #Le ping a été effectué et la durée de l'aller-retour est affiché en ms
        return


    @commands.command(
        name = "test",
        description = "Cette commande permet de vérifier que je fonctionne bien !",
        aliases = ['hello','bonjour','helloworld']
    )
    async def test_command(self,ctx):
        await ctx.send("Je suis là ! ^^")
        return


    @commands.command(
        name = 'alskbot',
        description = "Cette commande permet d'en savoir plus sur moi !",
        aliases = ['description']
    )
    async def inutilite_command(self,ctx):
        await ctx.send("""Hey !\nJe suis le bot Alskbot !\n""" \
        """Mon but est de rajouter des commandes utiles à Discord, comme des commandes d'Administration, de messages ou encore de fun !\n""" \
            """De base, j'ai été créée (oui féminin parce que pourquoi pas) par Tjibzo pour apprendre les bases de l'API Discord.py.\n"""\
                """Je suis un bot "modulaire" qui peut se voir rajouter des fonctionnalités en fonction des besoins des utilisateurs.\n"""\
                    """Mon fonctionnement nécessite la présence des rôles `@Muted`, `@PasValidé` et `@Validé`, afin de faire fonctionner les commandes Admin.\n"""\
                        """Si vous voulez voir l'avancement de mon développement, il est disponible ici : https://trello.com/b/vcRBHuC3\n"""\
                            """Que dire de plus ? Amusez vous bien ? *(je suppose)*""")
        return


    @commands.command(
        name = 'github',
        description = "Cette commande permet d'avoir le lien de la repo GitHub qui contient mon code !",
        aliases = ['code','git']
    )
    async def github_command(self,ctx):
        await ctx.send("Voici le lien de mon code !\nhttps://github.com/Tjibzo/Alskbot")
        return



def setup(bot):
    bot.add_cog(Basic(bot))
    #Ajoute les commande Basic au bot
    #Note : la fonction "setip" doit être dans tous les fichiers cog