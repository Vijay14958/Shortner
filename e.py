from f import *
import aiohttp

start_message = """<b>
Hey There, {}
π I Can Convert Link To TamizhMasters ShortLink
π¬ Send Me Any Message With Links
π I Will Shorten All Links In It 
π Convert to <a href="https://tamizhmasters.com/member/tools/bookmarklet">TamizhMasters</a> 

Β©οΈPowered By @simplysouth_links
</b>"""
start_button = [[Button.url("Join Channel β₯οΈ", "t.me/tamizhmastersofficial"), Button.inline("About Bot π€", "abt")],
                [Button.url("Connect To Shortner π", "https://tamizhmasters.com/member/tools/api")]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [[Button.url("Shorturllink.in", "https://shorturllink.in/member/tools/bookmarklet")],
              [Button.url("Playdisk.xyz", "https://playdisk.xyz/member/tools/bookmarklet")]]


about_text = """<b>

π€ Name :  TamizhMasters Link Convertor

π  Language  : Python3
π Library   : Telethon
π Owner     : @Bavabee
π§π»βπ» Developer : @Yali_Kk & @HMF_Owner_1

Β©οΈPowered By @simplysouth_links</b>"""
back_button = [Button.inline("βͺ Back", "back")]

