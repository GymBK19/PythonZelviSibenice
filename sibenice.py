import turtle
from copy import copy
import random
import string
import io
import unicodedata

debug = True;
sourceFile = "source.txt"; #File with words, each on separate line
	
slovo_odmaskovane = None;
slovo_maskovane = None;
slovo_zjisteno = False;
pokusu_zbyva = 6;


def remove_diacritics(s):
	"""Removes all diacritics characters from string
	"""
	return ''.join(c for c in unicodedata.normalize('NFD', s)
		if unicodedata.category(c) != 'Mn')
                  
def newRandomWord():
	"""Gets random line from sourceFile
	"""
	global slovo_odmaskovane, slovo_maskovane;
	fileManager = io.open(sourceFile,'r');
	readText = fileManager.read();
	fileManager.close();
	lines = readText.split("\n");
	slovo = lines[random.randrange(len(lines))].lower();
	del lines;
	if(debug): print("Hint: %s" % slovo);
	slovo_odmaskovane = list(slovo);
	slovo_maskovane = copy(slovo_odmaskovane);


newRandomWord();
turtle.hideturtle()
screen = turtle.getscreen()

def drawWord():
	"""Draws masked word
	If character is not know yet, draws underline
	"""
	turtle.clear()
	turtle.write(string.join(slovo_maskovane).upper(), move=False, align="CENTER", font=("Liberation Sans", 40, "normal"))
	
def processInput_frontend(inputText):
	"""Processes input character and draws unmasked word
	"""
	processInput_backend(inputText);
	drawWord();

def processInput_backend(inputText):
	global pokusu_zbyva, slovo_odmaskovane, slovo_maskovane;
	print(string.join(slovo_maskovane,""))
	print("Zbyva %d pokusu" % pokusu_zbyva)
	global pokusu_zbyva
	if(pokusu_zbyva <= 0):
		#User looses
		slovo_zjisteno = True
		return
	if(slovo_maskovane == slovo_odmaskovane):
		#User won
		print("Zjistil jsi slovo %s" % string.join(slovo_odmaskovane))
		slovo_zjisteno = True
		return
	pismeno_spravne = False
	for i in range(len(slovo_odmaskovane)):
		if(inputText == slovo_odmaskovane[i]):
			slovo_maskovane[i] = slovo_odmaskovane[i]
			pismeno_spravne = True
	if(not pismeno_spravne):
		pokusu_zbyva-=1
		

#Mask every character
for i in range(len(slovo_odmaskovane)):
    slovo_maskovane[i] = "_";

#Define keys
def a():
	processInput_frontend("a");
def b():
	processInput_frontend("b");
def c():
	processInput_frontend("c");
def d():
	processInput_frontend("d");
def e():
	processInput_frontend("e");
def f():
	processInput_frontend("f");
def g():
	processInput_frontend("g");
def h():
	processInput_frontend("h");
def i():
	processInput_frontend("i");
def j():
	processInput_frontend("j");
def k():
	processInput_frontend("k");
def l():
	processInput_frontend("l");
def m():
	processInput_frontend("m");
def n():
	processInput_frontend("n");
def o():
	processInput_frontend("o");
def p():
	processInput_frontend("p");
def q():
	processInput_frontend("q");
def r():
	processInput_frontend("r");
def s():
	processInput_frontend("s");
def t():
	processInput_frontend("t");
def u():
	processInput_frontend("u");
def v():
	processInput_frontend("v");
def w():
	processInput_frontend("w");
def x():
	processInput_frontend("x");
def y():
	processInput_frontend("y");
def z():
	processInput_frontend("z");
screen.onkey(a, "a")
screen.onkey(b, "b")
screen.onkey(c, "c")
screen.onkey(d, "d")
screen.onkey(e, "e")
screen.onkey(f, "f")
screen.onkey(g, "g")
screen.onkey(h, "h")
screen.onkey(i, "i")
screen.onkey(j, "j")
screen.onkey(k, "k")
screen.onkey(l, "l")
screen.onkey(m, "m")
screen.onkey(n, "n")
screen.onkey(o, "o")
screen.onkey(p, "p")
screen.onkey(q, "q")
screen.onkey(r, "r")
screen.onkey(s, "s")
screen.onkey(t, "t")
screen.onkey(u, "u")
screen.onkey(v, "v")
screen.onkey(w, "w")
screen.onkey(x, "x")
screen.onkey(y, "y")
screen.onkey(z, "z")
#End define keys

screen.listen()

drawWord()

input();
