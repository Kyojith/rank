from json import load,dump
from nextcord.ext import commands
from nextcord import Role , TextChannel,Embed

class Role(commands.Cog): 
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def setreactrole(self,ctx : commands.Context , messageid : str , role: str ,emoji = None):
        a_file = open(
            "data/role.json", "r", encoding="utf-8"
            )
        json_object = load(a_file)
        a_file.close()
        if messageid not in json_object["Role"]:
            data = {
                messageid : {
                    emoji : role
                }
            }
            json_object["Role"] = data
            a_file = open(
                "data/role.json", "w", encoding="utf-8"
            )
            dump(
                json_object,
                a_file,
                indent=4,
                ensure_ascii=False,
                )
            a_file.close()
        
        else:
            json_object["Role"][messageid][emoji] = role
            a_file = open(
                "data/role.json", "w", encoding="utf-8"
            )
            dump(
                json_object,
                a_file,
                indent=4,
                ensure_ascii=False,
                )
            a_file.close()

        message = await ctx.fetch_message(messageid)
        await message.add_reaction(emoji)
        embed = Embed(
            title = "สร้างสําเร็จ",
            colour = 0x99c8ff
        )
        embed.set_footer(text=ctx.author)
        await ctx.reply(embed=embed , delete_after=3)

def setup(bot: commands.Bot):
    bot.add_cog(Role(bot))