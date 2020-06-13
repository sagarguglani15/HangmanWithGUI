from tkinter import *
from words import choose_word
import string,random
from functools import partial

def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if(i in letters_guessed):
            pass
        else:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
        guessed_word+=' '
    return guessed_word

def get_available_letters(letters_guessed):
    s = string.ascii_lowercase
    l=list(s)
    for i in letters_guessed:
        try:
            l.remove(i)
        except:
            pass
    letters_left=''
    for i in l:
        letters_left+=i
    return letters_left

def setImage(n):
    global photo
    if(n==-1):
        c1 = Canvas(root, width=250, height=225, highlightthickness=0, bg='white', bd=2)
        c1.place(x=400, y=110)
        photo = PhotoImage(file=('hangman_images/life0.png'))
        c1.create_image(0, 0, image=photo, anchor='nw')
    else:
        c3 = Canvas(root, width=110, height=135, highlightthickness=0, bg='white', bd=2)
        c3.place(x=400, y=150)
        photo = PhotoImage(file=('hangman_images/l%s.png' % (str(n))))
        c3.create_image(0, 0, image=photo, anchor='nw')


root=Tk()
root.config(bg='cyan')
root.title('Dashboard')
root.geometry('1200x600')
root.title('Hangman by SAGAR GUGLANI')

bg = PhotoImage(file=('hangman_images/bg.png'))
Label(root,image=bg).place(relwidth=1,relheight=1)

secret_word = choose_word()
letters_guessed = []
global remaining_lives
remaining_lives=7
setImage(7)
hint=0
available_letters = get_available_letters(letters_guessed)

Lword=Label(root,text=' %s' %get_guessed_word(secret_word,letters_guessed),bg='white', fg='black', font='ABC 25 bold')
Lword.place(x=700, y=200)

def do(letter):
    global remaining_lives
    if(letter.lower() in secret_word):
        alphadic[letter].config(bg='green')
        alphadic[letter].config(state='disabled')
        letters_guessed.append(letter.lower())
        Lword.config(text=' %s' %get_guessed_word(secret_word,letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
            Label(root,text=' * * Congratulations, you won! * * ',bg='yellow',fg='red',font='ABC 20 bold italic').place(x=450,y=470)
            for k in alphadic.values():
                k.config(state='disabled')
            Bhint.config(state='disabled')
    else:
        remaining_lives-=1
        alphadic[letter].config(bg='red')
        alphadic[letter].config(state='disabled')
        letters_guessed.append(letter.lower())
        Lword.config(text=' %s' % get_guessed_word(secret_word, letters_guessed))
        if (remaining_lives == 0):
            Label(root,text=' * * HANGED, you lost! * * ',bg='yellow',fg='red',font='ABC 20 bold italic').place(x=450,y=470)
            Label(root, text=' By the way, the word was: %s' %(secret_word), bg='yellow', fg='red',font='ABC 20 bold italic').place(x=450, y=520)
            for k in alphadic.values():
                k.config(state='disabled')
            Bhint.config(state='disabled')
            setImage(-1)
            return
    setImage(remaining_lives)



Label(root,text='Welcome to the game, Hangman!',bg='white', fg='black', font='ABC 30 bold underline').place(x=300, y=50)

def Hint(secret_word, letters_guessed):
    Bhint.config(state='disabled')
    l=list(secret_word)
    for i in letters_guessed:
        if i in l:
            for j in range(l.count(i)):
                l.remove(i)
    h=random.choice(l)
    do(h.upper())
Bhint=Button(root, text='HINT',bg='black', fg='white', bd=6, font=("ABC 20 bold underline"),command=partial(Hint,secret_word,letters_guessed))
Bhint.place(x=100,y=200)

# Elife = Entry(root, bd=1, bg='white', fg='indigo', font='ABC 12')
# Elife.place(x=0, y=405)

global alphadic
alphadic={}
for s in string.ascii_uppercase:
    alphadic[s]=Button(root, text=s,bg='blue', fg='white', bd=6, font=("ABC 15 bold italic"), command=partial(do,s))

albx=350
alby=350
for i in alphadic.values():
    if (albx > 950):
        albx = 350
        alby += 50
    i.place(x=albx, y=alby)
    albx+=50
print(secret_word)
root.mainloop()