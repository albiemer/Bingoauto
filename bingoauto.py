
import random


class bingdata:
    forb = 0
    fori = 0
    forn = 0
    forg = 0
    foro = 0

def oldi():
    bingdata.fori = int(input("Enter a number for I (16-30): "))
    return 1

def i():
    bingdata.forn = int(input("Enter a number for N (31-45): "))
    return 1
            
def n():
    bingdata.forg = int(input("Enter a number for G (46-60): "))
    return 1
            
def g():
    bingdata.foro = int(input("Enter a number for O (61-75): "))
    return 1
    
def o():
    print("Your BINGO combination: ")
                        
    print("Your Bet: ", \
    "B[",bingdata.forb,"]", \
    "I[",bingdata.fori,"]", \
    "N[",bingdata.forn,"]", \
    "G[",bingdata.forg,"]", \
    "O[",bingdata.foro,"]")

    print("########## BINGO Result ##########")

    ugot = 0
    rb = random.choice(range(1,16))
    ri = random.choice(range(16,31))
    rn = random.choice(range(31,46))
    rg = random.choice(range(46,61))
    ro = random.choice(range(61,76))
                        
    if rb == bingdata.forb:
        ugot += 1
    if ri == bingdata.fori:
        ugot += 1
    if rn == bingdata.forn:
        ugot += 1
    if rg == bingdata.forg:
        ugot += 1
    if ro == bingdata.foro:
        ugot += 1
                        
    print("(1-15)  B:", rb)
    print("(16-30) I:", ri)
    print("(31-45) N:", rn)
    print("(46-60) G:", rg)
    print("(61-75) O:", ro)
                        
    print("Total Result you've got is", ugot)

def b():
    print("welcome to BINGO")
    bingdata.forb = int(input("Enter number for B (1-15): "))

    if bingdata.forb in range(1,16):
        bingdata.fori = int(input("Enter a number for I (16-30): "))
        
        if bingdata.fori in range(16,31):
            i()
            
            if bingdata.forn in range(31,46):
                n()
                
                if bingdata.forg in range(46,61):
                    g()
                    
                    if bingdata.foro in range(61,76):
                        o()    
                    else:
                        print("Input correct range with (61-75)")
                        g()
                    
                else:
                    print("Input correct range with (46-60)")
                    n()
                
            else:
                print("Input correct range with (31-45)")
                i()
            
        else:
            print("Input correct range with (16-30)")
            oldi()
        
    else:
        print("Input correct range with (1-15)")
        b() 

b()