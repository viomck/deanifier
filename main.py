import discord
import os
import re
import eng_to_ipa

client = discord.Client()

def main():
    client.run(os.getenv("BOT_TOKEN"))

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    words = message.clean_content.lower().split(" ")
    words = list(map(lambda w: re.sub("[^A-z]", "", w), words))

    for word in words:
        ipa = eng_to_ipa.convert(word)
        if (ipa.startswith("di") or ipa.startswith("dɪ")) and word.startswith("de") and word != "dean":
            await message.channel.send(word.replace("de", "dean"))

if __name__ == "__main__":
    main()
