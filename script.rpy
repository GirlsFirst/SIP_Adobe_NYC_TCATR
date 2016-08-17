# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player_name = Character("#C9C9C9")
define a= Character(color = "#C9C9C9")
define z = Character('Trainer', color="#C9C9C9")
define b = Character("??????", color="#000000")
define c = Character('Professor Maple', color="#87421F")
define d= Character("Announcer", color=("#000080")


# The game starts here.
label start:

    "You walk through Bredon Town, minding your own business, when a large foot knocks you over."
    
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
        z "{i}sigh{/i} ...that raichu was halfway to Barcombe City by now"
        
        b "{i}Hey!{/i} ,that was a good try. You've got a lot of potential!"
        
        jump choice2_name
    
    label choice2_name:
    
        "You raise your head to see an intellectual looking woman grinning back at you."
        
        c "Say, what's yo ur name kiddo?"
        
        $ player_name = renpy.input("What is your name?")
        
        $ player_name = player_name.strip()
        
        $ a = player_name
        
        c "That's a nice name!"
        
        c "You know what? You've been such a big help today, I'll let you keep the pokemon if you want!"
        
    label choice2_for:  
        
        a "Let me think about it."
        
    menu: 
        "Yes":
                jump choice2_done
        "No":
                jump choice2_loop
                
    label choice2_loop:
        
        "Seriously?!, reconsider it!"
        
        jump choice2_for
    
    label choice2_done:
        
        c "Take good care of them! Their your new best friend!"
        
        a "I can't wait to tell my mom." 
        
        c "So...since you're pretty much a pokemon trainer now, what are some of your aspirations?"
        
        menu:
            
            "I want to takeover my mother's gym.":
            
                c "Hmm, you've got a lot of work ahead of you trainer. I'd like you to visit Colosseum Gym."
            
                jump choice4_1
                
            "I want to battle my pokemon.":
                
                jump choice3_2
                
            "I want to level up my pokemon so they can mega evolve.":
                
                jump choice3_2
                    
    label choice3_2:
        
        c "Great! Now I'd would love for you to visit Lowestof Gym and battle the pokemon trainers there!"
           
        jump choice4_2
           
           
    label choice4_2:
        
        "You make your way to Colosseum City ready to battle and see trainer's different types of pokemon."
        
        d "All trainers come to the front of the stadium."
        
        "The battle begins! Who are you going to send out?"
        
    menu:
    
        "Our Starter Pokemon we used!":
                
                    d "Alright now come on out Rookie Keith!"
                    
                    "Rookie Keith sends out Houndor and Sneasel." 
                    
                    "{i}Cue battle transition{/i}"
                    
                    a "The was way too easy!" 
                    
                    jump choice5_2
                    
        "{i}Raichu{/i}":
            
                    d "Alright now come on out Novice Eliza!"
                    
                    'Novice Eliza sends out Crawdaunt and Walrein.'
                    
                    '{i}Cue battle transition{/i}'
                    
                    jump choice5_2
                    
                    
    label choice4_1
        
        
        
        
        
        
        
            
            
            
            
            
    
        
        
            

        return

