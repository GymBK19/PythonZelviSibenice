import turtle
from copy import copy
import random
import string
import io
import unicodedata

# SETTINGS START
strPressAnyLetter = "Zmackni pismeno"
strYouFailed = "Prohra"
strYouWon = "Vyhra"
strScreenTitle = "Sibenice"

hint = True  # Show right answer in console
sourceFile = "source.txt"  # File with words, each on separate line
turtleFont = ("Liberation Sans", 40, "normal")
# SETTINGS END
STATE_WAITING4GAME = 0
STATE_PLAYING = 1
STATE_AFTERGAME = 2
STATE_BUSY = 4

state = STATE_WAITING4GAME

word_unmasked = None
word_masked = None
tries_left = None

sibeniceDrawer = turtle.clone()
sibeniceDrawer.hideturtle()
sibeniceDrawed = 0
sibeniceTriesMax = 11
sibeniceSize = 100


def remove_diacritics(s):
    """Removes all diacritics characters from string
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def newRandomWord():
    """Gets random line from sourceFile
    """
    global word_unmasked, word_masked, tries_left, sibeniceDrawed, sibeniceDrawer, sibeniceTriesMax, sibeniceSize
    fileManager = io.open(sourceFile, 'r')
    readText = fileManager.read()
    fileManager.close()
    lines = readText.split("\n")
    slovo = lines[random.randrange(len(lines))].lower()
    del lines
    if (hint): print("Hint: %s" % slovo)
    word_unmasked = list(slovo)
    word_masked = copy(word_unmasked)
    tries_left = sibeniceTriesMax

    # Mask every character
    for i in range(len(word_unmasked)):
        word_masked[i] = "_"

    # Reset drawers
    turtle.pencolor("black")
    sibeniceDrawer.reset()
    sibeniceDrawer.penup()
    sibeniceDrawer.hideturtle()
    sibeniceDrawer.pencolor("red")
    sibeniceDrawed = 0
    sibeniceDrawer.right(90)
    sibeniceDrawer.forward(sibeniceSize * 1.5)
    sibeniceDrawer.right(90)
    sibeniceDrawer.forward(sibeniceSize * 2)
    sibeniceDrawer.speed(0)


turtle.hideturtle()
turtle.penup()
screen = turtle.getscreen()
screen.title(strScreenTitle)


def string_join_python27(list2Join):
    """Quick replacement for string.join from python 2.7
    Joins list of strings into one, serarating them by space
    """
    s = "";
    for ch in list2Join:
        s += ch + " ";
    return s[:-1];


def drawWord():
    """Draws masked word
    If character is not know yet, draws underline
    """
    global word_masked;
    turtle.goto(10, 50)
    turtle.write(string_join_python27(word_masked).upper(), move=False, align="CENTER", font=turtleFont)


def drawSibenice():
    """Draws that thing, where you will be hanged.
    Based on failed tries count
    """
    global tries_left, sibeniceDrawed, sibeniceTriesMax, sibeniceSize, state
    deltaTries = (sibeniceTriesMax - tries_left)  # How many failed attemps do we have to paint
    if (sibeniceDrawed == deltaTries):  # We have already painted all bad attemps
        return
    sibeniceDrawer.pendown()
    if (deltaTries == 1):
        sibeniceDrawer.right(180)
        sibeniceDrawer.forward(sibeniceSize)
    elif (deltaTries == 2):
        xcor2 = sibeniceDrawer.xcor() - sibeniceSize
        ycor2 = sibeniceDrawer.ycor()
        xcor1 = sibeniceDrawer.xcor() - (sibeniceSize / 2)
        ycor1 = sibeniceDrawer.ycor() + (sibeniceSize / 3)
        sibeniceDrawer.goto(xcor1, ycor1)
        sibeniceDrawer.goto(xcor2, ycor2)
        sibeniceDrawer.goto(xcor1, ycor1)
    elif (deltaTries == 3):
        sibeniceDrawer.goto(sibeniceDrawer.xcor(), sibeniceDrawer.ycor() + sibeniceSize)
    elif (deltaTries == 4):
        sibeniceDrawer.forward(sibeniceSize)
    elif (deltaTries == 5):
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        moveX = startX - sibeniceSize
        moveY = startY - (sibeniceSize * 2 / 10)
        sibeniceDrawer.right(180)
        sibeniceDrawer.forward(sibeniceSize * 8 / 10)
        sibeniceDrawer.goto(moveX, moveY)
        sibeniceDrawer.penup()
        sibeniceDrawer.goto(startX, startY)
    elif (deltaTries == 6):
        sibeniceDrawer.left(90)
        sibeniceDrawer.forward(sibeniceSize / 5)
    elif (deltaTries == 7):
        sibeniceDrawer.right(90)
        sibeniceDrawer.circle(sibeniceSize / 10)
    elif (deltaTries == 8):
        sibeniceDrawer.left(90)
        sibeniceDrawer.penup()
        sibeniceDrawer.forward(sibeniceSize / 5)
        sibeniceDrawer.pendown()
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        sibeniceDrawer.forward(sibeniceSize / 4)
        sibeniceDrawer.goto(startX, startY)
    elif (deltaTries == 9):
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        sibeniceDrawer.right(45)
        sibeniceDrawer.forward(sibeniceSize / 3)
        sibeniceDrawer.goto(startX, startY)
    elif (deltaTries == 10):
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        sibeniceDrawer.left(90)
        sibeniceDrawer.forward(sibeniceSize / 3)
        sibeniceDrawer.goto(startX, startY)
        sibeniceDrawer.right(45)
        sibeniceDrawer.forward(sibeniceSize / 4)
    elif (deltaTries == 11):
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        sibeniceDrawer.right(45)
        sibeniceDrawer.forward(sibeniceSize / 3)
        sibeniceDrawer.goto(startX, startY)
    elif (deltaTries == 12):
        startX = sibeniceDrawer.xcor()
        startY = sibeniceDrawer.ycor()
        sibeniceDrawer.left(90)
        sibeniceDrawer.forward(sibeniceSize / 3)
        sibeniceDrawer.goto(startX, startY)
        sibeniceDrawer.write(strYouFailed, move=False, align="CENTER", font=turtleFont)
        unmaskWord("red")
        state = STATE_AFTERGAME
    sibeniceDrawer.penup()
    sibeniceDrawed = deltaTries


def redraw():
    """Draws UI, based on current state
    """
    global state
    turtle.clear()
    if (state == STATE_PLAYING):
        drawWord()
        drawSibenice()
    elif (state == STATE_WAITING4GAME):
        turtle.write(strPressAnyLetter, move=False, align="CENTER", font=turtleFont)
    elif (state == STATE_AFTERGAME):
        drawWord()


def unmaskWord(textColor):
    """Shows word as unmasked with come color
    """
    global word_masked, word_unmasked
    turtle.pencolor("black")

    # Remove every good character, so we have space for writing in red
    turtle.clear()
    for i in range(len(word_unmasked)):
        word_masked[i] = "_";
    drawWord()

    turtle.pencolor("red")

    word_masked = copy(word_unmasked)
    drawWord()
    turtle.pencolor("black")


def update(inputText):
    """Processes input character and draws unmasked word
    """
    global state
    if (state == STATE_BUSY):
        return
    if (state == STATE_WAITING4GAME and inputText != None):
        state = STATE_BUSY
        newRandomWord()
        state = STATE_PLAYING
    elif (state == STATE_PLAYING):
        checkLetter(inputText)
    elif (state == STATE_AFTERGAME):
        state = STATE_WAITING4GAME
    redraw()


def checkLetter(inputText):
    """Checks if this letter is located inside word.
    If yes, fills it
    Otherwise decreases tries left count
    """
    global tries_left, word_unmasked, word_masked, state
    pismeno_spravne = False
    for i in range(len(word_unmasked)):
        if (inputText == word_unmasked[i]):
            word_masked[i] = word_unmasked[i]
            pismeno_spravne = True
    if (not pismeno_spravne):
        tries_left -= 1
    if (word_masked == word_unmasked):
        sibeniceDrawer.pencolor("green")
        sibeniceDrawer.write(strYouWon, move=False, align="CENTER", font=turtleFont)
        state = STATE_AFTERGAME


# Define keys
def a():
    update("a")


def b():
    update("b")


def c():
    update("c")


def d():
    update("d")


def e():
    update("e")


def f():
    update("f")


def g():
    update("g")


def h():
    update("h")


def i():
    update("i")


def j():
    update("j")


def k():
    update("k")


def l():
    update("l")


def m():
    update("m")


def n():
    update("n")


def o():
    update("o")


def p():
    update("p")


def q():
    update("q")


def r():
    update("r")


def s():
    update("s")


def t():
    update("t")


def u():
    update("u")


def v():
    update("v")


def w():
    update("w")


def x():
    update("x")


def y():
    update("y")


def z():
    update("z")


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
# End define keys

screen.listen()

update(None)

turtle.getscreen()._root.mainloop()