# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
init:
    image lovein normal = "lovein.png"
    image prof normal = "prof2.png"
    image road="road.jpg"
    image city="city.png"
    image back="back.png"
    image gym="gym.jpg"
    image forest="forest.png"
    image town="town.jpg"
    image devin normal ="bugleader.png"
    image trainer ="trainer1.png"
    image fighter ="fighter.png"
    image karate ="fighter2.png"
# Declare characters used by this game.
define player_name = Character("#C9C9C9")
define a= Character(color = "#C9C9C9")
define z = Character('Trainer', color="#C9C9C9")
define b = Character("??????", color="#000000") 
define c = Character('Professor Maple', color="#87421F")
define d= Character("Announcer", color="#000080")
define rival_name= Character("#830303")
define e = Character(color = "#830303")
define f = Character("Devin", color = "006400")
# The game starts here.

label splashscreen:
    $ renpy.movie_cutscene('lion.avi')
    
    return
    
    jump start



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
    
        "The raichu became confused." 
    
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
                
                hide back
                
                hide prof normal
                
                jump choice4_1
                
            "I want to battle my pokemon.":
                
                jump choice3_2
                
            "I want to level up my pokemon so they can mega evolve.":
                
                jump choice3_2
                    
    label choice3_2:
        
        c "Great! Now I'd would love for you to visit Lowestof Gym and battle the pokemon trainers there!"
        
        hide prof normal 
        
        hide back
        
        jump choice4_2
           
           
    label choice4_1:
        
        show city
        
        "You make your way to Colosseum City ready to battle and see trainer's different types of pokemon."
        
        d "All trainers come to the front of the stadium."
        
        "The battle begins! Who are you going to send out?"
        
    menu:
    
        "Our Starter Pokemon we used!":
                
                    d "Alright now come on out Rookie Keith!"
                    
                    show trainer
                    
                    "Rookie Keith sends out Houndor and Sneasel." 
                    
                    "{i}Cue battle transition{/i}"
                    
                    a "The was way too easy!" 
                    
                    hide trainer
                    
                    jump choice5_2
                    
        "{i} Leggo Raichu{/i}":
            
                    d "Alright now come on out Fighter Bryan!"
                    
                    show fighter
                    
                    'Fighter Bryant sends out Crawdaunt and Walrein.'
                    
                    '{i}Cue battle transition{/i}'
                    
                    hide fighter
                    
                    jump choice5_2
                    
                    
    label choice4_2:
        
        show road   
        
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
            
            hide road
            
            jump choice5done
            
        label choice5:
            
            e "Dang, how'd you get so good?"
            
            a "I had a little practice."
            
            e "We'll see how long that practice keeps you ahead of the game!"
            
            a "{i}Yeah yeah keep talking, you're such a sore loser.{/i}"
            
            e "I don't have time to hang around with softies,{i}ta ta{/i}!"
            
            hide lovein normal
            
            hide road
            
            jump choice5done
            
        
        label choice5_2:
            
            d "Up next is Karate Kid Zack!"
            
            "Zack sends out Golbat and Magnemite!"
            
            show karate
            
            menu:
                
                "Send out your holy starter!":
                    
                    a "I barely won that won!"
                    
                    hide karate
                    
                    jump choice6

                "Send out that big foot Raichu!":
                
                    a "We won that by a mile!"
                    
                    hide karate
                    
                    hide city 
                    
                    jump choice6

        label choice5done:
              
            show gym
             
            show devin normal 
            
            a "We're here at the {i}Lowestof Gym{/i} to battle the current Gym Leader, Devin."
            
          
            
            d "Gym Leader Devin has just sent out Heracross, Vespequien, and Kricketot as his team of Pokemon. Oooh, fierce!"
            
            d "Which Pokemon do you want to enter into battle with first?"
            
            menu:
            
                "Starter Pokemon":
                
                    d "Wow! That was heartbreaking. Truly! The winner lost the duel to Gym Leader Devin."
                    
                    a "Aw that sucks! I hope I'll do better next time."
                        
                "{i}Raichu{i}":
                
                    d "Wow! That was spectacular. Amazing! The winner has won the duel and receives a $20 gift card to Apple Bees."  
                    
                    a "Woop woop, I'm glad my training paid off."
            hide gym

            hide devin normal
            
            jump choice8
                
        label choice6:
            
            show road  
            
            a "On to the next gym!"

           
            
            show lovein normal
            
            e "Where do you think you're going?"
            
            a "Hey! You just got here huh?"
            
            a "I'm on my way to Lowestofe Gym to get stronger so I can take over mom's gym!"
            

            
        
            $ rival_name = renpy.input("What is your rival's name?")
        
            $ rival_name = rival_name.strip()
        
            $ e = rival_name 

            e "Yeah,so what?!........ Listen my mom doesn't want me traveling alone and she told me to find you!"

            e "Do you think we could go together?..."

            jump choice6loop

        label choice6loop:

            a "Let me think about it"

            menu: 

                "Yes":

                    "{i}Seriously{/i} ahem that's cool I guess. "

                    jump choice7

                "No":

                    "............."

                    "I'm not leaving here until you say yes."

                    jump choice6loop

        label choice7:

            a "On to the gym!"

            hide road

           

            show town

            

            e "I heard that this gym leader is a little boy."

            e "What a joke."

            e "I think you can take him."

            a "You're supporting me in this endeavour?"

            e "Don't take what I say the wrong way...."
            
            hide lovein normal 
            
            hide town
            
            
            show gym 
            
            show lovein normal
            
            a "We're here at the {i}Lowestof Gym{/i} to battle the current Gym Leader, Devin."
            
            e "I think I see him!"
            
            hide lovein normal
          
            show devin normal
            
       
            
            d "Gym Leader Devin has just sent out Heracross, Vespequien, and Kricketot as his team of Pokemon. Oooh, fierce!"
            
            d "Which Pokemon do you want to enter into battle with first?"
            
            menu:
            
                "Starter Pokemon":
                
                    d "Wow! That was heartbreaking. Truly! The winner lost the duel to Gym Leader Devin."
                    
                    a "Aw that sucks! I hope I'll do better next time."
                        
                "{i}Raichu{i}":
                
                    d "Wow! That was spectacular. Amazing! The winner has won the duel and receives a $20 gift card to Apple Bees."  
                    
                    a "Woop woop, I'm glad my training paid off."
                    
                    hide devin normal
                    
                    show lovein normal
                    
                    e "I knew you could do it!"

                    hide gym
                    
                    jump choice9 

            label choice8:
                
                show forest 
                
                "On my way to Olempec Town, I ran into whats-their-face."
                
                e "Ready for another battle?"
                
                a "Ready to leave me alone?"
                
                e "Now let {i}me{/i} think about it"
                
                e "..........."
                
                e "Nah, I love it when you get ticked off."
                
                a "Alright alright let's go!"
                
                menu:
                    
                    "Use your starter!":
                        
                        e "I've gotten used to your pokemon's tricks!"
                        
                        e "Try harder next time, and cry harder while your at it!"
                        
                        a "I'm so tired of this...."
                        
                        e "I could give you some tips on winning if you want?"
                        
                        "I'm out of here"
                        
                        jump choice10
                        
                
                    
                    
                    "Use Raichu":
                        
                        e "That was insane!" 
                        
                        e "I'll report you to the Pokemon League for cheating"
                        
                        e "You give your pokemon steriods or something?"
                        
                        a "You really only have to be the bare mininum to beat you."
                        
                        e "Very funny"
                        
                        e "Do you think you could teach me how to battle sometime?"
                        
                        a "Maybe later if I have time!"
                        
                        jump choice10
                        
            #label choice 10, going to Olempec City alone, introduce Spork and battle her..after that is samurai gym!
                
            #label choice9 going with love interest to Olempec City and battling Spork, love dialogue and rom com stuff insues....after that is samurai gym!
                        

