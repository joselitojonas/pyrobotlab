def whataboutstarwars():
  x = (random.randint(1, 2))
       if x == 1:
           fullspeed()
           i01.moveHead(130,149,87,80,100)
           i01.mouth.speak("R2D2")
           sleep(1)
           i01.moveHead(155,31,87,80,100)
           sleep(1)
           i01.moveHead(130,31,87,80,100)
           sleep(1)
           i01.moveHead(90,90,87,80,100)
           sleep(0.5)
           i01.moveHead(90,90,87,80,70)
           sleep(1)
           relax()
       if x == 2:
           fullspeed()
           i01.mouth.speak("Hello sir, I am C3po unicyborg relations")
           i01.moveHead(138,80)
           i01.moveArm("left",79,42,23,41)
           i01.moveArm("right",71,40,14,39)
           i01.moveHand("left",180,180,180,180,180,47)
           i01.moveHand("right",99,130,152,154,145,180)
           i01.moveTorso(90,90,90)
           sleep(1)
           i01.moveHead(116,80)
           i01.moveArm("left",85,93,42,16)
           i01.moveArm("right",87,93,37,18)
           i01.moveHand("left",124,82,65,81,41,143)
           i01.moveHand("right",59,53,89,61,36,21)
           i01.moveTorso(90,90,90)
           sleep(1)
           relax()
