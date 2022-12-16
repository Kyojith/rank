import nextcord
import json
from nextcord.ext import commands

class Event(commands.Cog): 
    def __init__(self, React: commands.Bot):
        self.React = React
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload : nextcord.RawReactionActionEvent): 
        with open("data/role.json", "r+" , encoding='utf-8') as file:
            currentdata = json.load(file)["Role"]
            if str(payload.message_id) in list(currentdata.keys()) and str(payload.emoji) in list(currentdata[str(payload.message_id)].keys()):
                member = payload.member
                role = self.React.get_guild(payload.guild_id).get_role(int(currentdata[str(payload.message_id)][str(payload.emoji)]))
                if not role in member.roles:
                    await member.add_roles(role)

            else:
                pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload : nextcord.RawReactionActionEvent):
        with open("data/role.json", "r+" , encoding='utf-8') as file:
            currentdata = json.load(file)["Role"]
            if str(payload.message_id) in list(currentdata.keys()) and str(payload.emoji) in list(currentdata[str(payload.message_id)].keys()):
                member = self.React.get_guild(payload.guild_id).get_member(payload.user_id)
                role = self.React.get_guild(payload.guild_id).get_role(int(currentdata[str(payload.message_id)][str(payload.emoji)]))
                if role in member.roles:
                    await member.remove_roles(role)

            else:
                pass

def setup(React: commands.Bot):
    React.add_cog(Event(React))