import pyfiglet
#import random


#font=random.choice(pyfiglet.FigletFont.getFonts())
ascii_art=pyfiglet.figlet_format("Eid-ul-Adha", font="big")
greeting=f"{ascii_art}\nEid-ul-Adha Mubarak!\n {ascii_art}"
print(greeting)