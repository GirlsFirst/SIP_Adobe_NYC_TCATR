﻿# You can place the script of your game in this file.

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
    image spork smile ="sporksmilesmirk.png"
    image spork angry ="spork.png"
    image samurai ="samurai.png"
    image mom ="mom.png"
    image home = "home.jpg"
    image room ="room.jpg"
    image battle ="mommy.png"
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
define s = Character("Electra", color="#FFFF00")
define t = Character("Takeo", color="#8E2323")
define m = Character("Mother", color="#7F00FF")
# The game starts here.

label splashscreen:




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
       
     
        
        c "Say, what's your name kiddo?"
        
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
                    
                    hide lovein normal
                    
                    jump choice9 

            label choice8:
                
                show forest 
                
                "On my way to Olempec Town, I ran into whats-their-face."
                
                show lovein normal
                
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
                        
                        hide lovein normal
                        
                        hide forest
                        
                        jump choice10
                        
                
                    
                    
                    "Use Raichu":
                        
                        e "That was insane!" 
                        
                        e "I'll report you to the Pokemon League for cheating"
                        
                        e "You give your pokemon steriods or something?"
                        
                        a "You really only have to be the bare mininum to beat you."
                        
                        e "Very funny"
                        
                        e "Do you think you could teach me how to battle sometime?"
                        
                        a "Maybe later if I have time!"
                        
                        hide lovein normal
                        
                        hide forest 
                        
                        jump choice10
                        
            
            label choice10
            
            show mountain
            
            a "Let's see... which way do I have to go?"
            
            a "I think I have to climb that mountain over there."
            
            a "This is gonna be abuse on my legs."
            
            "Better get started right now!"
            
            show mtown
            
            a "That took way too long to get here."
            
            a "What is this, some kind of bathhouse town?"
            
            show lovein normal
            
            e "You know it's really weird when you talk to yourself."
            
            e "It almost makes it seem like you have friends!"
            
            a "{i}Hah! That was so funny!{/i}"
            
            "How did I know they were following me.."
            
            e "Think that there is a volcano or somthing underneath the mountain, that's why there are so many bath houses."
               
            a "I guess that makes sense.."
            
            e "You heading to the gym?"
            
            a "Did you think I climbed the mountain to take a bath?"
            
            e "Well no.... dang you're so hard to talk to! See you later."
            
            hide lovein normal
            
            a "........ That was weird."
            
            hide mtown
            
            show peak
            
            a "Okay I'm going to take this gym down!"
            
            show spork smile 
            
            s "Are you really now?"
            
            "Oh dang this lady heard."
            
            s "Well you're in for a {i}shock kid{/i}, cause I don't lose easily"
            
            s "You ready, let's fight RIGHT NOW!"
            
            a "Wait real quick before we start, why are we fighting so high above the ground?"
            
            s "Less talking more fighting!"
            
            hide spork smile
            
            show spork angry
            
            d "Gym Leader Electra sent out Raichu, Electabuzz and Emolga."
            
                menu:
                    
                    "Send out ya starter pokemon":
                        
                        "Awww yeah! That was way to easy!"
                        
                        jump choice0
                        
                    "Send out Raichu":
                        
                        "That was really tough since she had a Raichu too."
                        
                        jump choice0
                        
            label choice0:
            
                        hide spork angry
                        
                        show spork smile
                        
                        s "You really know your stuff kid. You put up alot of {i}resistance{/i}!"
                        
                        a "Thank you for taking the time to fight me!"
                        
                        s "Stay safe!"
                        
                        hide spork smile
                        
                        hide peak
                        
                        jump choice11
                    
                    
            label choice9:
                
                show mountain
                
                show lovein normal
                
                e "How much longer do we have to walk"
                
                e "Are we there yet???"
                
                a "Does it look we are there yet?"
                
                a "We so obviously have to climb that mountain to get to the gym."
                
                a "So stop your belly-aching!"
                
                e "Okay Okay"
                
                hide mountain 
                
                hide lovein normal
                
                show mtown
                
                show lovein normal
                
                a "And here we are!"
                
                e "Okay but why are there so many bathtubs?"
                
                a "Well I did a little research while we were wallking here, apparently there is a dormant volcano underneath this mountain."
                
                e "So they don't have to pay the heat bill, lucky."
                
                a "Let's keep going, it looks like Olempec's gym is at the top."
                
                hide mountain
                
                hide lovein normal
                
                show peak
                
                show lovein normal
                
                a "Why are you shaking like that?"
                
                e "Leave me alone, can't you see how high up we are?"
                
                a "You afraid of heights or something?"
                
                e "As a matter of fact I am! And I'm proud!"
                
                e "I think the pokegods never wanted us to be this close to the sky!"
                
                b "I'm es-static that you've climbed this high to come see me."
                
                b "Ohm...I'm over here kids."
                
                "We turned around to see a fashionable lady stading behind us."
                
                s "Watts up? I'm this gym's leader Electra."
                
                s "I'm shocked to see a couple kids hoping to battle me!"
                
                s "Watt are you waiting for? {i} Let's Go!{/i}"
                
                e "Wait before you guys start fighting I have a quick question."
                
                e "Did you decide to build this gym at the top of a mountain? Maybe that's why you never get any younger visitors!"
                
                e "And you seemed like such a {i} grounded {/i} person."
                
                show spork angry 
                
                s "Tell your friend to be quiet before I throw them off this cliff."

                d "Electra sent out Raichu, Electabuzz and Emolga"
                
                menu:
                    
                    "Send out your starter!":
                        
                        a "Of course I won!"
                        
                        jump choice01
                        
                    "Send out the Raichu":
                        
                        hide spork angry
                        
                        show lovein normal
                        
                        e "Why would you send out Raichu when she has one?"
                        
                        a "I still won, chill out!"
                        
                        hide lovein normal
                        
                        show spork smile
                        
                        s "Is your red-headed friend always like this?"
                        
                        a "Pretty much 24/7."
                        
                        s "I feel bad for you."
                        
                        s "Take care kids!"
                    
                        s "It would really {i} hertz{i} my feelings if you didn't come back to visit!"
                        
                        hide spork smile
                        
                        show lovein normal
                        
                        e "If she makes one more pun I might throw up."
                        
                        hide peak 
                        
                        hide lovein normal
                        
                        show templeroad
                        
                        show lovein normal
                        
                        e "The last place we have to go to is Taketomi Island."
                        
                        a "I've always wanted visit this place!"
                        
                        e "The place is very ....different."
                        
                        e "Well culturally that is."
                        
                        a "I'm definelty getting a very different vibe as we come up to the drawbridge."
                        
                        e "I heard their gym leader is a samurai or something!"
                        
                        a "Okay now I'm really excited!"
                        
                        e "Don't get to excited, you still have to beat them."
                        
                        a "Chill {i}mom{/i}, I can handle this!"
                        
                        hide templeroad 
                        
                        hide lovein normal
                        
                        show shrine
                        
                        show lovein
                        
                        a "This place is so cool."
                        
                        e "Too much red, it's hurting my eyes!"
                        
                        a "How do you do your hair in the morning then?"
                        
                        e "..............."
                        
                        e "I think we need to find some type of clearing, that's where the gym is."
                        
                        a "And how do you know all of this?"
                        
                        e " I literally just looked at the billboard that said town map"
                        
                        a "Okay then you lead the way!"
                        
                        hide shrine
                        
                        hide lovein
                        
                        show temple
                        
                        a "Wow look at this view!"
                        
                        a "And I can see the gym from here too!"
                        
                        show lovein normal
                        
                        a "And you just had to ruin the moment didn't you?"
                        
                        e "Quit your {i}gasping{/i} and {i}gawking{/i} and let's go already."
                        
                        a "I'm taking note to come here by myself next time."
                        
                        hide temple
                        
                        hide lovein normal
                        
                        show intemple
                        
                        "It's so cool."
                        
                        e "This place looks decent."
                        
                        e "Could use a little bit of interior design."
                        
                        a "Okay if this place looks decent, what does your room look like, the Taj Mahal?"
                        
                        e "Chill, I was just giving my constructive criticism."
                        
                        b "Ahh young love."
                        
                        e "First of all, I'm not in love, second of all who said that?"
                        
                        a "I am in sound agreement with you on this one!"
                        
                        hide lovein normal
                        
                        b "If you guys came here to flirt then I kindly ask you to leave."
                        
                        a "Listen, {i}whoever you are{/i}, I came to battle and my friend came to nag... I mean tag along."
                        
                        show samurai
                        
                        o "That's great!, I'm Takeo, and I specialize in fighting pokemon!"
                        
                        a "You're really a samurai!"
                        
                        o "You thought this place was just a tourist attraction huh?"
                        
                        a "No but a samurai, who do you fight in this day and age?"
                        
                        o ".........."
                        
                        o "My inner demons ¯\_(ツ)_/¯ ."
                        
                        o "Alright LET'S GO!"
                        
                        d "Gym Leader Takeo sent out Hariyama, Machamp and Hitmontop."
                        
                           menu:
                            
                            "Send out your starter.":
                                
                                "This battle was really hard for some reason!"
                                
                                o "I always go down kicking and scratching, or should I say kicking and {i}punching{/i}?"
                                
                                "Cue laugh track"
                                
                                jump choice13
                                
                            "Who's that pokemon? It's {i}Raichu{/i}." :
                             
                                a "That was like taking candy from a baby."
                                
                                a "Or should I say taking steriods from a weight lifter."
                                
                                o "Hey!, You know I would never take any performance enhancing substanc-"
                                
                                "Cue laugh track"
                                
                                jump choice13
                                
        label choice13:
                            
                            
                            o "Come visit me if you ever need any help kids!"
                            
                            o "It gets pretty lonely living out here in a temple."
                            
                            hide samurai
                            
                            show lovein normal
                            
                            e "I fully believe the protein shakes are getting to that guy's head."
                            
                            a "Don't mske fun of him, he could hunt you down one day!"
                            
                            e "I'd actually love to see him try."
                            
                            hide intemple
                            
                            hide lovein normal
                            
                            show road
                            
                            a "We know where the last gym leader is."
                            
                            show lovein normal
                            
                            e "This has been the moment you've been waiting for!"
                            
                            a "Ah I recognize this path more than anyone else."
                            
                            e "I guess this is where I drop you?"
                            
                            a "Yeah I'll see you ar-"
                            
                            e "Listen I've had alot of fun going on this trip with you."
                            
                            e "I'm really happy you let me {i} nag{/i} along."
                            
                            e "Come see me if you need anything."
                            
                            a "Wow they're being surprisingly nice today."
                            
                            hide lovein normal 
                            
                            hide road
                            
                            show home
                            
                            "It smells just like I left it, like fresh laundry and cheap perfume."
                            
                            b "Since you're back here I guess you're ready to take me on."
                            
                            a "Okay this isn't a mistery I know who's talking."
                            
                            show mom
                            
                            m "Do you know how much I've missed you?"
                            
                            a "I could take a guess."
                            
                            m "No matter, are you ready to battle?"
                            
                            m "I've been waiting since you were a child for this day!"
                            
                            m "You're finally going to take over the family gym!"
                            
                            m "Hurray let's go outside!"
                            
                            a "Wait Mom I need time to think."
                            
                            a "I'll be in my room."
                            
                            hide home
                            
                            hide mom
                            
                            show room
                            
                            "I need some serious advice."
                            
                            "I really don't know if I have what it takes it beat mom."
                            
                            "Maybe I should look to someone for advice."
                            
                            menu:
                                
                                "Our Rival":
                                    
                                    jump choicer
                                    
                                "Devin the Bug Gym Leader":
                                    
                                    jump choiced
                                    
                                "Electra the Electric Gym Leader":
                                    
                                    jump choicee
                                    
                                "Takeo the Fighting Gym Leader":
                                    
                                    jump choicet
                                    
                      #finish choice11 solo route to takeomi island, beat rival after samurai battle.
                      
                      #finish end of mom gym route, get advice from any one of the mentors and beat mom. then establish love based on route.
              
        label choice11:
                
                    show templeroad
                    
                    a "Ugh Man! I'm so exhausted! How am I gonna have energy for the gym battle?"
                    
                    "{i}WORRIES{/i}"
                    
                    a "What if I've come this far just to fail!"
                    
                    "I will not! mother, I'm going to do this for us!"
                    
                    hide templeroad
                    
                    show shrine 
                    
                    show lovein normal
                    
                    e "Well, Well, Well If it isn't you?"
                    
                    "Look of curiosty"
                    
                    e "Where ya headed, I know your on your way to a battle, why not refresh your skills before you take an L?"
                    
                    a "Okay sure, Mr.I THINK I Know It All"
                    
                    "Love Interest sends out Dragonite "
                    
                    menu:
                    
                        "Use your starter!":
                        
                            e "Goodluck Hun"
                            
                            a "I don't need it!"
                            
                            "Now how was that for your smack talking, now get out of my way I have a battle to win"
                            
                            jump choice 14
                        
                        
                            
                        "{i}Raichu{i}":
                    
                            e "Wow! I thought you were supposed to be getting better, should not be lacking out here" 
                                
                            a "Woop woop, I'm determined my training needs to pay off eventually."
                            
                            "You say mockingly"
                            
                            e "Hope your ready for that Samurai!"
                            
                            a "Yea, yea see you later hater."
                            
                            jump choice 14
                
                
                
        label choice 14:    
                    
                    hide lovein normal
                    
                    hide shrine
                    
                    show temple 
                    
                    a "OMG! This is it, no turning back"
                    
                    "THIS IS FOR YOU MOM!"
                    
                    "Continues onward to the temple."
                    
                    hide temple    
               
                    show intemple
                    
                    "ENTERS Temple"
                    
                    t "Who goes there?"
                    
                    "I look around, but I don't see anyone."
                                
                    "FLOP!"                    
                    
                    "A man with a sword, and dressed like a Samurai appears to have fallen neck first in front of me"
                    
                    show samurai
                    
                    t "I'm sorry about that rusty entrance but hi I'm The Takeomi Gym Leader. I was told to expect you from a special someone"
                    
                    a "Hello, I'm here to earn my experience I would like to Battle you Master Takeo "
                    
                    t"That's what I'm here for laddy , step in my arena, get ready to begin in 10 minutes"
                    
                    "Takeo sends out Hariyama"
                    
                    menu:
                        "Use your starter!":
                        
                            t "OH MY!, I didn't expect that powerful pokemon, how did I let a twerp beat me, now BEAT IT!"
                        
                            jump choice 15
                            
                            
                        "{i}Raichu{i}":
                        
                            t "OH MY!, I didn't expect that powerful pokemon, how do I let a twerp beat me, now BEAT IT!"
                            
                            jump choice 15
                        
        label choice 15:
                
                    hide intemple 
                    
                    hide samurai
                    
                    show city
                    
                    "I want to hurry, how can I make it to home fast enough?"
                    
        label choice001_for:
                    
                    "What do I use?"
                    
                    menu:
                        
                        "Passerby's Car-ride":
                                                jump choice001_loop
                        
                        
                        "Bike":
                                jump choice001_done

        label choice001_loop:
                    
                        "I don't trust strangers"
                        
                        jump choice001_for
                        
        label choice001_done:
                    
                    hide city
                    
                    show road
                    
                    show prof normal
                    
                    c "So you've made it back in one piece, how's Raichu and your starter holding up?"
                                
                    a "Pretty healthy ma'am. We're on our way to our last gym battle any advice or LUCK your able to give?"
                    
                    c "Yes, I sure do, don't let those nerves effect your outcome on your next battle. Clear eyes full hearts Can't lose!!"
                    
                    a "Thank you so much helping me out in the beginning. I have to go visit my Mom. I'll {i}catch{/i} you later."
                    
                    "HAHA!, pokemon pun"
                    
                    hide road 
                    
                    hide prof normal
                    
                    show house 
                    
                    "Yes I've Made It!"
                    
                    hide house 
                    
                    show home 
                    
                    show mom normal
                    
                    m "Hi Sweety, How was your battling experience with Master Takeo I told him to expect you, but I have some terrible news and I need your help right away!"
                    
                    a "Of Course Mom , what is it ?"
                    
                    m "See I wanted to surprise you and be your last gym leader battle , but this person came and Took over my gym and asked to battle you for it back"
                    
                    a "take me there, NOW! "
                    
                    "Who would take over an innocent lady's property ; just to battle with me?"
                    
                    hide home
                    
                    hide mom normal
                    
                    show mommy
                    
                    show mom
                    
                    m "You see, that person right there!"
                    
                    hide mom 
                    
                    show lovein normal
                    
                    e "Hello darling, nice to see she follows directions. What does this battle and this Gym mean to you and your precious mommy {i}HAHA{/i} "
                    
                    a "Honestly don't care, you've crossed the line here!"
                    
                    "FINAL BATTLE FOR COLOSSEUM GYM!"
                    
                    "Love Interest sends out Dragonite"
                        
                        menu:
                    
                            "Use your starter!":
                                
                                e "Fair fighting huh? You've trained, keep at the Colosseum Gym"
                            
                                jump choice 16
                                
                            "{i}Raichu{i}":
                                e "Fair fighting huh? You've trained, keep at the Colosseum Gym"
                                
                                jump choice 16
                                
                                
                                
                                
                label choice 16:
                    

                    hide lovein normal
                    
                    show mom 
                    
                    m "Thank you so much sweety, words can't describe how much I love you and appreciate your training skills, I want you to use those skills you learned and Take The Colosseum Gym in your hands"
                    
                    m " Don't let ANYONE come in between you and your journey. You can become the BEST Gym Leader"
                    
                    "OBTAINED THE COLOSSEUM GYM KEY"
                    
                    m "Now I'm going home. How about you go check out your new Gym"
                    
                    a "Okay, thank you Mom. I love you so much. See you later!"
                    
                    "You run off excitedly."
                    
                    hide mom normal
                    
                    show colosseum
                    
                    "THIS is mine? THIS is what I've spent my journey to accquire?, Did I achieve my goal?"
                    
                        
                    
                    
                    
                            
                    
                    
                    
                    
                            
                            
                            
                            
                            
                            
                            
                            
                            
                        
                            
                            
                        
                        
                        
                        
                        
                        
                        
                           
                        
                
                
                   
                   
                
                
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
                
                        

