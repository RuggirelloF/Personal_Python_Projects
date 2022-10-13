import turtle

#Window
Wn = turtle.Screen()
Wn.title("Pong")
Wn.bgcolor("black")
Wn.setup(width = 800,height = 600)
Wn.tracer(0)

#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid = 5, stretch_len = 0.5)

#JugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid = 5, stretch_len = 0.5)

#Pelota
Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("circle")
Pelota.color("white")
Pelota.penup()
Pelota.goto(0,0)
Pelota.dx = 0.25
Pelota.dy = 0.25

#Red
Red = turtle.Turtle()
Red.shape("square")
Red.color("white")
Red.penup()
Red.goto(0,0)
Red.shapesize(stretch_wid = 50, stretch_len = 0.01)

#Marcador
Marcador = turtle.Turtle()
Marcador.speed(0)
Marcador.color("white")
Marcador.penup()
Marcador.hideturtle()
Marcador.goto(0,260)
Marcador.write("0		0", align = "center", font = ("Courier", 30, "normal"))

#Marcador
MarcadorA = 0
MarcadorB = 0

#Funciones
def jugadorA_up():
	y = jugadorA.ycor()
	y += 30
	jugadorA.sety(y)

def jugadorA_down():
	y = jugadorA.ycor()
	y -= 30
	jugadorA.sety(y)

def jugadorB_up():
	y = jugadorB.ycor()
	y += 30
	jugadorB.sety(y)

def jugadorB_down():
	y = jugadorB.ycor()
	y -= 30
	jugadorB.sety(y)

#Teclado
Wn.listen()
Wn.onkeypress(jugadorA_up, "w")
Wn.onkeypress(jugadorA_down, "s")
Wn.onkeypress(jugadorB_up, "Up")
Wn.onkeypress(jugadorB_down, "Down")


while True:
	Wn.update()

	Pelota.setx(Pelota.xcor() + Pelota.dx)
	Pelota.sety(Pelota.ycor() + Pelota.dy)

	#Bordes
	if Pelota.ycor() > 290:
		Pelota.dy *= -1

	if Pelota.ycor() < -290:
		Pelota.dy *= -1

	#Bordes puntos
	if Pelota.xcor() > 390:
		Pelota.goto(0,0)
		Pelota.dx = 0.25
		MarcadorA += 1
		Marcador.clear()
		Marcador.write("{}		{}".format(MarcadorA,MarcadorB), align = "center", font = ("Courier", 30, "normal"))

	if Pelota.xcor() < -390:
		Pelota.goto(0,0)
		Pelota.dx = 0.25
		MarcadorB += 1
		Marcador.clear()
		Marcador.write("{}		{}".format(MarcadorA,MarcadorB), align = "center", font = ("Courier", 30, "normal"))

	if ((Pelota.xcor() > 340 and Pelota.xcor() < 350)
			and (Pelota.ycor() < jugadorB.ycor() + 50
			and Pelota.ycor() > jugadorB.ycor() - 50)):
		Pelota.dx *= -1.1

	if ((Pelota.xcor() < -340 and Pelota.xcor() > -350)
			and (Pelota.ycor() < jugadorA.ycor() + 50
			and Pelota.ycor() > jugadorA.ycor() - 50)):
		Pelota.dx *= -1.1

