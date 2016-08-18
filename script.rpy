# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
init:
    image lovein normal = "lovein2.png"
    image prof normal = "prof2.png"
    image road="road.jpg"
    image city="city.png"
    image back="back.png"
    image gym="gym.png"
    image forest="forest.png"
    image town="town.jpg"
# Declare characters used by this game.
define player_name = Character("#C9C9C9")
define a= Character(color = "#C9C9C9")
define z = Character('Trainer', color="#C9C9C9")
define b = Character("??????", color="#000000") 
define c = Character('Professor Maple', color="#87421F")
define d= Character("Announcer", color="#000080")
define rival_name= Character("#830303")
define e = Character(color = "#830303")

# The game starts here.
label start:

    
    show back
    
    "You walk through Pritempts Plains minding your own business, when a large foot knocks you over."
    
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
        
        show back 
       
        show prof normal
       
       
        
        
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
                
                hide prof normal
                
                jump choice4_1
                
            "I want to battle my pokemon.":
                
                jump choice3_2
                
            "I want to level up my pokemon so they can mega evolve.":
                
                jump choice3_2
                    
    label choice3_2:
        
        c "Great! Now I'd would love for you to visit Lowestof Gym and battle the pokemon trainers there!"
        
        hide prof normal 
        
        jump choice4_2
           
           
    label choice4_1:
        
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
                    
        "{i} Leggo Raichu{/i}":
            
                    d "Alright now come on out Novice Eliza!"
                    
                    'Novice Eliza sends out Crawdaunt and Walrein.'
                    
                    '{i}Cue battle transition{/i}'
                    
                    jump choice5_2
                    
                    
    label choice4_2:
            
        "On your way to Lowestof Gym, someone stops you in the middle of the street."
        
        show lovein normal
        
        a "Hey! You just got here huh?"
        
        $ rival_name = renpy.input("What is your rival's name?")
        
        $ rival_name = rival_name.strip()
        
        $ e = rival_name
        
        e " Yeah I did......hold up. Is that a pokeball I see? You finally got one too. I've been itching to battle you this whole time."
        
        e "{i}LET'S GO{/i}"
        
        "They send out Luxray and Garchomp"
        
        menu: 
            
            "Send out our starter!":
                
                jump choice5
            
            "Send out {i}Based Raichu{/i}.":
                
                jump choice5fail
                
        label choice5fail:
            
            e "I knew you could never beat me!"
            
            a "Ugh shut it! Since we were little you've always been a sore winner!"
            
            e "The only sore thing should be your pokemon after that butt whoopin!"
            
            a "I'm out of here! And I'll get you next time!"
            
            e "{i}Sure you will{/i}"
            
            hide lovein normal
            
            jump choice5done
            
        label choice5:
            
            e "Dang, how'd you get so good?"
            
            a "I had a little practice."
            
            e "We'll see how long that practice keeps you ahead of the game!"
            
            a "{i}Yeah yeah keep talking, you're such a sore loser.{/i}"
            
            e "I don't have time to hang around with softies,{i}ta ta{/i}!"
            
            hide lovein normal
            
            jump choice5done
            
        
        label choice5_2:
            
            d "Up next is Poke Maniac Zack!"
            
            "Zack sends out Golbat and Magnemite!"
            
            menu:
                
                "Send out your holy starter!":
                    
                    a "We barely won that won!"
                    
                "Send out that big foot Raichu!"
                    
                    
                        
            
            
               
        
                
        
        
        
        
        
        
        
        
            
            
            
            
            
    
        
        
            

        return

