import os,sys,time
from time import *

r='\x1b[00m\x1b[91m'
g='\x1b[00m\x1b[32m'
y='\x1b[00m\x1b[33m'
c='\x1b[00m\x1b[36m'
w='\x1b[00m'
u='\033[4m'
b='\033[5m'

def sprint(s):
   for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)
        
def corrupt():
	print(r+'[?]'+w+' Command not found, pleade type help')
        
def exit():
	print(r+'[!]'+w+' The user forces it to stop')
	primt(r+'[!]'+w+' Exiting tool')
	
def help():
		print('')
		print('command                                example')
		print('-------                                -------')
		print('set text [your text]        set text iqbalmh18')
		print('run, go, create                         create')
		print('')
		
def all_main():
	global text
	while True:
		am = input(w+'saydog('+r+'text2ascii/all'+w+') > '+w)
		if am == 'help':
			help()
		elif am == 'exit':
			exit()
			sys.exit(1)
		elif 'set text' in am:
			text = am.split()[(-1)]
			print('text > '+text)
		elif am == 'run' or am == 'create' or am == 'go':
			try:
				os.system('figlet -f "1Row" "'+text+'"')
				os.system('figlet -f "3-D" "'+text+'"')
				os.system('figlet -f "3D Diagonal" "'+text+'"')
				os.system('figlet -f "3D-ASCII" "'+text+'"')
				os.system('figlet -f "3x5" "'+text+'"')
				os.system('figlet -f "4Max" "'+text+'"')
				os.system('figlet -f "5 Line Oblique" "'+text+'"')
				os.system('figlet -f "AMC 3 Line" "'+text+'"')
				os.system('figlet -f "AMC 3 Liv1" "'+text+'"')
				os.system('figlet -f "AMC AAA01" "'+text+'"')
				os.system('figlet -f "AMC Neko" "'+text+'"')
				os.system('figlet -f "AMC Razor" "'+text+'"')
				os.system('figlet -f "AMC Razor2" "'+text+'"')
				os.system('figlet -f "AMC Slash" "'+text+'"')
				os.system('figlet -f "AMC Slider" "'+text+'"')
				os.system('figlet -f "AMC Thin" "'+text+'"')
				os.system('figlet -f "AMC Tubes" "'+text+'"')
				os.system('figlet -f "AMC Untitled" "'+text+'"')
				os.system('figlet -f "ANSI Shadow" "'+text+'"')
				os.system('figlet -f "ASCII New Roman" "'+text+'"')
				os.system('figlet -f "Acrobatic" "'+text+'"')
				os.system('figlet -f "Alligator" "'+text+'"')
				os.system('figlet -f "Alligator2" "'+text+'"')
				os.system('figlet -f "Alpha" "'+text+'"')
				os.system('figlet -f "Alphabet" "'+text+'"')
				os.system('figlet -f "Arrows" "'+text+'"')
				os.system('figlet -f "Avatar" "'+text+'"')
				os.system('figlet -f "B1FF" "'+text+'"')
				os.system('figlet -f "Banner" "'+text+'"')
				os.system('figlet -f "Banner3-D" "'+text+'"')
				os.system('figlet -f "Banner3" "'+text+'"')
				os.system('figlet -f "Banner4" "'+text+'"')
				os.system('figlet -f "Barbwire" "'+text+'"')
				os.system('figlet -f "Basic" "'+text+'"')
				os.system('figlet -f "Bear" "'+text+'"')
				os.system('figlet -f "Bell" "'+text+'"')
				os.system('figlet -f "Benjamin" "'+text+'"')
				os.system('figlet -f "Big Chief" "'+text+'"')
				os.system('figlet -f "Big Money-ne" "'+text+'"')
				os.system('figlet -f "Big Money-nw" "'+text+'"')
				os.system('figlet -f "Big Money-se" "'+text+'"')
				os.system('figlet -f "Big Money-sw" "'+text+'"')
				os.system('figlet -f "Big" "'+text+'"')
				os.system('figlet -f "Bigfig" "'+text+'"')
				os.system('figlet -f "Binary" "'+text+'"')
				os.system('figlet -f "Block" "'+text+'"')
				os.system('figlet -f "Blocks" "'+text+'"')
				os.system('figlet -f "Bloody" "'+text+'"')
				os.system('figlet -f "Bolger" "'+text+'"')
				os.system('figlet -f "Braced" "'+text+'"')
				os.system('figlet -f "Bright" "'+text+'"')
				os.system('figlet -f "Broadway KB" "'+text+'"')
				os.system('figlet -f "Broadway" "'+text+'"')
				os.system('figlet -f "Bubble" "'+text+'"')
				os.system('figlet -f "Bulbhead" "'+text+'"')
				os.system('figlet -f "Caligraphy" "'+text+'"')
				os.system('figlet -f "Caligraphy2" "'+text+'"')
				os.system('figlet -f "Calvin S" "'+text+'"')
				os.system('figlet -f "Cards" "'+text+'"')
				os.system('figlet -f "Catwalk" "'+text+'"')
				os.system('figlet -f "Chiseled" "'+text+'"')
				os.system('figlet -f "Chunky" "'+text+'"')
				os.system('figlet -f "Coinstak" "'+text+'"')
				os.system('figlet -f "Cola" "'+text+'"')
				os.system('figlet -f "Colossal" "'+text+'"')
				os.system('figlet -f "Computer" "'+text+'"')
				os.system('figlet -f "Contessa" "'+text+'"')
				os.system('figlet -f "Contrast" "'+text+'"')
				os.system('figlet -f "Cosmike" "'+text+'"')
				os.system('figlet -f "Crawford" "'+text+'"')
				os.system('figlet -f "Crawford2" "'+text+'"')
				os.system('figlet -f "Crazy" "'+text+'"')
				os.system('figlet -f "Cricket" "'+text+'"')
				os.system('figlet -f "Cursive" "'+text+'"')
				os.system('figlet -f "Cyberlarge" "'+text+'"')
				os.system('figlet -f "Cybermedium" "'+text+'"')
				os.system('figlet -f "Cybersmall" "'+text+'"')
				os.system('figlet -f "Cygnet" "'+text+'"')
				os.system('figlet -f "DANC4" "'+text+'"')
				os.system('figlet -f "DWhistled" "'+text+'"')
				os.system('figlet -f "Dancing Font" "'+text+'"')
				os.system('figlet -f "Decimal" "'+text+'"')
				os.system('figlet -f "Def Leppard" "'+text+'"')
				os.system('figlet -f "Delta Corps Priest 1" "'+text+'"')
				os.system('figlet -f "Diamond" "'+text+'"')
				os.system('figlet -f "Diet Cola" "'+text+'"')
				os.system('figlet -f "Digital" "'+text+'"')
				os.system('figlet -f "Doh" "'+text+'"')
				os.system('figlet -f "Doom" "'+text+'"')
				os.system('figlet -f "Dot Matrix" "'+text+'"')
				os.system('figlet -f "Double Shorts" "'+text+'"')
				os.system('figlet -f "Double" "'+text+'"')
				os.system('figlet -f "Dr Pepper" "'+text+'"')
				os.system('figlet -f "Efti Chess" "'+text+'"')
				os.system('figlet -f "Efti Font" "'+text+'"')
				os.system('figlet -f "Efti Italic" "'+text+'"')
				os.system('figlet -f "Efti Piti" "'+text+'"')
				os.system('figlet -f "Efti Robot" "'+text+'"')
				os.system('figlet -f "Efti Wall" "'+text+'"')
				os.system('figlet -f "Efti Water" "'+text+'"')
				os.system('figlet -f "Electronic" "'+text+'"')
				os.system('figlet -f "Elite" "'+text+'"')
				os.system('figlet -f "Epic" "'+text+'"')
				os.system('figlet -f "Fender" "'+text+'"')
				os.system('figlet -f "Filter" "'+text+'"')
				os.system('figlet -f "Fire Font-k" "'+text+'"')
				os.system('figlet -f "Fire Font-s" "'+text+'"')
				os.system('figlet -f "Flipped" "'+text+'"')
				os.system('figlet -f "Flower Power" "'+text+'"')
				os.system('figlet -f "Four Tops" "'+text+'"')
				os.system('figlet -f "Fraktur" "'+text+'"')
				os.system('figlet -f "Fun Face" "'+text+'"')
				os.system('figlet -f "Fun Faces" "'+text+'"')
				os.system('figlet -f "Fuzzy" "'+text+'"')
				os.system('figlet -f "Georgi16" "'+text+'"')
				os.system('figlet -f "Georgia11" "'+text+'"')
				os.system('figlet -f "Ghost" "'+text+'"')
				os.system('figlet -f "Ghoulish" "'+text+'"')
				os.system('figlet -f "Glenyn" "'+text+'"')
				os.system('figlet -f "Goofy" "'+text+'"')
				os.system('figlet -f "Gothic" "'+text+'"')
				os.system('figlet -f "Graceful" "'+text+'"')
				os.system('figlet -f "Gradient" "'+text+'"')
				os.system('figlet -f "Graffiti" "'+text+'"')
				os.system('figlet -f "Greek" "'+text+'"')
				os.system('figlet -f "Heart Left" "'+text+'"')
				os.system('figlet -f "Heart Right" "'+text+'"')
				os.system('figlet -f "Henry 3D" "'+text+'"')
				os.system('figlet -f "Hex" "'+text+'"')
				os.system('figlet -f "Hieroglyphs" "'+text+'"')
				os.system('figlet -f "Hollywood" "'+text+'"')
				os.system('figlet -f "Horizontal Left" "'+text+'"')
				os.system('figlet -f "Horizontal Right" "'+text+'"')
				os.system('figlet -f "ICL-1900" "'+text+'"')
				os.system('figlet -f "Impossible" "'+text+'"')
				os.system('figlet -f "Invita" "'+text+'"')
				os.system('figlet -f "Isometric1" "'+text+'"')
				os.system('figlet -f "Isometric2" "'+text+'"')
				os.system('figlet -f "Isometric3" "'+text+'"')
				os.system('figlet -f "Isometric4" "'+text+'"')
				os.system('figlet -f "Italic" "'+text+'"')
				os.system('figlet -f "Ivrit" "'+text+'"')
				os.system('figlet -f "JS Block Letters" "'+text+'"')
				os.system('figlet -f "JS Bracket Letters" "'+text+'"')
				os.system('figlet -f "JS Capital Curves" "'+text+'"')
				os.system('figlet -f "JS Cursive" "'+text+'"')
				os.system('figlet -f "JS Stick Letters" "'+text+'"')
				os.system('figlet -f "Jacky" "'+text+'"')
				os.system('figlet -f "Jazmine" "'+text+'"')
				os.system('figlet -f "Jerusalem" "'+text+'"')
				os.system('figlet -f "Katakana" "'+text+'"')
				os.system('figlet -f "Kban" "'+text+'"')
				os.system('figlet -f "Keyboard" "'+text+'"')
				os.system('figlet -f "Knob" "'+text+'"')
				os.system('figlet -f "Konto Slant" "'+text+'"')
				os.system('figlet -f "Konto" "'+text+'"')
				os.system('figlet -f "LCD" "'+text+'"')
				os.system('figlet -f "Larry 3D 2" "'+text+'"')
				os.system('figlet -f "Larry 3D" "'+text+'"')
				os.system('figlet -f "Lean" "'+text+'"')
				os.system('figlet -f "Letters" "'+text+'"')
				os.system('figlet -f "Lil Devil" "'+text+'"')
				os.system('figlet -f "Line Blocks" "'+text+'"')
				os.system('figlet -f "Linux" "'+text+'"')
				os.system('figlet -f "Lockergnome" "'+text+'"')
				os.system('figlet -f "Madrid" "'+text+'"')
				os.system('figlet -f "Marquee" "'+text+'"')
				os.system('figlet -f "Maxfour" "'+text+'"')
				os.system('figlet -f "Merlin1" "'+text+'"')
				os.system('figlet -f "Merlin2" "'+text+'"')
				os.system('figlet -f "Mike" "'+text+'"')
				os.system('figlet -f "Mini" "'+text+'"')
				os.system('figlet -f "Mirror" "'+text+'"')
				os.system('figlet -f "Mnemonic" "'+text+'"')
				os.system('figlet -f "Modular" "'+text+'"')
				os.system('figlet -f "Morse" "'+text+'"')
				os.system('figlet -f "Morse2" "'+text+'"')
				os.system('figlet -f "Moscow" "'+text+'"')
				os.system('figlet -f "Mshebrew210" "'+text+'"')
				os.system('figlet -f "Muzzle" "'+text+'"')
				os.system('figlet -f "NScript" "'+text+'"')
				os.system('figlet -f "NT Greek" "'+text+'"')
				os.system('figlet -f "NV Script" "'+text+'"')
				os.system('figlet -f "Nancyj-Fancy" "'+text+'"')
				os.system('figlet -f "Nancyj-Improved" "'+text+'"')
				os.system('figlet -f "Nancyj-Underlined" "'+text+'"')
				os.system('figlet -f "Nancyj" "'+text+'"')
				os.system('figlet -f "Nipples" "'+text+'"')
				os.system('figlet -f "O8" "'+text+'"')
				os.system('figlet -f "OS2" "'+text+'"')
				os.system('figlet -f "Octal" "'+text+'"')
				os.system('figlet -f "Ogre" "'+text+'"')
				os.system('figlet -f "Old Banner" "'+text+'"')
				os.system('figlet -f "Patorjk-HeX" "'+text+'"')
				os.system('figlet -f "Pawp" "'+text+'"')
				os.system('figlet -f "Peaks Slant" "'+text+'"')
				os.system('figlet -f "Peaks" "'+text+'"')
				os.system('figlet -f "Pebbles" "'+text+'"')
				os.system('figlet -f "Pepper" "'+text+'"')
				os.system('figlet -f "Poison" "'+text+'"')
				os.system('figlet -f "Puffy" "'+text+'"')
				os.system('figlet -f "Puzzle" "'+text+'"')
				os.system('figlet -f "Pyramid" "'+text+'"')
				os.system('figlet -f "Rammstein" "'+text+'"')
				os.system('figlet -f "Rectangles" "'+text+'"')
				os.system('figlet -f "Red Phoenix" "'+text+'"')
				os.system('figlet -f "Relief" "'+text+'"')
				os.system('figlet -f "Relief2" "'+text+'"')
				os.system('figlet -f "Reverse" "'+text+'"')
				os.system('figlet -f "Roman" "'+text+'"')
				os.system('figlet -f "Rot13" "'+text+'"')
				os.system('figlet -f "Rotated" "'+text+'"')
				os.system('figlet -f "Rounded" "'+text+'"')
				os.system('figlet -f "Rowan Cap" "'+text+'"')
				os.system('figlet -f "Rozzo" "'+text+'"')
				os.system('figlet -f "Runic" "'+text+'"')
				os.system('figlet -f "Runyc" "'+text+'"')
				os.system('figlet -f "S Blood" "'+text+'"')
				os.system('figlet -f "SL Script" "'+text+'"')
				os.system('figlet -f "Santa Clara" "'+text+'"')
				os.system('figlet -f "Script" "'+text+'"')
				os.system('figlet -f "Serifcap" "'+text+'"')
				os.system('figlet -f "Shadow" "'+text+'"')
				os.system('figlet -f "Shimrod" "'+text+'"')
				os.system('figlet -f "Short" "'+text+'"')
				os.system('figlet -f "Slant Relief" "'+text+'"')
				os.system('figlet -f "Slant" "'+text+'"')
				os.system('figlet -f "Slide" "'+text+'"')
				os.system('figlet -f "Small Caps" "'+text+'"')
				os.system('figlet -f "Small Isometric1" "'+text+'"')
				os.system('figlet -f "Small Keyboard" "'+text+'"')
				os.system('figlet -f "Small Poison" "'+text+'"')
				os.system('figlet -f "Small Script" "'+text+'"')
				os.system('figlet -f "Small Shadow" "'+text+'"')
				os.system('figlet -f "Small Slant" "'+text+'"')
				os.system('figlet -f "Small Tengwar" "'+text+'"')
				os.system('figlet -f "Small" "'+text+'"')
				os.system('figlet -f "Soft" "'+text+'"')
				os.system('figlet -f "Speed" "'+text+'"')
				os.system('figlet -f "Spliff" "'+text+'"')
				os.system('figlet -f "Stacey" "'+text+'"')
				os.system('figlet -f "Stampate" "'+text+'"')
				os.system('figlet -f "Stampatello" "'+text+'"')
				os.system('figlet -f "Standard" "'+text+'"')
				os.system('figlet -f "Star Strips" "'+text+'"')
				os.system('figlet -f "Star Wars" "'+text+'"')
				os.system('figlet -f "Stellar" "'+text+'"')
				os.system('figlet -f "Stforek" "'+text+'"')
				os.system('figlet -f "Stick Letters" "'+text+'"')
				os.system('figlet -f "Stop" "'+text+'"')
				os.system('figlet -f "Straight" "'+text+'"')
				os.system('figlet -f "Stronger Than All" "'+text+'"')
				os.system('figlet -f "Sub-Zero" "'+text+'"')
				os.system('figlet -f "Swamp Land" "'+text+'"')
				os.system('figlet -f "Swan" "'+text+'"')
				os.system('figlet -f "Sweet" "'+text+'"')
				os.system('figlet -f "THIS" "'+text+'"')
				os.system('figlet -f "Tanja" "'+text+'"')
				os.system('figlet -f "Tengwar" "'+text+'"')
				os.system('figlet -f "Term" "'+text+'"')
				os.system('figlet -f "Test1" "'+text+'"')
				os.system('figlet -f "The Edge" "'+text+'"')
				os.system('figlet -f "Thick" "'+text+'"')
				os.system('figlet -f "Thin" "'+text+'"')
				os.system('figlet -f "Thorned" "'+text+'"')
				os.system('figlet -f "Three Point" "'+text+'"')
				os.system('figlet -f "Ticks Slant" "'+text+'"')
				os.system('figlet -f "Ticks" "'+text+'"')
				os.system('figlet -f "Tiles" "'+text+'"')
				os.system('figlet -f "Tinker-Toy" "'+text+'"')
				os.system('figlet -f "Tombstone" "'+text+'"')
				os.system('figlet -f "Train" "'+text+'"')
				os.system('figlet -f "Trek" "'+text+'"')
				os.system('figlet -f "Tsalagi" "'+text+'"')
				os.system('figlet -f "Tubular" "'+text+'"')
				os.system('figlet -f "Twisted" "'+text+'"')
				os.system('figlet -f "Two Point" "'+text+'"')
				os.system('figlet -f "USA Flag" "'+text+'"')
				os.system('figlet -f "Univers" "'+text+'"')
				os.system('figlet -f "Varsity" "'+text+'"')
				os.system('figlet -f "Wavy" "'+text+'"')
				os.system('figlet -f "Weird" "'+text+'"')
				os.system('figlet -f "Wet Letter" "'+text+'"')
				os.system('figlet -f "Whimsy" "'+text+'"')
				os.system('figlet -f "Wow" "'+text+'"')
				os.system('figlet -f "" "'+text+'"')
			except KeyboardInterrupt:
				exit()
		else:
			corrupt()

all_main()