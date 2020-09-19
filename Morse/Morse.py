import winsound
import time

def dit():
	winsound.Beep(880, 200)

def dash():
	winsound.Beep(880, 800)

def a():
	dit()
	dash()

def b():
	dash()
	dit()
	dit()
	dit()

def c():
	dash()
	dit()
	dash()
	dit()

def d():
	dash()
	dit()
	dit()

def e():
	dit()

def f():
	dit()
	dit()
	dash()
	dit()

def g():
	dash()
	dash()
	dit()

def h():
	dit()
	dit()
	dit()
	dit()

def i():
	dit()
	dit()

def j():
	dit()
	dash()
	dash()
	dash()

def k():
	dash()
	dit()
	dash()

def l():
	dit()
	dash()
	dit()
	dit()

def m():
	dash()
	dash()

def n():
	dash()
	dit()

def o():
	dash()
	dash()
	dash()

def p():
	dit()
	dash()
	dash()
	dit()

def q():
	dash()
	dash()
	dit()
	dash()

def r():
	dit()
	dash()
	dit()

def s():
	dit()
	dit()
	dit()

def t():
	dash()

def u():
	dit()
	dit()
	dash()

def v():
	dit()
	dit()
	dit()
	dash()

def w():
	dit()
	dash()
	dash()

def x():
	dash()
	dit()
	dit()
	dash()

def y():
	dash()
	dit()
	dash()
	dash()

def z():
	dash()
	dash()
	dit()

def spc():
	time.sleep(4)


def transmitl(letter):
	if letter == 'a':
		a()
	elif letter == 'b':
		b()
	elif letter == 'c':
		c()
	elif letter == 'd':
		d()
	elif letter == 'e':
		e()
	elif letter == 'f':
		f()
	elif letter == 'g':
		g()
	elif letter == 'h':
		h()
	elif letter == 'i':
		i()
	elif letter == 'j':
		j()
	elif letter == 'k':
		k()
	elif letter == 'l':
		l()
	elif letter == 'm':
		m()
	elif letter == 'n':
		n()
	elif letter == 'o':
		o()
	elif letter == 'p':
		p()
	elif letter == 'q':
		q()
	elif letter == 'r':
		r()
	elif letter == 's':
		s()
	elif letter == 't':
		t()
	elif letter == 'u':
		u()
	elif letter == 'v':
		v()
	elif letter == 'w':
		w()
	elif letter == 'x':
		x()
	elif letter == 'y':
		y()
	elif letter == 'z':
		z()
	elif letter == ' ':
		spc()
	else: 
		print("ERROR WILL ROBINSON")


def transmitm(mesg):
	mesg = mesg.lower()
	print(mesg)
	for x in mesg:
		transmitl(x)
		time.sleep(2)