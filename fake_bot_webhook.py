from dhooks import Webhook
from dhooks import Embed
from datetime import date,datetime
import json

embed=Embed(
    title="Sucessful Checout!",
    url="https://twitter.com/_thecodingbunny?lang=en",
    color=65280,
    timestamp="now"
)

hook=Webhook("https://discordapp.com/api/webhooks/715950160185786399/uFNsHqIAsOCbiPiBFgUv-pozfLlZyondpi2uuIUjQbxcNuvFz2UedZcRH8dBH6Fo5-7T")
#Get webhook

now=datetime.now()
copped_time=now.strftime("||%Y%m%d\n%H:%M:%S||")
#Get time

store=input("Enter store name:")
#Get store

profile="||"+input("Enter profile:")+"||"
#Get profile

product_image=input("Enter product image link:")
#Get image

product_name=input("Enter product name:")
#Get product name

size=input("Enter product size:")
#Get size

price="$"+input("Enter the price:")
#Get price

order_number="||"+input("Enter order number:")+"||"
#Get order number



embed.add_field(name="Date Time",value=copped_time)
embed.add_field(name="Store",value=store)
embed.add_field(name="Profile",value=profile)
embed.add_field(name="Product",value=product_name)
embed.add_field(name="Size",value=size)
embed.add_field(name="Price",value=price)
embed.add_field(name="Order Number",value=order_number)
embed.set_thumbnail(product_image)
#Embed elements


embed.set_footer(text="@theGaneshBot",icon_url="https://ganeshbot.com/public/images/logo-transparent.png")

hook.send(embed=embed)







