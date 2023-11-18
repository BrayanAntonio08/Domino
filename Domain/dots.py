backgroud = "black"
color = "white"

class Dots:
    def __init__(self, x, y, size, dots, canvas, horizontal) -> None:
        #atributos
        self.x = x
        self.y = y
        self.size = size
        self.dot_size = self.size/14
        paint_switch = {
            0 : self.dot0,
            1 : self.dot1,
            2 : self.dot2,
            3 : self.dot3,
            4 : self.dot4,
            5 : self.dot5,
            6 : self.dot6
        }
        paint_method = paint_switch.get(dots, self.dot0)
        paint_method(canvas, horizontal)

    def dot0(self, canvas, horiz):
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)


    def draw_dot(self, dot_size, x, y, canvas):
        canvas.create_oval(x, y, x+dot_size*2, y+dot_size*2, fill=color)
    
    def dot1(self, canvas, horiz):
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot_x = x+(self.size/2)-dot_size
        dot_y = y+(self.size/2)-dot_size
        self.draw_dot(dot_size, dot_x, dot_y, canvas)

    def dot2(self, canvas, horiz):
        #dibujar el fondo
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot1_x = x+dot_size
        dot1_y = y+dot_size
        self.draw_dot(dot_size, dot1_x, dot1_y, canvas)
        dot2_x = x2-dot_size*3
        dot2_y = y2-dot_size*3
        self.draw_dot(dot_size, dot2_x, dot2_y, canvas)

    def dot3(self, canvas, horiz):
        #dibujar el fondo
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot1_x = x+dot_size
        dot1_y = y+dot_size
        self.draw_dot(dot_size, dot1_x, dot1_y, canvas)
        dot2_x = x2-dot_size*3
        dot2_y = y2-dot_size*3
        self.draw_dot(dot_size, dot2_x, dot2_y, canvas)
        dot3_x = x+(self.size/2)-dot_size
        dot3_y = y+(self.size/2)-dot_size
        self.draw_dot(dot_size, dot3_x, dot3_y, canvas)
    
    def dot4(self, canvas, horiz):
        #dibujar el fondo
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot1_x = x+dot_size
        dot1_y = y+dot_size
        self.draw_dot(dot_size, dot1_x, dot1_y, canvas)
        dot2_x = x2-dot_size*3
        dot2_y = y2-dot_size*3
        self.draw_dot(dot_size, dot2_x, dot2_y, canvas)
        dot3_x = x2 - dot_size*3
        dot3_y = y + dot_size
        self.draw_dot(dot_size, dot3_x, dot3_y, canvas)
        dot4_x = x + dot_size
        dot4_y = y2 - dot_size*3
        self.draw_dot(dot_size, dot4_x, dot4_y, canvas)

    def dot5(self, canvas, horiz):
        #dibujar el fondo
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot1_x = x+dot_size
        dot1_y = y+dot_size
        self.draw_dot(dot_size, dot1_x, dot1_y, canvas)
        dot2_x = x2-dot_size*3
        dot2_y = y2-dot_size*3
        self.draw_dot(dot_size, dot2_x, dot2_y, canvas)
        dot3_x = x2 - dot_size*3
        dot3_y = y + dot_size
        self.draw_dot(dot_size, dot3_x, dot3_y, canvas)
        dot4_x = x + dot_size
        dot4_y = y2 - dot_size*3
        self.draw_dot(dot_size, dot4_x, dot4_y, canvas)
        dot5_x = x+(self.size/2)-dot_size
        dot5_y = y+(self.size/2)-dot_size
        self.draw_dot(dot_size, dot5_x, dot5_y, canvas)

    def dot6(self, canvas, horiz):
        #dibujar el fondo
        x = self.x
        y = self.y
        x2 = x+self.size
        y2 = y+self.size
        canvas.create_rectangle(x, y, x2, y2, outline=color, fill=backgroud)
        dot_size = self.dot_size
        dot1_x = x+dot_size
        dot1_y = y+dot_size
        self.draw_dot(dot_size, dot1_x, dot1_y, canvas)
        dot2_x = x2-dot_size*3
        dot2_y = y2-dot_size*3
        self.draw_dot(dot_size, dot2_x, dot2_y, canvas)
        dot3_x = x2 - dot_size*3
        dot3_y = y + dot_size
        self.draw_dot(dot_size, dot3_x, dot3_y, canvas)
        dot4_x = x + dot_size
        dot4_y = y2 - dot_size*3

        self.draw_dot(dot_size, dot4_x, dot4_y, canvas)
        dot5_x = x+(self.size/2)-dot_size if horiz else x+dot_size
        dot5_y = y+dot_size if horiz else y+(self.size/2)-dot_size
        self.draw_dot(dot_size, dot5_x, dot5_y, canvas)
        dot6_x = x+(self.size/2)-dot_size if horiz else x2-dot_size*3
        dot6_y = y2-dot_size*3 if horiz else y+(self.size/2)-dot_size
        self.draw_dot(dot_size, dot6_x, dot6_y, canvas)