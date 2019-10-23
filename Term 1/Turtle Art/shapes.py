import turtle
turtle.bgcolor("black")
turtle.setup(width=1000,height=1000)
x=turtle.Pen()
y=turtle.Pen()

x.shape("circle")
x.color("yellow")
x.speed(0)
x.width(3)



for i in range(250):
    x.forward(i*3)
    x.circle(5)
    x.right(115)
    
  
    
