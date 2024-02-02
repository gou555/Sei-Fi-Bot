import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("The bot is ready")
    print("----------------")


@client.command()
async def links(ctx):
    embed = discord.Embed(title="OFFICIAL LINKS", description="━━━━━━━━━━━━━━━━━━", color=0x00ff00)
    embed.add_field(name="Twitter", value="https://twitter.com/SeiFiNFT", inline=False)
    embed.add_field(name="Discord", value="https://discord.gg/zNhQKjF8", inline=False)
    embed.add_field(name="Website", value="https://sei-fi.com/", inline=False)
    embed.add_field(name="", value="\u200b", inline=False)
    willg_discord_mention = "<@654058499122397184>"
    nopaajJ_discord_mention = "<@638045784000036885>"
    tnc_discord_mention = "<@775423863429398578>"
    team_info = (f"{willg_discord_mention} | Twitter: https://twitter.com/willG555_\n"
                f"{nopaajJ_discord_mention} | Twitter: https://twitter.com/nopaajJ\n"
                f"{tnc_discord_mention} | Twitter: https://twitter.com/tncmv")

    embed.add_field(name="**TEAMS**", value="", inline=False)
    embed.add_field(name="", value=team_info, inline=False)
    embed.set_image(url="https://i.imgur.com/mfK438m.png")
    await ctx.send(embed=embed)



@client.command()
async def sei_info(ctx):
    embed = discord.Embed(title="What is Sei?", color=0x00ff00)
    embed.description = (
        "Sei is a general purpose, open-source Layer 1 blockchain specialized for the exchange of digital assets. "
        "Leveraging a novel consensus and technical breakthroughs, Sei is the fastest blockchain in the industry.\n\n"
        
        "A common misconception is that Sei is a DeFi chain. However, the exchange of digital assets is universal "
        "across gaming, social, and NFTs. Trading is general purpose.\n\n"
        
        "We’ve made this guide to help you get started on the new SEI Mainnet adventure. The Compass team is always "
        "by your side as you take the plunge, and embark on new journeys."
    )
    
    embed.add_field(
        name="The Basics",
        value=(
            "🧭How to create a Sei wallet using Compass Wallet?\n"
            "https://seistartguide.addpotion.com/how-to-create-a-sei-wallet-using-compass-wallet\n"
            "📲How to Install a Sei Wallet using the Compass Wallet Android app?\n"
            "https://seistartguide.addpotion.com/how-to-install-a-sei-wallet-using-the-compass-wallet-android-app\n"
            "🌉How to bridge funds from Ethereum & other blockchains into your Sei wallet?\n"
            "https://seistartguide.addpotion.com/how-to-bridge-funds-from-ethereum-other-blockchains-into-your-sei-wallet\n"
            "📤How to bridge funds from Sei to Ethereum & other blockchains using your Sei Wallet?\n"
            "https://seistartguide.addpotion.com/how-to-bridge-funds-from-sei-to-ethereum-other-blockchains-using-your-sei-wallet\n"
        ),
        inline=False
    )
    
    embed.add_field(
        name="Doing more with your $SEI",
        value=(
            "🏦How to Stake $SEI?\n"
            "https://seistartguide.addpotion.com/how-to-stake-sei\n"
            "📈How to trade Perps or open Long/Short positions on Levana?\n"
            "https://seistartguide.addpotion.com/how-to-trade-perps-or-open-longshort-positions-on-levana\n"
            "🎲How to participate in Sensei Fi’s gamified Defi using Compass Wallet?\n"
            "https://seistartguide.addpotion.com/how-to-participate-in-sensei-fis-gamified-defi-using-compass-wallet\n"
        ),
        inline=False
    )
    
    embed.add_field(
        name="About Compass",
        value=(
            "Compass Wallet is an extension built exclusively for Seilors. We've thought of the needs of every explorer "
            "on the blazing-fast L1 and created a wallet that can fulfill each requirement.\n"
            "Website: https://compasswallet.io/"
        ),
        inline=False
    )
    
    await ctx.send(embed=embed)

@client.command()
async def faq(ctx):
    embed = discord.Embed(title="SEI-FI NFT FAQ", color=0x00ff00)
    embed.add_field(name="**What are the benefits of holding an SEI-FI NFT?**",
                    value=("As a holder of an SEI-FI NFT, you will gain access to a 50% Profit Share from all current "
                           "and future arcade games developed on the Sei-Fi platform. Our roadmap also includes  "
                           "the exciting addition of PVP sports betting, raffles and more. We aim to establish a group of alpha "
                           "callers, providing insights into NFT trading, whitelist opportunities, airdrops, and more!"),
                    inline=False)
    embed.add_field(name="**How much revenue goes to holders?**",
                    value="50% of profit generated from the games will go to holders.",
                    inline=False)
    embed.add_field(name="**When is the mint date for Sei-Fi?**",
                    value="Our mint date is TBA",
                    inline=False)
    embed.add_field(name="**What is the collection size and mint price?**",
                    value="The collection size is 999 and mint price is TBA for WL.",
                    inline=False)
    await ctx.send(embed=embed)

@client.command()
async def about(ctx):
    embed = discord.Embed(title="About Sei-Fi", color=0x00ff00)
    embed.add_field(name="**Mission**",
                    value=("Sei-Fi aim to be a significant and innovative project on the SEI network. "
                           "We are dedicated to creating a vibrant platform that unite the Sei ecosystem. "
                           "Our vision is not just to participate in the Sei ecosystem but to be a driving "
                           "force in its expansion and success. We believe in the immense potentiel of the Sei network "
                           "and we're committed to being a key part of this journey."     ),
                    inline=False)
    embed.add_field(name="**Art**",
                    value=("Each piece in the Sei-Fi collection is completely unique. The collection have "
                           "80+ differents traits. The Sei-Fi is just a masterpiece in itself. Thanks to our chad "
                           "artist @younes"),
                    inline=False)

    embed.add_field(name="**Socials**",
                    value=("Website: https://sei-fi.com/\n"
                           "Twitter: https://twitter.com/SeiFiNFT"),
                    inline=False)            
   
    await ctx.send(embed=embed)
client.run('YOUR TOKEN')



