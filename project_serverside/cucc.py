from flask import Flask, redirect, url_for , render_template, flash, request 
from udp_test import sendMessage, setTimeout
import threading
import time

app = Flask(__name__)
app.secret_key = 'BardosAnyjaASzerelmem'
pos = (0,0)
gopos = (0,0)
motor1_displacement = 0
motor2_displacement = 0
speed  = 1 # masodpercbeli lepesek szama * 100
step_num  =1 #half step, etc
degrees = 40
#rendering the HTML page which has the button
timeout = False
def updateDegrees(degrees):
    mystring = "deg"+str(degrees)
    if (sendMessage(mystring) is True):
        print("Confirmed updated degrees to "+str(degrees))
    else:
        print("Handshake not received. Check connection.")
    if(abs(degrees) > 720):
        timeout = True
    else:
        timeout = False
    setTimeout(timeout)
def moveTo(gopos):
    global pos
    print("going to " + str(gopos))
    #elso tengely
    delta1 = (pos[0]-gopos[0])
    motor1_displacement = 0
    #masodik tengely 
    delta2 = (pos[1]-gopos[1])
    print("delta = "+str(delta1)+","+str(delta2))
    motor2_displacement = 0
    #atalakitjuk a koordinatakat stepper fokokba
    f1 = 12 #amugy nem ennyi 
    f2 = 32
    k1 = f1/f2 * 1/144
    k2 =  f1/f2 *1/144 # ra worm gear 
    motor1_displacement = delta1/k1
    motor2_displacement = delta2/k2
    updateDegrees(motor1_displacement)
    if(sendMessage("1") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    updateDegrees(motor2_displacement)
    if(sendMessage("2") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    print("motor displacements: "+str(motor1_displacement)+","+str(motor2_displacement))
    return pos

@app.route('/refresh')
def refresh():
    return redirect(url_for('/json'))
@app.route('/entry', methods =['GET','POST'])
def entry_page():
    if request.method == 'POST':
        return redirect("/json")
    else:
        return redirect("/json")

@app.route('/')
def redir():
    return redirect("/json")
@app.route('/json')
def json():
    global pos,motor1_displacement,motor2_displacement
    f1 = 8 #amugy nem ennyi 
    f2 = 32
    k1 = f1/f2 * 1/144
    k2 =  f1/f2 *1/144 # ra worm gear 
    pos = (pos[0]+motor1_displacement*k1,pos[1]+motor2_displacement*k2)
    motor1_displacement = 0
    motor2_displacement = 0
    return render_template("json.html",data1 = pos[0], data2 = pos[1])
@app.route('/up')
def up():
    global motor1_displacement
    updateDegrees(degrees)
    motor1_displacement += degrees
    print("going up")
    if(sendMessage("1") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    return redirect("/json")
@app.route('/down')
def down():
    global motor1_displacement
    updateDegrees(-degrees)
    motor1_displacement += -degrees
    print ("going down")
    if(sendMessage("1") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    return redirect("/json")
@app.route('/left')
def left():
    global motor2_displacement
    updateDegrees(degrees)
    motor2_displacement += degrees
    print ("going left")
    if(sendMessage("2") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    return redirect("/json")
@app.route('/right')
def right():
    global motor2_displacement
    updateDegrees(-degrees)
    motor2_displacement += -degrees
    print ("going right")
    if(sendMessage("2") is True):
        print("Confirmed movement executed.")
    else:
        print("Handshake not received. Check connection.")
    return redirect("/json")
@app.route('/stop')
def stop():
    sendMessage("5")
    print("Stopping, action interrupted. Recalibrate.")
    return redirect("/json")

@app.route('/speed1')
def speed1():
    global speed
    speed  =2
    sendMessage("6")
    print("Step frequency changed to 100.")
    return redirect("/json")
@app.route('/speed2')
def speed2():
    global speed
    speed  =4
    sendMessage("7")
    print("Step frequency changed to 200.")
    return redirect("/json")
@app.route('/speed3')
def speed3():
    global speed
    speed  =8
    sendMessage("8")
    print("Step frequency changed to 300.")
    return redirect("/json")
@app.route('/speed4')
def speed4():
    global speed
    speed  =16
    sendMessage("9")
    print("Step frequency changed to 500.")
    return redirect("/json")
@app.route('/speed5')
def speed5():
    global speed
    speed  =32
    sendMessage("a")
    print("Step frequency changed to 800.")
    return redirect("/json")

@app.route('/step1')
def step1():
    global step_num
    step_num = 1
    sendMessage("b")
    print("Full step.")
    return redirect("/json")
@app.route('/step2')
def step2():
    global step_num
    step_num = 2
    sendMessage("c")
    print("Half step.")
    return redirect("/json")
@app.route('/step3')
def step3():
    global step_num
    step_num = 4
    sendMessage("d")
    print("Quarter step")
    return redirect("/json")
@app.route('/step4')
def step4():
    global step_num
    step_num = 8
    sendMessage("e")
    print("Eighth step")
    return redirect("/json")

@app.route('/data', methods=['POST'])
def get_calibration():
    global pos
    nums = (float(request.form['number']),float(request.form['number2']))
    pos = nums
    print("New calibration: "+str(nums, pos))
    return redirect("/json")
@app.route('/gdata', methods=['POST'])
def get_goto():
    global gopos,pos
    nums = (float(request.form['gnumber']),float(request.form['gnumber2']))
    gopos = nums
    moveTo(gopos)
    pos = gopos
    return redirect("/json")
@app.route('/ddata', methods=['POST'])
def get_angle():
    global degrees
    degrees = float(request.form['dnumber'])
    updateDegrees(degrees)
    return redirect("/json")

app.run(host="0.0.0.0")