add_library("sound")

def playMusic():
    global a, b, c, d, e, f, x, old
    x.play()
    old = x
    print("peaches")

def setup():
    global a, b, c, d, e, f, x, old
    size(800, 800)
    img = loadImage("wood.jpg")
    image(img, 0, 200)
    
    a = SoundFile(this, "RNB.wav")
    b = SoundFile(this, "TRAP.wav")
    c = SoundFile(this, "HIPHOP.wav")
    d = SoundFile(this, "POP.wav")
    e = SoundFile(this, "FUNK.wav")
    f = SoundFile(this, "TECHNO.wav")
    x = SoundFile(this, "BG.wav")
    playMusic()
    
def mouseClicked():
    global old
    if mouseY in range(280, 380):
        if mouseX in range(190, 260):
            old.stop()
            a.play()
            old = a
    if mouseY in range(280, 350):        
        if mouseX in range(260, 330):
            old.stop()
            b.play()
            old = b
    if mouseY in range(280, 350):
        if mouseX in range(330, 400):
            old.stop()
            c.play()
            old = c
    if mouseY in range(280, 350):
        if mouseX in range(400, 470):
            old.stop()
            d.play()
            old = d
    if mouseY in range(280, 350):
        if mouseX in range(470, 540):
            old.stop()
            e.play()
            old = e
    if mouseY in range(280, 350):
        if mouseX in range(540, 610):
            old.stop()
            f.play()
            old = f
            
def draw():
    noStroke()
    # border left
    fill(random(150),random(100),random(100))
    rect(0, 200, 100, 600)
    # border right
    fill(random(150),random(100),random(100))
    rect(700, 200, 100, 600)
    # top arch
    arc(400, 200, 800, 300-60, PI, TWO_PI, CHORD)
    
    # side design left (grey)
    fill(120, 120, 120)
    rect(0, 300, 100, 20)
    rect(0, 340, 100, 20)
    rect(0, 380, 100, 20)
    
    # side design left (red)
    fill(230, 50, 50)
    rect(0, 320, 100, 20)
    fill(230, 10, 10)
    rect(0, 360, 100, 20)
    
    # side design right (grey)
    fill(120, 120, 120)
    rect(700, 300, 100, 20)
    rect(700, 340, 100, 20)
    rect(700, 380, 100, 20)
    
    # side design right (red)
    fill(230, 50, 50)
    rect(700, 320, 100, 20)
    fill(230, 10, 10)
    rect(700, 360, 100, 20)
    
    # top design (grey)
    fill(120, 120, 120)
    rect(350, 80, 20, 120)
    rect(390, 80, 20, 120)
    rect(430, 80, 20, 120)
    
    # top design (red)
    fill(230, 50, 50)
    rect(370, 80, 20, 120)
    fill(230, 10, 10)
    rect(410, 80, 20, 120)
    
    # arch on wood
    fill(80, 80, 80)
    arc(400, 280, 420, 160-60, PI, TWO_PI, CHORD)
    
    # middle design (yellow)
    fill(200, 200, 100)
    rect(250, 400, 300, 50)
    
    # middle design (grey)
    fill(120, 120, 120)
    rect(250, 400, 300, 10)
    rect(250, 420, 300, 10)
    rect(250, 440, 300, 10)
    rect(370, 400, 60, 40)
    textSize(28)
    fill(0)
    text("J&B", 378, 434)
    
    # middle design_vert (grey)
    fill(100, 100, 100)
    rect(230, 390, 20, 70)
    rect(550, 390, 20, 70)
    
    # middle design
    fill(80, 80, 80)
    rect(325, 470, 150, 80)
    fill(120, 120, 120)
    rect(325, 530, 150, 20)
    fill(250, 40, 30)
    rect(335, 480, 10, 60)
    rect(455, 480, 10, 60)
    fill(240, 100, 100)
    rect(355, 520, 10, 20)
    rect(375, 520, 10, 20)
    rect(395, 520, 10, 20)
    rect(415, 520, 10, 20)
    rect(435, 520, 10, 20)
    textSize(13)
    fill(0)
    text("Josh & Brandon", 354, 503)
    
    # genre buttons
    fill(100, 240, 130)
    rect(190, 280, 70, 100)
    fill(240, 100, 130)
    rect(260, 280, 70, 100)
    fill(100, 130, 240)
    rect(330, 280, 70, 100)
    fill(180, 130, 200)
    rect(400, 280, 70, 100)
    fill(240, 200, 100)
    rect(470, 280, 70, 100)
    fill(10, 200, 150)
    rect(540, 280, 70, 100)
    
    # genre button text
    textSize(20)
    fill(0)
    text("R&B", 205, 335)
    text("TRAP", 270, 335)
    text("HIP", 418, 325)
    text("HOP", 413, 350)
    text("POP", 485, 335)
    text("FUNK", 548, 335)
    textSize(12)
    text("TECHNO", 340, 335)
