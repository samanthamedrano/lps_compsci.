import turtle

def tDawg(myTurle):
    myTurle.forward(130)
    myTurle.left(180)
    myTurle.forward(30)
    myTurle.right(90)
    myTurle.forward(30)
    myTurle.right(180)
    myTurle.forward(60)
    myTurle.right(180)
    myTurle.forward(30)
    myTurle.left(90)
    myTurle.forward(100)

myColors = ['red', 'blue', 'purple', 'green', 'yellow', 'gray', 'black']


# your code starts executing here and should call your functions
bob = turtle.Turtle()
bob.speed(100)

bob.right(135)

for tyeDye in myColors:
    bob.color(tyeDye)
    bob.right(45)
    tDawg(bob)


