def shakehand():
      rest()
      i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(80,86)
      i01.moveArm("left",5,90,30,10)
      i01.moveArm("right",5,90,30,10)
      i01.moveHand("left",2,2,2,2,2,90)
      i01.moveHand("right",2,2,2,2,2,90)
      i01.moveTorso(90,90,90)
      sleep(1)
    ##move arm and hand
      i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
      i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
      i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
      i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(39,70)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,65,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",50,50,40,20,20,90)
      i01.moveTorso(120,100,90)
      sleep(1)
    ##close the hand
      i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
      i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
      i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
      i01.setArmSpeed("left", 0.75, 0.85, 0.75, 0.85)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(39,70)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,62,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",180,126,120,145,168,77)
      i01.moveTorso(101,100,90)
      sleep(3)
    ##shake hand up
      i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
      i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
      i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
      i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(90,90)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,70,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",180,126,120,145,168,77)
      i01.moveTorso(101,100,90)
      sleep(1)
    ##shake hand down
      x = (random.randint(1, 5))
      if x == 1:
        i01.mouth.speak("please to meet you")
      if x == 2:
        i01.mouth.speak("carefull my hand is made out of plastic")
      if x == 3:
        i01.mouth.speak("I am happy to shake a human hand")
      if x == 4:
        i01.mouth.speak("it is a pleasure to meet you")
      if x == 5:
        i01.mouth.speak("very nice to meet you")  
      i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
      i01.setHeadSpeed(0.85, 0.85)
      i01.setTorsoSpeed(1.0, 1.0, 1.0)
      i01.moveHead(80,53)
      sleep(2)
      i01.moveHead(39,70)
      sleep(2)
      i01.moveHead(80,53)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,60,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",180,126,120,145,168,77)
      i01.moveTorso(101,100,90)
      sleep(1)
    ##shake hand up
      i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
      i01.setHeadSpeed(0.85, 0.85)
      i01.setTorsoSpeed(1.0, 1.0, 1.0)
      i01.moveHead(80,53)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,75,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",180,126,120,145,168,77)
      i01.moveTorso(101,100,90)
      sleep(1)
    ##shake hand down
      i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 0.75, 0.75, 0.95, 0.85)
      i01.setHeadSpeed(0.85, 0.85)
      i01.setTorsoSpeed(1.0, 1.0, 1.0)
      i01.moveHead(82,88)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,62,16)
      i01.moveHand("left",50,50,40,20,20,90)
      i01.moveHand("right",180,126,120,145,168,77)
      i01.moveTorso(101,100,90)
      sleep(2)
    ## release hand  
      i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.85)
      i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(39,70)
      i01.moveArm("left",5,84,16,15)
      i01.moveArm("right",6,73,62,16)
      i01.moveHand("left",50,50,40,20,20,77)
      i01.moveHand("right",20,30,30,20,20,90)
      i01.moveTorso(101,100,90)
      sleep(1)
    ##relax
      i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
      i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.85)
      i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
      i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
      i01.setHeadSpeed(1.0, 1.0)
      i01.setTorsoSpeed(0.75, 0.55, 1.0)
      i01.moveHead(79,85)
      i01.moveArm("left",5,84,28,15)
      i01.moveArm("right",5,90,30,12)
      i01.moveHand("left",92,33,37,71,66,25)
      i01.moveHand("right",10,50,40,20,20,113)
      i01.moveTorso(90,90,90)