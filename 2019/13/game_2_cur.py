#!/usr/bin/env python

from collections import namedtuple
import threading
from Queue import Queue
import numpy as np
import time

import curses
stdscr = curses.initscr()

debug_log = open("debug_log.txt", "w")

def log(line):
    global n_blocks, score, ball_x, ball_y, paddle_x, paddle_y, expected_x
    debug_log.write("bl:{0} s:{1} b:{2} p:{3}: e:{4} {5}\n".format(n_blocks, score, (ball_x, ball_y),
                                                                 (paddle_x, paddle_y), expected_x, line))

def read_input(filename):
    with open(filename) as i:
        return [int(x) for x in i.readline().split(',')] 

Opcode = namedtuple('Opcode', ['opcode', 'modes'])
def decode_opcode(n):
    op = n % 100
    n = n /100
    modes = []
    for i in xrange(3):
        modes.append(n%10)
        n = n / 10
    return Opcode(op, modes)

def get_joystick():
    global expected_x, paddle_x, win, n_blocks
    #if n_blocks < 200:
    #    win.addstr(28,  30, "***")
    #    win.refresh()
    #    time.sleep(5)
    #    win.addstr(28,  30, "   ")
    #    win.refresh()
    if expected_x > paddle_x:
        return 1
    elif expected_x < paddle_x:
        return -1
    return 0

class IntCode:
    op_n_args = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2,
        99: 0}
        
    def __init__(self, ram):
        self.ram = list(ram)
        self.pc = 0
        self.input_queue = Queue()
        self.output_queue = Queue(1)
        self.state = 'pre-run'
        self.relative_base = 0
        self.joystick = 0
        
    def get_rval(self, op, n):
        mode = op.modes[n-1]
        if mode == 0:
            addr = self.ram[self.pc+n]
        elif mode == 1:
            addr = self.pc+n
        elif mode == 2:
            addr = self.ram[self.pc+n]+self.relative_base
        else:
            print("Bad mode", mode)
            exit(-1)
        #print "    rval:", self.pc, n, op.modes[n-1], v
        self.ensure_ram(addr)
        return self.ram[addr]

    def ensure_ram(self, size):
        if len(self.ram) < size+1:
            self.ram = self.ram + [0]*(1+size-len(self.ram))

    def set_lval(self, op, n, value):
        mode = op.modes[n-1]
        #print "    lval:", self.ram[self.pc+n], value, self.pc, n, mode
        if mode == 0:
            addr = self.ram[self.pc+n]
        elif mode == 1:
            addr = self.pc+n
        elif mode == 2:
            addr = self.ram[self.pc+n]+self.relative_base
        else:
            print("Bad mode", mode)
            exit(-1)
        self.ensure_ram(addr)
        self.ram[addr] = value

    def send_input(self, value):
        self.input_queue.put(value)

    def get_output(self):
        return self.output_queue.get()

    def has_output(self):
        return not self.output_queue.empty()
            
    def run(self):
        self.state = 'running'
        op = decode_opcode(self.ram[self.pc])
        while op.opcode != 99:
            #print("Starting opcode", pc, op, ram[pc:pc+4])
            jump_to = None
            if op.opcode == 1:
                value = self.get_rval(op, 1) + self.get_rval(op, 2) 
                self.set_lval(op, 3, value)
            elif op.opcode == 2:
                value = self.get_rval(op, 1) * self.get_rval(op, 2) 
                self.set_lval(op, 3, value)
            elif op.opcode == 3:
                #i = raw_input("> ")
                #if self.input_queue.empty():
                    #print "Input empty"
                #    self.set_lval(op, 1, 0)
                #else:
                #    v = self.input_queue.get()
                    #print "Input read: {}".format(v)
                    self.set_lval(op, 1, get_joystick())
                #print "Read {}".format(self.joystick)
            elif op.opcode == 4:
                #print(self.get_rval(op, 1))
                self.output_queue.put(self.get_rval(op, 1))
            elif op.opcode == 5:
                if self.get_rval(op, 1) != 0:
                    jump_to = self.get_rval(op, 2)
            elif op.opcode == 6:
                if self.get_rval(op, 1) == 0:
                    jump_to = self.get_rval(op, 2)
            elif op.opcode == 7:
                if self.get_rval(op, 1) < self.get_rval(op, 2):
                    self.set_lval(op, 3, 1)
                else:
                    self.set_lval(op, 3, 0)
            elif op.opcode == 8:
                if self.get_rval(op, 1) == self.get_rval(op, 2):
                    self.set_lval(op, 3, 1)
                else:
                    self.set_lval(op, 3, 0)
            elif op.opcode == 9:
                #print "updating base", op, self.ram[self.pc+1]
                self.relative_base += self.get_rval(op, 1)
            else:
                print("Unknown instruction %d at %d" % (self.ram[self.pc], self.pc))
                exit(-1)
            #print("New RAM", ram[pc:pc+4])
            if jump_to is None:
                self.pc += self.op_n_args[op.opcode]
            else:
                self.pc = jump_to
            op = decode_opcode(self.ram[self.pc])
        self.state = 'finished'

def thread_func(compy):
    compy.run()


ram = read_input('input.txt')
ram[0] = 2
c = IntCode(ram)
t = threading.Thread(target=thread_func, args=(c,))
t.start()

win = curses.newwin(30, 45, 0, 0)

board = np.zeros((45,25), dtype=int)
score = -1
ball_x = 15
ball_y = 0
paddle_x = None
paddle_y = 22
sig_paddle_x = None
expected_x = None
n_blocks = 0
going_right = True
going_up = False
expected_x = 23
right_wall = 0
left_wall = 43
zero_scores = []

def adjust_joystick():
    assert  False
    global sig_paddle_x
    if sig_paddle_x is None or expected_x is None:
        return
    while sig_paddle_x < expected_x:
        sig_paddle_x += 1
        #print "Going right"
        c.send_input(1)
    while sig_paddle_x > expected_x:
        #print "Going left"
        sig_paddle_x -= 1
        c.send_input(-1)
    assert sig_paddle_x == expected_x

overrides = {
    268: 19,
    264: 29,
    263: 29,
    231: 3,
    215: 11,
    214: 11,
    }

while c.state != 'finished' or c.has_output():
    #print "About to do reads:", c.state
    try:
        x = c.get_output()
        y = c.get_output()
        b = c.get_output()
    except:
        #print "Sending blocked input"
        c.send_input(0)
        continue
    #print x, y, b
    if x == -1 and y == 0:
        score = b
    else:
        ch = ' '
        if b == 1:
            ch = '+'
            left_wall = min(x, left_wall)
            right_wall = max(x, right_wall)
        elif b == 2:
            ch = '.'
        elif b == 3:
            ch = '-'
            log("Paddle moved")
            #print "Pad: b={},p={},ex={},j={}".format((ball_x,ball_y), (x, y), expected_x, c.joystick)
            paddle_x = x
            paddle_y = y
            if sig_paddle_x is None:
                sig_paddle_x = x
        elif b == 4:
            ch = 'o'
            #print "Ball:b={},p={},ex={}".format((x,y), (paddle_x, paddle_y), expected_x)
            if abs(x-ball_x) > 1 or abs(ball_y - y) > 1:
                log("TELEPORT: old:{} new:{}".format((ball_x, ball_y), (x, y)))
            if ball_y != y:
                going_right = x > ball_x
            going_up = y < ball_y
            ball_x = x
            ball_y = y
            log("Ball: up:{} right:{}".format(going_up, going_right))
            if going_up: 
                a = ball_x
                b = ball_y
                if going_right:
                    dir = 1
                else:
                    dir = -1
                a += dir
                b -= 1
                while board[a,b] == 0:
                    a += dir
                    b -= 1
                if b == left_wall or b == right_wall:
                   pass # skip
                else:
                    expected_x = a 
            else:
                if going_right:
                    dir = 1
                else:
                    dir = -1
                a = ball_x #+ dir
                b = ball_y #+ 1
                while board[a,b] == 0 and board[a+dir, b] == 0 and right_wall < a < left_wall:
                    a += dir
                    b += 1
                if board[a,b] == 2 or board[a+dir, b] == 2:
                    expected_x = a - (dir*1)
                    log("board[{0},{1}]: {2}, board[{3},{1}]: {4}".format(a, b, board[a,b], a+dir, board[a+dir, b]))
                else:    
                    if going_right:
                        expected_x = x + (paddle_y - y)
                    else:
                        expected_x = x - (paddle_y - y)
                    if expected_x >= right_wall- 1:
                        expected_x = right_wall - (expected_x - right_wall) - 2
                    if expected_x <= left_wall + 1:
                        #print "Correcting {} to {}".format(expected_x, -expected_x + 2)
                        expected_x = -expected_x + 2
                    log("No expected collision path")
            #print "Wall:", left_wall, right_wall
            #print "Exp:", going_up, going_right, (x,y), paddle_x, expected_x, sig_paddle_x
        board[x,y] = b
        win.addch(y,x,ch)
        if b == 0 or b == 2:
            n_blocks = np.count_nonzero(board==2)
            
        if n_blocks == 0:
            zero_scores.append(score)

        override = " "
        if overrides.has_key(n_blocks):
            expected_x = overrides[n_blocks]
            override = "*"
            
        
        win.addstr(26,  0, "Ball:   {0:2}, {1:2}  Up: {2:3} Right:{3:3}".format(ball_x, ball_y, going_up, going_right))
        win.addstr(27,  0, "Paddle: {0:2}, {1:2}  ".format(paddle_x, paddle_y))
        win.addstr(28,  0, "Expected x: {}{} ".format(expected_x, override))
        win.addstr(29,  0, "Score: {0:5}  ".format(score))
        win.addstr(29, 25, "Blocks: {0:3} ".format(n_blocks))

        if ball_y == 22:
            fail_x = ball_x
            fail_paddle = paddle_x
                
        if b in [0,3,4]:
            delay = 0.001
            if n_blocks < 220:
                delay = 0.02
            win.refresh()
            time.sleep(delay)
        #adjust_joystick()

    #print (x,y,b), c.state, n_blocks, score, (ball_x, ball_y), (paddle_x, paddle_y), expected_x
    

curses.endwin()
    
print "Failed with x=", fail_x, paddle_x, n_blocks

print zero_scores[-1]
