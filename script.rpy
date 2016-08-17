# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player_name = Character("#C9C9C9")
define a= Character(color = "#C9C9C9")
define z = Character('Trainer', color="#C9C9C9")
define b = Character("??????", color="#000000")
define c = Character('Professor Maple', color="#87421F")



# The game starts here.
label start:

    "You walk through Solaceon Town, minding your own business, when a large foot knocks you over."
    
    "Raising your head you see a Raichu running off into the distance."
                      
    b "Think Fast"

    "Three Pokeballs fall to your feet."
     
    b "Make sure that Raichu doesn't get away!"
    
    z "You want to me choose one huh?"
    
    menu:
        "Turtwig":
                    jump choice1_T
        
        "Chimchar":
                    jump choice1_C
    
        "Piplup":
                    jump choice1_P
                      
                      

    label choice1_T:
    
        z "Turtwig use absorb!.....wait how do I know all this?"
    
        "The raichu became confused but started to run away." 
    
        jump choice1_fail
    
    label choice1_C:
        
        z "Chimchar use ember!.....wait how do I know all this?"
        
        "The raichu got inflicted with a burn and turned its tail down in surrender." 
        
        jump choice1_done
    
    label choice1_P:
        
        z "Piplup use Bubble!....wait how do I know all this?"
        
        "It was a critical hit! The raichu fainted."
        
        jump choice1_done
    
    label choice1_done:
        b "Throw this pokeball at it!"
        
        z " Alright, I'll give it a shot!"
        
        "...."
        
        "...."
        
        "...."
        
        "{i}click{/i}"
        
        b "That was awesome kid!"
       
        jump choice2_name
        
    label choice1_fail: 
        z "{i}sigh{/i} ...that raichu was halfway to Eterna City by now"
        
        b "{i}Hey!{/i} ,that was a good try. You've got a lot of potential!"
        
        jump choice2_name
    
    label choice2_name:
    
        "You raise your head to see an intellectual looking woman grinning back at you."
        
        c "Say, what's your name kiddo?"
        
        $ player_name = renpy.input("What is your name?")
        
        $ player_name = player_name.strip()
        
        $ a = player_name
        
        c "That's a nice name!"
        
        c "You know what? You've been such a big help today, I'll let you keep that pokemon if you want!"
        
        a "Let me think about it."
        
    
        
        return

