import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	async def spam(self, ctx, user: discord.Member, number: int, spam_text: str=None):
		"""Spam The User hehe"""
		if spam_text == None:
			await self.bot.say('Wait What Dude Want To Spam Sombody Nothing Wew')
			return
		for i in range(number):
			await self.bot.send_message(user, spam_text)
			
def setup(bot):
	bot.add_cog(Spam(bot))
