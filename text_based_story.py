import os
os.system('clear')

def intro():
    print("You wake up in your bedroom a standard room with a twin bed and two doors")
    print("one is your closet the other is the door into the hallway.")
    print("Everything looks a little off more dream like As you're unsure about what to do next") 
    print("and if this is a dream or not you choose to explore.")
    print("Type out your choices according to what is in the 'apostrophes'.")
    print("you have three choices")
    bed_choice = input("\nWhere do you want to go Bedroom 'door' 'closet' or back to 'bed'?").lower()
    
    if bed_choice == 'door':
        bedroom_door()
    elif bed_choice=='closet':
        closet()
    elif bed_choice=='bed':
        back_to_bed()
    else:
        print("Invalid choice. Try again.")
        intro()

def bedroom_door():
    print("""
As you step out into the hall, something feels off.
The familiar layout has warped, with rooms displaced from their usual spots.
Directly ahead, where you least expect it, stands the bathroom.
To your right, another hallway stretches out, shrouded in an eerie mist.
Cautiously, you move towards the center of the room. Suddenly, an object strikes your face!
You grab it, pulling it away to examine it. 
It's round, like a ball. Before you can process this, a loud creak echoes above.
A ladder descends from the ceiling, nearly hitting you as it unfolds,
revealing an entrance to the attic.""")
    bedroom_door_choice = input("\nWhere do you want to go the'hall' the'bathroom' or the 'attic'?").lower()
    if bedroom_door_choice == "hall":
        hall()
    elif bedroom_door_choice == "attic":
        attic()
    elif bedroom_door_choice == "bathroom":
        bathroom()
    else:
        print("Invalid choice. Try again.")
        bedroom_door()
          
def closet():
    print("""
You decide to head to the closet it looks normal enough so you open it.
On the other side of the shutter doors is nothing,
there is a void on the other side.
In the distance there seems to be light at the end of the void.""")
    closet_choice = input("\nYou have three choices 'run','wonder' inside,or 'close'the door.").lower()
    if closet_choice == "run":
        run_2()
    elif closet_choice == "wonder":
        wonder()
    elif closet_choice == "close":
        close()
    else:
        print("Invalid choice. Try again.")
        closet()

def back_to_bed():
    print("""
You look back to the bed to try to 'sleep' and it seems that a person is your bed.
You take a closer look at them but their features are cloudy, hard to discern but from what you see it seems to be yourself.
you try to wake it up and your hand passes right through it.
It disappears and fades into a thin mist.""")
    bed_choice = input("\nYou have one choice 'back'.").lower()
    if bed_choice == "back":
        bedroom()
    elif bed_choice == 'sleep':
        print("no.")
        back_to_bed()
    else:
        print("Invalid choice. Try again.")
        back_to_bed()

def bedroom():
    print("You are back in the bedroom what will you do.")
    bed_choice = input("\nYou have three choises: 'closet', bedroom 'door', and back to 'bed'.").lower()
    
    if bed_choice == 'door':
        bedroom_door()
    elif bed_choice=='closet':
        closet()
    elif bed_choice=='bed':
        back_to_bed()
    else:
        print("Invalid choice. Try again.")
        bedroom()
        
def hall():
    print("""
You enter the mist filled hallway. 
The hallway is getting worse as you move down the lights start flickering
yet the hallway stays lit no matter whether the lights are on or off.
The floor the carpet gets shorter, more rigid, and older the white paint slowly darkens into a yellow-ish color
and is chipping away. Soon the hallway is falling apart and is smelling of smoke.""")
    hall_choice = input("\nYou have one choice 'RUN'. ").lower()
    if hall_choice == "run":
        run()
    else:
        print("Invalid choice. Try again.")
        hall()        

def run():
    print("""
You quickly run to the end of the hallway through the fire and the falling apart floor.
As your bolting the floor fully gives way and you fall.""")
    print("\nBefore you can process anything that is happening you land on new carpet.")
    run_choice = input("\nYou have one choice 'otherside'. ").lower()
    if run_choice == "otherside":
        otherside()
    else:
        print("Invalid choice. Try again.")
        run()        
        
def otherside():
    print("You are back in your bedroom it looks more normal than before. The lighting looks like it is dawn. Where do you want to go")
    other_choice = input("\nYou have three choises: 'closet',bedroom 'door', and back to 'bed'.").lower()
    
    if other_choice == 'door':
        bedroom_door_2()
    elif other_choice=='closet':
        closet_2()
    elif other_choice=='bed':
        bed()
    else:
        print("Invalid choice. Try again.")
        otherside()
        
def bedroom_door_2():
    print("""
The cold door is locked where will you go now?
""")
    bedroom_door_2_choice = input("\nYou have one choice 'bedroom'. ").lower()
    if bedroom_door_2_choice == "bedroom":
        otherside()
    else:
        print("Invalid choice. Try again.")
        bedroom_door_2()     

def bed():
    print("""
Your bed looks normal and quite comfy. You feel tired.
""")
    other_bed_choice = input("\nYou have two choices 'back'or'sleep'.").lower()
    if other_bed_choice == "back":
        otherside()
    elif other_bed_choice == 'sleep':
        sleep()
    else:
        print("Invalid choice. Try again.")
        bed()
        
def sleep():
    print("""
You climb into the bed and you instantly fall asleep.
""")
    sleep_choice = input("\nYou have one choices 'awaken'.").lower()
    if sleep_choice == "awaken":
        awaken()
    else:
        print("Invalid choice. Try again.")
        sleep()
        
def awaken():
    print("""
You wake up in your bed and everything looks normal and everything feels normal.
You walk around everything is where it should be and nothing out of the ordinary.
You move on with your life and quickly forget the encounter only to be reminded of it in your passing thoughts.
YOU WIN
""")
    awaken_choice = input("\nYou have two choices start'again','quit'.").lower()
    if awaken_choice == "again":
        intro()
    elif awaken_choice=='quit':
        print("thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        awaken()

def run_2():
    print("""
You panic and run away from the void. 
You pass through the bedroom door and turn into an expansive hallway.
at the end of that hallway is nothing, another void.
You turn around another void closing in and now void is all there is.
You feel the floor beneath you but you can't see anything.
You run around the void for all eternity. You never wake up…
""")
    Run_2_choice = input("\nYou have two choices start'again','quit'.").lower()
    if Run_2_choice == "again":
        intro()
    elif Run_2_choice =='quit':
        print("thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        run_2()

def wonder():
    print("""
You wonder inside the void and walk slowly towards the light.
You can't see anything other than the light you can feel the solid floor beneath you.
You keep walking, the light seems no closer than it was before. 
You pick up the pace. It gets no closer, when you look behind you and there is nothing… you run you try to run as fast as possible to the light… you collapse, you look on as the light is still taunting you with freedom seeming within reach but never possible.
You never wake up again
GAME OVER
""")
    wonder_choice = input("\nYou have two choices start'again','quit'.").lower()
    if wonder_choice == "again":
        intro()
    elif wonder_choice =='quit':
        print("thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        wonder()
        
def close():
    print("""
You close the shutters
""")
    close_choice = input("\nYou have two choices bedroom'door','open'the shutters.").lower()
    if close_choice == "door":
        bedroom_door()
    elif close_choice =='open':
        open()
    else:
        print("Invalid choice. Try again.")
        close()

def open():
    print("""
You open the shutters and the closet looks normal
""")
    open_choice = input("\nYou have two choices 'close' the shutters,'wonder' inside.").lower()
    if open_choice == "wonder":
        wonder_2()
    elif open_choice =='close':
        close()
    else:
        print("Invalid choice. Try again.")
        open()
        
def wonder_2():
    print("""
You enter the closet and close the door.
once you close the door you sit down and through the cracks in the shutters you see
the light outside change from a light blue dream tint to a darker brown or sandy color.
""")
    wonder_2_choice = input("\nYou have two choices 'wait' or 'wonder' outside.").lower()
    if wonder_2_choice == "wonder":
        room()
    elif wonder_2_choice =='wait':
        wait()
    else:
        print("Invalid choice. Try again.")
        wonder_2() 

def wait():
    print("""
You decide to wait.
The color outside the shutters change once more back to a orange dawn color.
""")
    wait_choice = input("\nYou have two choices 'wait' or 'wonder' outside.").lower()
    if wait_choice == "wonder":
        otherside()
    elif wait_choice =='wait':
        wait_2()
    else:
        print("Invalid choice. Try again.")
        wait() 

def wait_2():
    print("""
You decide to wait a little longer and the color dimms into nothingness. 
There is no closet any more, only the void. 
You feel the carpet flatten into a flat tile like texture beneath you. 
You wonder about the void for all eternity.
You never wake up again.
""")
    wait_2_choice = input("\nYou have two choices start'again' or 'quit'.").lower()
    if wait_2_choice == "again":
        intro()
    elif wait_2_choice =='quit':
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        wait_2() 
        
def room():
    print("""
You open the closet door to a bedroom sized room with hazel wallpaper. 
Infront of you is a small coffee table with a cup of coffee on it.
It is dimly lit by the lightbulb that is burning out above it.
""")
    room_choice = input("\nYou have three choices drink the'coffee',back to the 'closet' or 'wait'.").lower()
    if room_choice == "coffee":
        coffee()
    elif room_choice =='closet':
        wait_2()  
    elif room_choice =='wait':
        wait_3()
    else:
        print("Invalid choice. Try again.")
        room() 
        
def wait_3():
    print("""
You decide to wait still considering wether to drink the coffee or go back to the closet.
In your comtemplation the closet door seems to have disappeared.
""")
    wait_3_choice = input("\nYou have two choices drink the 'coffee' or 'wait'.").lower()
    if wait_3_choice == "coffee":
        coffee()
    elif wait_3_choice =='wait':
        wait_3()
    else:
        print("Invalid choice. Try again.")
        wait_3()       

def coffee():
    print("""
You drink the coffee you feel weird but nothing seems to happen.
The closet door has disappeared. 
""")
    coffee_choice = input("\nYou have one choice 'wait'.").lower()
    if coffee_choice == "wait":
        wait_4()
    else:
        print("Invalid choice. Try again.")
        coffee()   
        
def wait_4():
    print("""
You wait and slowly you feel the energy in you rise as the caffeine kicks in. 
The lightbulb keeps flickering quicker and quicker then it burns out.
You are left in darkness and the hard old carpet shifts into a softer cold tile.
You are in the void a cold dark and empty place where you are doomed to wonder for eternity. 
Except you feel different you feel a warmth like the sun is shining on you. 
You wake up in your kitchen with a cup of coffee in your hand.
YOU WIN
""")
    wait_2_choice = input("\nYou have two choices start'again' or 'quit'.").lower()
    if wait_2_choice == "again":
        intro()
    elif wait_2_choice =='quit':
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        wait_4() 
        
def closet_2():
    print("""
You enter the closet it looks normal.
""")
    closet_2_choice = input("\nYou have two choices back to the 'bedroom' or 'wait'.").lower()
    if closet_2_choice == "bedroom":
        otherside()
    elif closet_2_choice =='wait':
        wait_2()
    else:
        print("Invalid choice. Try again.")
        closet_2()        
        
def bathroom():
    print("""
You entered the bathroom and it seems normal but the mirror is off.
You have no reflection. 
You touch the mirror and your hand passes through the mirror.
You pull back but you cant get your arm out so you decide to enter the mirror.
""")
    bathroom_choice = input("\nYou have one choice into the 'mirror'.").lower()
    if bathroom_choice == "mirror":
        otherside()
    else:
        print("Invalid choice. Try again.")
        bathroom()      
        
def attic():
    print("""
You climb up the the attic and turn on the light.
The ladder to the attic snapped from your weight so you can't go back down. 
There is a hole in the attic bringing a cold draft. 
There is a closed box on the floor you don't recognize it.
""")
    attic_choice = input("\nYou have two choices back out the 'hole' or look into the'box'.").lower()
    if attic_choice == "hole":
        hole()
    elif attic_choice =='box':
        box()
    else:
        print("Invalid choice. Try again.")
        attic()   

def hole():
    print("""
You look out the hole.
Tt looks just like the street your house is on and the front of your house looks the same.
So you jump out of the hole expecting to hit the hard ground below. 
You contemplate your decisions up to this point.
What has led you to jumping out of a hole in an attic about to break some bones on the ground. 
You brace for the impact but you fall right through the dirt.
You are in the void a place of eternal darkness where you are now falling for eternity.
GAME OVER
""")
    hole_choice = input("\nYou have two choices start'again' or 'quit'.").lower()
    if hole_choice == "again":
        intro()
    elif hole_choice =='quit':
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Try again.")
        hole() 

def box():
    print("""
You open the box to see your bedroom from the perspective of the ceiling.
This bedroom at the bottom of the box looks more normal than the one you were in.
It looks like it is dawn instead of the timeless place you were in before. 
So out of morbid curiosity, you enter the box.
""")
    box_choice = input("\nYou have one choice into the 'box'.").lower()
    if box_choice == "box":
        otherside()
    else:
        print("Invalid choice. Try again.")
        box() 
  
intro()