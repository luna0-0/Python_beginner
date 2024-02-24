def game():
    return 88

score=game()
with open('34 highscore.txt') as f:
    hscore=f.read()

if hscore=='':
    with open("34 highscore.txt",'w') as f:
        hiscore=f.write(str(score))

elif int(hscore)<score:
    with open("34 highscore.txt","w") as f:
        hiscore=f.write(str(score))