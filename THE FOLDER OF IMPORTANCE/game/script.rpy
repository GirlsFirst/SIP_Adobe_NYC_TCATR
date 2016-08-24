# You can place the script of your game in this file.

# Declare images below this line, using the image statement.    


init:
    image lovein normal = "lovein.png"
    image prof normal = "prof2.png"
    image road="road.jpg"
    image city="city.jpg"
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
    image samurai ="sam.png"
    image mom ="mom.png"
    image home = "house.jpg"
    image room ="room.jpg"
    image battle ="mommy.png"
    image temple ="temple.jpg"
    image peak ="peak.jpg"
    image splash="newraichu.png"
    image turt ="turtwig.png"
    image pip="piplup.png"
    image chim="chimchar.png"
    image lux ="luxray.png"
    image hari="hariyama.png"
    image drag="dragonite.png"
    image colo ="colosseum.png"
    image kang="kang.png"
    image butter="butterfree.png"
    image raichu="raichu.png"
    image ball="ball.png"
    image black="black.png"
    image garden ="garden.jpg"
    
# Declare characters used by this game.
define player_name = Character("#C9C9C9")
define a= Character(color = "#C9C9C9")
define z = Character('Trainer', color="#C9C9C9")
define b = Character("??????", color="#000000") 
define c = Character('Professor Maple', color="#87421F")
define d= Character("Announcer", color="#000080")
define rival_name= Character("#FF0000")
define e = Character(color = "#FF0000")
define f = Character("Devin", color = "006400")
define s = Character("Electra", color="#FFFF00")
define t = Character("Takeo", color="#8E2323")
define m = Character("Mother", color="#7F00FF")
# The game starts here.

label splashscreen:

    $ renpy.movie_cutscene('lion.avi')
    
    show splash with dissolve
    
    hide splash
    
    return

label start:

    play sound ("bensound-straight.mp3")
    
    show back
    

    
    "You walk through Pritempts Plains minding your own business, when a large foot knocks you over."
    
    show raichu
    
    "Raising your head, you see a Raichu running off into the distance."
                      
    b "Heads up! Think Fast!"

    hide raichu

    show ball

    "Three Pokeballs fall to your feet."
     
    b "Make sure that Raichu doesn't get away!"
    
    z "Am I supposed to choose a Pokeball?"
    
    hide ball
    
    
    label choicejk:
            
            menu:
                
                "Turtwig":
                            
                            show turt
                            
                            "Are you sure?"
                            
                            menu:
                                
                                "Yes":
                                    
                                    hide turt
                                    
                                    jump choice1_T
                                    
                                "No":
                                    
                                    hide turt
                                    
                                    jump choicejk
                
                "Chimchar":
                          
                          show chim
                          
                          "Are you sure?"
                          
                          menu:
                              
                                "Yes":
                                    hide chim
                                    
                                    jump choice1_C
                                
                                "No":
                                    
                                    hide chim
                                    
                                    jump choicejk
                                    
                                
            
                "Piplup":
                    
                    show pip
                    
                    "Are you sure?"
                    
                    menu:
                        
                                "Yes":
                                    
                                    hide pip
                                    
                                    jump choice1_P
                                    
                                "No":
                                    
                                    hide pip
                                    
                                    jump choicejk
                          
                      

    label choice1_T:
        
        show turt
        
        z "Turtwig used absorb!.....Wait, how do I know all this?"
    
        "The Raichu became confused." 
        
        hide turt
        
        jump choice1_done
    
    label choice1_C:
        
        show chim
        
        z "Chimchar use ember!.....Wait, how do I know all this?"
        
        "The Raichu got inflicted with a burn and turned its tail down in surrender." 
        
        hide chim
        
        jump choice1_done
    
    label choice1_P:
        
        show pip
        
        z "Piplup use Bubble!....Wait, how do I know all this?"
        
        "It was a critical hit! The Raichu fainted."
        
        hide pip
        
        jump choice1_done
    
    label choice1_done:
        
        b "Throw this pokeball at it!"
        
        z " Alright, I'll give it a shot!"
        
        show ball
        
        "....1"
        
        "....2"
        
        "....3"
        
        "{i}click{/i}"
        
        b "That was awesome, kid!"
        
        hide ball
        
        jump choice2_name
    
    
    label choice2_name:
        
        show back 
       
        show prof normal
       

        "You raise your head to see an intellectual looking woman grinning back at you."
       
        stop sound 
        
        play sound ("bensound-funkyelement.mp3")
        
        c "I'm Professor Maple. I know everything about Pokemon and their behavior."
        
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
        
        "Seriously?! Reconsider it!"
        
        jump choice2_for
    
    label choice2_done:
        
        c "Take good care of them! They're your new best friend!"
        
        a "I can't wait to tell my mom." 
        
        c "So... Since you're pretty much a pokemon trainer now, what are some of your aspirations?"
        
        menu:
            
            "I want to take over my mother's Pokemon gym!":
            
                c "Hmm, you've got a lot of work ahead of you, trainer. I'd like for you to visit Colosseum Gym."
                
                c "You'll meet a lot of powerful trainers there. If you battle your way to the top, you'll be able to advance."
                
                c "After defeating all the gyms in your path, your mom will await you. She's the last gym leader, isn't she?"
                
                a "Uh... Okay. I didn't expect this to happen, but being a trainer sounds pretty exciting."
                
                "You look down at your pokemon and grin."
                
                a "Let's do this!"
                
                hide back
                
                hide prof normal
                
                jump choice4_1
                
            "I want to battle with my pokemon!":
                
                jump choice3_2
                
            "I want to level up my pokemon so they can evolve!":
                
                jump choice3_2
                    
        label choice3_2:
        
        c "Great! Now I would love for you to visit Lowestof Gym and battle the pokemon trainers there. If you beat their gym leader, you'll be able to advance onwards."
        
        c "The last gym leader is your mom, right? If you beat her, you'll become the best trainer in the world!"
        
        c "Until someone else comes along and beats you, that is."
        
        c "Along the way, you'll bond with your Pokemon and if they get strong enough, you can evolve them!"
        
        hide prof normal 
        
        hide back
        
        stop sound
        
        jump choice4_2
           
           
        label choice4_1:
        
        stop sound 
        
        show city
        
        "You make your way to Colosseum City, ready to battle, and see trainers with different types of pokemon."
        
        a "Wow... This place is huge. And kind of scary. Kind of terrifying. Jeez, I should train a bit more."
        
        hide city
        
        show back
        
        "You head into the tall grass and fight a bunch of Weedle and Starly."
        
        a "I'm training up my Pokemon!"
        
        "..."
        
        "...Hours later..."
        
        a "THEY'RE LEVEL 15! FINALLY!"
        
        hide back
        
        show city
        
        "You head back into the city."
        
        a "I'm ready! Let's do this!"
        
        "You head to the stadium, and hear a loud booming voice."
        
        d "All trainers come to the front of the stadium!"
        
        a "Oh man, it's my turn."
        
        "The battle begins! Who are you going to send out?"
        
        play sound ("bensound-epic.mp3")
        
        menu:

        
                "Our Starter Pokemon we used!":
                
                    d "Alright, now come on out, Rookie Keith!"
                    
                    show trainer
                    
                    "Rookie Keith sends out Houndor and Sneasel." 
                    
                    "{i}Cue battle transition{/i}"
                    
                    "Houndor and Sneasel get absolutely demolished by your amazing starter Pokemon."
                    
                    a "The was way too easy!" 
                    
                    hide trainer
                    
                    jump choice5_2
                    
                    
                "{i}Let's go, Raichu!{/i}":
                    
                    show raichu
                    
                    d "Alright now come on out, Fighter Bryan!"
                    
                    hide raichu
                    
                    show fighter
                    
                    'Fighter Bryan sends out Crawdaunt and Walrein.'
                    
                    '{i}Cue battle transition{/i}'
                    
                    "Raichu uses Uber Thunderbolt on Fighter Bryant's Pokemon! They black out."
                    
                    hide fighter
                    
                    
                    jump choice5_2
                    
                    
        label choice4_2:
            
                show road   
            
                "On your way to Lowestof Gym, someone stops you in the middle of the street."
            
                
                show lovein normal
                
                a "Well, well. Guess who's here. I haven't seen them since... This morning."
                
                $ rival_name = renpy.input("What is your rival's name?")
                
                $ rival_name = rival_name.strip()
                
                $ e = rival_name
                
                e "Hey. You finally got a pokemon? Wow! Took you long enough. Jeez, I've been waiting for this! I've been itching to battle you this whole time."
                
                e "{i}LET'S GO!{/i}"
               
                
        label choice23:
            
            play sound ("bensound-epic.mp3")
            
            show lovein normal
            
            show road
            
            "They send out Dragonite."
            
            show drag
            
            menu: 
                
                "Send out our starter!":
                    
                    jump choice5
                
                "Send out {i}Based Raichu{/i}.":
                    
                    hide drag
                    
                    show raichu
                    
                    jump choice5fail
                    
        label choice5fail:
                
                "Their Dragonite uses Dragon Claw. Your Raichu passes out."
                
                e "I knew you could never beat me!"
                
                a "Ugh, shut it! Since we were little you've always been a sore winner!"
                
                e "The only sore thing should be your pokemon after that butt whoopin'!"
                
                a "I'm out of here! And I'll get you next time!"
                
                e "{i}Sure you will!{/i}"
                
                "Your Pokemon black out."
                
                hide raichu
                
                hide lovein normal
                
                hide road
                
                stop sound
                
                show town
                
                
                "You rush to the Pokemon center hurriedly, cradling your Pokemon in your arms. The nurse heals your Pokemon."
                
                a "Whew, you guys are alright. Let's go back and beat them up now."
                
                hide town
                
                jump choice23
                
                
                
                
        label choice5:
            
            "Your starter destroys the Dragonite! The Dragonite roars in pain and faints."
            
            e "Dang, how'd you get so good?"
            
            a "I had a little practice."
            
            e "We'll see how long that practice keeps you ahead of the game!"
            
            a "{i}Yeah, yeah, keep talking. You're such a sore loser.{/i}"
            
            e "I don't have time to hang around with softies, {i}bye{/i}!"
            
            hide lovein normal
            
            a "Wow... What an aggressive start to my Pokemon journey. Didn't see them coming, really."
            
            a "Pretty cool, though. Now I can brag to them about my Pokemon. They {i}are{/i} my childhood friend, after all."
            
            "You whistle to yourself as you make yourway to Lowestof Gym."
            
            hide road
            
            stop sound
            
            jump choice5done
            
        
        label choice5_2:
            
            d "Up next is Karate Kid Zack!"
            
        label choice72:
            
            "Zack sends out Golbat and Magnemite!"
            
            show karate
            
            menu:
                
                "Send out your holy starter!":
                    
                    "Their Golbat uses Bite. Your Pokemon are wounded!"
                    
                    a "Ah shoot! I lost that one!"
                    
                    "Your Pokemon black out."
                
                    
                    hide karate
                    
                    "You rush to the Pokemon center and heal your Pokes."
                    
                    jump choice72
            
                "Send out that big foot Raichu!":
                    
                    hide karate
                    
                    show raichu
                    
                    "Raichu used Discharge!"
                    
                    
                    a "Nice job, Raichu! We won that by a mile!"
                    
                    hide karate
                    
                    
                    hide city 
                    
                    jump choice6

        label choice5done:
              
            show gym
             
            
            a "Finally here! Whew, my feet are tired."                                                    
            
            a "We're here at the {i}Lowestof Gym{/i} to battle the current Gym Leader, Devin."
                  
            show devin normal 
            
            a "{i}The gym leader is a little boy? Uh....{/i}"
            
            a "Whelp. Get ready to get rekt, kid!"
            
            "You smile confidently and step onto the stage."
            
            play sound ("bensound-epic.mp3")
            
            label choice99:
            
            d "Gym Leader Devin has just sent out Butterfree. Oooh, fierce!"
            
            show butter
            
            d "Which Pokemon do you want to enter into battle with first?"
            
            menu:
            
                "Starter Pokemon":
                    
                    show butter
                    
                    "The Butterfree uses Gust! Ouch, that must hurt."
                    
                    a "Argh! We're losing! Come on, we can do this!"
                    
                    "..."
                
                    d "Wow! That was heartbreaking."
                    
                    d "Truly heartbreaking!"
                    
                    d "The winner lost the duel to Gym Leader Devin."
                    
                    a "Aw, that sucks! I hope I'll do better next time."
                    
                    "Your Pokemon black out."
                    
                    "You rush to the Pokemon center and heal your Pokes."
                    
                    hide butter
                    
                    jump choice99
                    
                "{i}Raichu{i}":
                
                    hide butter
                
                    hide devin normal
                
                    show raichu
                    
                    a "Raichu, use Spark!"
                    
                    "As Raichu sends bolts of electricity towards the Butterfree, the crowd cheers in delight."
                    
                    show butter
                    
                    "The Butterfree cries out in pain and faints!"
                    
                    hide butter
                
                    d "Wow! That was spectacular. Amazing! The winner has won the duel and receives a $20 gift card to Apple Bees."  
                    
                    a "Whoop whoop! I'm glad my training paid off."
                    
                    hide raichu 
                    
                    d "The underdog trainer has just won the gym battle!"
                    
                    "As the crowd cheers, Devin walks up to you silently. He hands you the Lowestof Gym Badge, and waves at the crowd."
                    
                    "His smile is a tiny bit sad."
                
                    a "Ah... Good match. I had fun. Uh... I'll see you around."
                    
                    d "With this Gym Badge, this trainer will be able to go to Olempec Town, where Leader Electra awaits! Let's give a round of applause and send the trainer on their way!"
                    
                    "The audience cheers."
                    
                    "You walk out of the gym slowly, with a bright smile on your face."
                    
                    hide gym

                    hide devin normal
                    
                    stop sound
                    
                    jump choice8
                
        label choice6:
            
            stop sound
            
            show road  
            
            a "Onto the next gym!"

            show lovein normal
            
            play sound ("bensound-buddy.mp3")
            
            e "Where do you think you're going?"
                                            
            hide lovein normal
                                                
            "A voice calls out to you."
                                       
            "You turn to see your childhood friend."
            
            a "Hey! You just got here, huh? I haven't seen you since... This morning. Hahah."
            
            a "I'm on my way to Lowestof Gym to get stronger so I can take over mom's gym!"
                                                                
            show lovein normal
                                                                                    
            $ rival_name = renpy.input("What is your rival's name?")
        
            $ rival_name = rival_name.strip()
        
            $ e = rival_name 

            e "Yeah, so what?!........ Listen, my mom doesn't want me traveling alone and she told me to find you!"

            e "Do you think we could go together...?"

            jump choice6loop

        label choice6loop:

            a "Let me think about it."

            menu: 

                "Yes":

                    e "{i}Seriously? YES!{/i}"
                    
                    e "Ahem.. I mean, that's cool. I guess. Haha."

                    jump choice7

                "No":

                    "............."
                    
                    "Your rival looks at you disbelievingly."
                    
                    e "WHAT?!@ We've known each other for so long! Come on, we're best friends, right?!"
                    
                    "........"

                    e "I'm not leaving here until you say yes."

                    jump choice6loop

        label choice7:

            a "Okey doke. On towards the gym!"
            
            hide city
            
            hide road
            
            hide lovein normal

            show town
            
            show lovein normal

            e "I heard that this gym leader is a little boy."

            e "What a joke."

            e "I think you can take him."

            a "You're supporting me in this endeavour?"

            e "Don't take what I say the wrong way...."
                   
            "You glance at your rival out of the corner of your eye. They're looking the other way, hands in pockets."
                                                                                                                   
            a "Hmm..."
            
            hide lovein normal 
            
            hide town
            
            
            show gym 
            
            show lovein normal
            
            a "We're here at the {i}Lowestof Gym{/i} to battle the current Gym Leader, Devin."
            
            e "I think I see him!"
            
            e "Get ready for the first gym battle of your life!"
            
            hide lovein normal
          
            show devin normal
            
       
        label choice123:
        
            stop sound 
            
            play sound ("bensound-epic.mp3")
            
            "You step onto the stage. The crowd is cheering, watching your every move."
            
            a "{i}Wow, this is kind of nerve-wracking.{/i}"
            
            d "Gym Leader Devin has just sent out Butterfree. Oooh, fierce!"
            
            show butter
            
            d "Which Pokemon do you want to enter into battle with first?"
            
            menu:
            
                "Starter Pokemon":
                    
                    "The Butterfree uses Gust! Ouch, that must hurt."
                    
                    a "Argh! We're losing! Come on, we can do this!"
                    
                    "..."
                
                    d "Wow! That was heartbreaking."
                    
                    d "Truly heartbreaking!"
                    
                    d "The winner lost the duel to Gym Leader Devin."
                    
                    a "Aw, that sucks! I hope I'll do better next time."
                    
                    "Your Pokemon black out."
                    
                    "You rush to the Pokemon center and heal your Pokes."
                    
                    "..."
                    
                    a "I'll be back for sure!!"
                    
                    "..."
                    
                    stop sound
                    
                    jump choice123
                    
                "{i}Raichu{i}":
                
                    hide devin normal
                
                    show raichu
                
                    a "Raichu, use Spark!"
                    
                    "As Raichu sends bolts of electricity towards the Butterfree, the crowd cheers in delight."
                    
                    a "YEAH, LET'S GO, THAT'S RIGHT, TAKE THAT LITTLE BOY!!!!!!"
                    
                    show butter
                    
                    "The Butterfree cries out in pain and faints!"
                    
                    hide butter
                    
                    stop sound
                
                    d "Wow! That was spectacular. Amazing! The winner has won the duel and receives a $20 gift card to Apple Bees."  
                    
                    a "Whoop whoop! I'm glad my training paid off."
                    
                    hide devin normal
                    
                    show lovein normal
                    
                    e "I knew you could do it!"
                    
                    "You turn to see your rival running towards you, with an uncharacteristically bright smile plastered onto their face."
                    
                    a "Hey! Yeah, that was {i}waaaaay{/i} too easy. I bet you could do it too; you have a Dragonite, after all."
                    
                    e "Honestly, I think so too. Well, I'm still proud of you for beating your first ever gym leader!"
                    
                    hide lovein
                    
                    show devin normal
                    
                    "Your conversation is interrupted by Devin, who hands you your Lowestof Gym Badge."
                    
                    "You thank him and turn back to your rival, who is waiting patiently by the door of the gym."
                    
                    hide devin normal
                    
                    show lovein
                    
                    a "So, what next?"
                    
                    e "Next up is Olempec Town, where an Electric type Gym leader lady awaits!"
                    
                    a "Oh man, more fighting. Alright, let's go!"
                    
                    "You grin at each other as you exit the gym."
                     
                    hide gym
                   
                    hide raichu
                    
                    hide lovein normal
                    
                    stop sound
                    
                    jump choiceplzwork 
        
        label choiceplzwork:
                
                play sound ("bensound-buddy.mp3")
                
                show mountain
                
                show lovein normal
                
                e "How much longer do we have to walk...?"
                
                e "Are we there yet...?"
                
                a "Does it look we are there yet?"
                
                a "We so obviously have to climb that mountain to get to the gym."
                
                a "So stop your belly-aching!"
                
                e "SERIOUSLY? Ugh, fine."
                                    
                "You laugh, amused by your friend's antics. They look grouchy as they glare at the looming mountain ahead."
                                                                                       
                a "Hey, you'll be fine. You won't die."                                                                       
                
                hide mountain 
                
                hide lovein normal
                
                show mtown
                
                ".............."
                
                show lovein normal
                
                a "And here we are!"
                
                e "Oh man. I literally thought I was going to die. I'm so tired."
                
                e "Okay, but why are there so many hot springs?"
                
                a "Well I did a little research while we were walking here. Apparently there is a dormant volcano underneath this mountain."
                
                e "So they don't have to pay the heat bill? How lucky."
                
                a "Let's keep going, it looks like Olempec's gym is at the top."
                
                e "Wait... Let's take a break first and grab some food."
                
                "..."
                
                "You stop at a shop and grab some turkey sandwiches."
                
                a "These good?"
                
                e "Perfect. Let's eat them on the way!"
                
                hide mountain
                
                hide lovein normal
                
                show peak
                
                "....."
                
                show lovein normal
                
                stop sound
                                                           
                "You arrive at the top of the mountain. The ground is littered with piles of snow."
                                                           
                "Your rival stands close to you, shivering. Their lips are purple."                                           
                
                a "Uhh... Why are you shaking like that? Are you alright?"
                
                e "L-Leave me alone... Can't you see how high up we are?"
                                                                         
                "You hear their teeth chatter."                                                         
                
                a "You afraid of heights or something? Or are you just cold?"
                
                e "As a matter of fact, I am both suffering from my fear of heights as well as the cold."
                
                e "I doubt that the Pokegods ever wanted us to be this close to the sky!"
                                                                                         
                hide lovein normal                                                                      
                
                b "I'm es-static that you've climbed this high to come see me."
                
                b "Ohm...I mean, {i}I'm{/i} over here, kids."
                
                
                show spork smile
                
                "We turned around to see a fashionable lady standing behind us."
                
                s "Whats up? I'm this gym's leader, Electra."
                
                s "I'm shocked to see a couple kids hoping to battle me! Y'all should grow up first."
                
                s "Hah, I'll have a lot of fun beating you up!"                                                           
                                                                           
                s "What are you waiting for? {i} Let's Go!{/i}"
                
                hide spork smile
                
                show lovein normal
                
                e "Wait. Before you guys start fighting, I have a quick question."
                
                e "Why did you decide to build this gym at the top of a mountain? Maybe that's why you never get any visitors!"
                
                e "And you seemed like such a {i}grounded {/i} person. Hah, get it? Grounded."
                
                a "Oh my god."
                
                hide lovein normal
                
                show spork angry 
                
                s "Tell your friend to be quiet before I throw them off this cliff."
                
                a "Lets! Battle!"
        
        label choice90:
            
                show peak
                
                show spork angry
            
                stop sound
                
                play sound ("by.mp3")
                
                s "Prepare to get destroyed."
            
                d "Gym Leader Electra sent out Luxray!"
                
                show lux
                
                hide spork angry
                
                menu:
                    
                    "Send out your starter!":
                        
                        "Electra's Luxray used Volt Switch, quickly followed by a Wild Charge!"
                        
                        a "Argh!"
                        
                        "You have no time to react."
                                            
                        a "Ah, shoot! This Luxray is so strong!"
                        
                        "You cry in dismay as your Pokemon faints in your arms."
                        
                        a "I can't believe I lost!"
                        
                        hide lux
                        
                        show spork smile
                        
                        "Your Pokemon black out."
                        
                        a "I'll be back for sure!!!"
                    
                        hide peak
                        
                        show mtown
                        
                        "You rush to the Pokemon center and heal your Pokes."
                        
                        "..."
                        
                        hide mtown
       
                        jump choice90
                        
                    "Send out the Raichu":
                        
                        hide lux 
                        
                        show raichu
                                 
                        "Your Raichu uses Thunder Wave. It's not very effective but it looks like Electra's Luxray is paralyzed!"
                                                                                                          
                        "Electra's Luxray passes out as your Raichu follows up with Thunder Fang."
                        
                        a "Yes! I think we won!"
                        
                        stop sound
                                                      
                        hide raichu                            
                        
                        show lovein normal
                        
                        e "Why would you send out Raichu when she has a Luxray? They're both electric types."
                        
                        a "I still won, chill out fam!"
                        
                        hide lovein normal
                        
                        play sound ("happy.mp3")
                        
                        show spork smile
                        
                        s "Is your red-headed friend always like this?"
                        
                        a "Pretty much 24/7."
                        
                        s "I feel bad for you."
                                                                                     
                        s "Well, good luck to you guys, wherever you go. Here is the Olempec Gym Badge."
                        
                        "Electra hands a shiny yellow badge to you. You can't help but gawk."
                        
                        a "IT'S SO SHINY!"
                        
                        "Electra laughs and pats your arm."
                                                                                     
                        s "And good luck with your friend too. Don't bicker too much!"
                        
                        "She looks over at your rival and laughs."
                        
                        s "Ahh, young love."  
                        
                        a "Urgh, stop embarrassing me."
                                                                                                   
                        stop sound
                        
                        jump choice01
                        
                        
        label choice01:
            
                        
                        play sound ("bensound-buddy.mp3")
                        
                        s "Take care, kids! The next gym is at Taketomi Island. I hope you lose! If you do, come back and {i}chill{/i} with me."
                                                                                
                        "Her eyebrow twitches. Looks like she's bitter about losing."
                                                                                
                        "{i}Hah... Sure we'll lose.{/i} (sarcasm, obviously)"
                        
                        "{i}Also, we're not coming back.{/i}"
                                                                
                        hide spork smile
                                                                
                        show lovein normal                                        
                    
                        "You turn to the redhead next to you. Their face is starting to turn blue from cold."
                                                                                                             
                        "{i}Nope... Definitely not coming back.{/i}"   
                                           
                        hide lovein normal                   
                        
                        show spork smile
                                           
                        s "It would really {i}hertz{/i} my feelings if you didn't come back to visit!"                   
                         
                        hide spork smile
                                                                                                      
                        show lovein normal                                                                               
                                                                                                      
                        e "If she makes one more pun I might throw up."
                        
                        hide peak 
                        
                        hide lovein normal
                        
                        show templeroad
                        
                        show lovein normal
                        
                        e "The last place we have to go to is Taketomi Island."
                        
                        a "I've always wanted to visit that place!"
                        
                        e "That place is very ....Different."
                        
                        e "Culturally, that is."
                        
                        a "I'm definitely getting a very different vibe as we come up to the drawbridge."
                        
                        e "I heard their gym leader is a samurai or something!"
                        
                        a "Wow! Okay, now I'm really excited!"
                        
                        e "Don't get too excited! You still have to beat them."
                        
                        a "Chill out, {i}mom{/i}, I can handle this!"
                        
                        a "Ugh, honestly I wish you could help me out sometimes."
                        
                        "Your friend laughs, and pats you on the head."
                        
                        e "More fun this way! Don't worry, I'll always stick around if you're in trouble."
                        
                        "You brush their hand off and give them a playful shove."
                        
                        a "Yeah, I know. Deep down. {i}Very{/i} deep down. You're not very obvious when it comes to friendship, you know?"
                        
                        e "...Well, I guess. I {i}do{/i} care, sometimes."
                        
                        "You turn to see your redhead friend, whose face matches the color of their hair."
                        
                        a "Chill, fam. Don't make me feel embarrassed."
                        
                        "You feel slightly thrown off, as an awkward pause ensues. You decide to start whistling randomly, and look in the other direction."
                        
                        hide templeroad 
                        
                        hide lovein normal
                        
                        show shrine
                        
                        "......"
                        
                        a "Wow!"
                        
                        show lovein normal
                        
                        a "Hey, we're here! This place is so cool."
                        
                        e "Too much red, it's hurting my eyes!"
                        
                        a "How do you look at yourself in the mirror then?"
                                            
                        e "What?"
                        
                        a "Like, your hair."
                        
                        a "You feel me?"
                        
                        e "..............."
                                            
                        e "Haha. I'm impressed. Yeah, you're so funny!"
                                                          
                        "They look unimpressed."                                  
                        
                        e "I think we need to find some type of clearing, that's where the gym is."
                        
                        a "And how do you know all of this?"
                        
                        e "I literally just looked at the billboard that said, 'town map.'"
                        
                        a "WOW, you're so smart! Okay then, you lead the way."
                        
                        hide lovein
                        
                        "You roll your eyes as your rival starts walking in a random direction."
                        
                        a "You better not get us lost."
                        
                        "In front of you, your friend sighs dramatically."
                        
                        e "We'll be fine!"
                        
                        hide shrine
                        
                        show temple
                        
                        play sound ("happy.mp3")
                            
                        
                        a "Are we here yet? Is this the place? Did you really lead us to the right area?"
                        
                        a "I knew I could trust you!"
                        
                        "You tackle your friend, beaming brightly. They roll their eyes at you."
                        
                        a "Hey, that's my line! I mean, my move! Whatever!"
                        
                        "......"
                        
                        "You guys keep walking."
                        
                        a "Wow, look at this view!"
                        
                        a "And I can see the gym from here too!"
                        
                        show lovein normal
                        
                        "Your friend stops and turns around. They snap their fingers in your face."
                        
                        a "Ahh!"
                        
                        a "And you just had to ruin the moment, didn't you?"
                        
                        e "Quit your {i}gasping{/i} and {i}gawking{/i} and let's go already."
                        
                        a "I'm taking note to come here by myself next time. Not with some random stranger that I obviously hadn't known my entire life."
                        
                        e "Hey! I was so nice to you when you were little! Especially when your mom left to defend her gym."
                        
                        stop sound
                        
                        e "..."
                        
                        play sound ("sad.mp3")
                        
                        e "Sorry. I didn't mean to bring up bad memories."
                        
                        "They pat your back, obviously trying very hard to be reassuring."
                        
                        e "It's okay though, right?"
                        
                        e "I was always there for you."
                        
                        a "Yeah... I know. Sorry."
                        
                        a "I'm really glad you're travelling with me, honestly."
                        
                        a "Would be super lonely without you."
                           
                        "You sigh and force a smile."
                        
                        a "Come on, let's walk. I'm not the type to get all mushy and sad for no reason."
                        
                        stop sound
                        
                        "Your friend peers in your face. They seem really relieved that you've pulled yourself together."
                        
                        e "Alright. Let's go kick some samurai butt!"
                
                        hide temple
                        
                        hide lovein normal
                        
                        hide shrine
                        
                        show intemple
                        
                        "..."
                        
                        a "Wow!"
                        
                        a "{i}It's so cool!{/i}"
                        
                        "A giant statue sits at the very end of the temple hall. On the sides, behind the columns, is empty air."
                        
                        a "Wow, that's kind of dangerous..."
                        
                        a "Someone could get hurt if they fall down there."
                        
                        show lovein normal
                        
                        e "This place looks decent, I guess."
                        
                        e "Could use a little bit of interior design."
                        
                        a "Okay... If this place looks just {i}decent{/i}, what does your room look like? The Taj Mahal?!"
                        
                        e "Chill, I was just giving my constructive criticism."
                        
                        b "Ahh, young love."
                        
                        e "First of all, I'm not in love. Second of all, who said that?"
                        
                        a "I am in sound agreement with you on this one!"
                        
                        a "For once."
                        
                        hide lovein normal
                        
                        b "If you guys came here to flirt, then I kindly ask for you to leave."
                        
                        a "Listen, {i}whoever you are{/i}, I came to battle and my friend came to nag... I mean, uh, tag along."
                        
                        "Your rival shoves their elbow into your side aggressively." 
                        
                        e "Hey! I'm here to help you along on your journey."
                        
                        a "Ouch! I don't care, just stop that."
                        
                        "You push them away and turn towards the direction of voice."
                        
                        show samurai
                        
                        "..."
                        
                        a "WHOA!"
                        
                        a "Argh! Get out of my face!"
                        
                        t "Yeah, that's great. Hi guys. I'm Takeo, and I specialize in fighting Pokemon. I haven't had challengers in months, though."
                        
                        a "...Wow! You're really a samurai!"
                        
                        t "You thought this place was just a tourist attraction, huh?"
                        
                        a "No, but a samurai.... Who do you fight in this day and age?"
                        
                        t ".........."
                        
                        t "My inner demons :^) ."
                        
                        t "Alright, quit beating around the bush, LET'S GO!"
                                                                            
        label choice45:
            
                        stop sound
                        
                        play sound ("bensound-epic.mp3")
                        
                        d "Gym Leader Takeo sent out Hariyama!"
                        
                        a "Oh shoot! I forgot to heal my Raichu!"
                        
                        show hari
                        
                        hide samurai
                        
                        menu:
                            
                            "Send out your starter.":
                                
                                hide hari
                                
                                show samurai
                                
                                t "You think you can beat me with that little thing? You're naiive!"
                                
                                hide samurai
                                
                                show hari
                                
                                "Hariyama used Close Combat! It sends your starter Pokemon flying towards your friend, who is standing at the edge of the temple, right next to the columns!"
                                
                                stop sound
                                
                                play sound ("woo.mp3")
                                
                                a "Oh no! Watch out!"
                                
                                hide hari
                                
                                show lovein normal
                                
                                e "Urgh!"
                                
                                "Your rival catches your injured Pokemon, barely able to stop its impact!"
                                
                                "Together, they wobble precariously on the edge of the temple!"
                                
                                e "OH MY JEEZ I'M GOING TO DIE!!!"
                                
                                hide lovein normal
                                
                                "The screams of your friend echo through the hall. Your eyes widen in shock!"
                                
                                a "Hang on!"
                                
                                "You're overcome with fear. Your legs shake, refusing to budge as you watch your companions on the brink of potential death."
                                
                                a "I'm coming...!"
                                
                                "You force your feet to move! Your heart pounds rapidly, knowing that the situation had just taken a turn for the worse."
                                
                                "You dash towards the two desperately, praying for the best."
                                
                                show lovein normal
                                                          
                                e "Ahhh!"
                                
                                "You reach out and grab onto your friend's hand."
                                
                                "..."
                                
                                a "Come on!"
                                
                                "..."
                                
                                hide lovein normal
                                
                                "With a grunt of effort, you heave them back onto their feet. You just saved your friends!"
                                
                                show lovein normal
                                
                                e "Urgh..."
                                
                                "They collapse against you, knees shaking."
                                
                                a "Hey, are you alright?!@"
                                
                                e "I-I'm okay..."
                                
                                hide lovein normal
                                
                                stop sound
                                
                                "You gently set your rival and wounded Pokemon on the ground, and turn towards Takeo, eyes blazing."
                                
                                a "Who designed this temple?! Anyone could get hurt falling off the sides!"
                                
                                "Angrily, you call on the Pokemon Center nurse, who just happened to be at the temple for her daily worship."
                                
                                "As she hurriedly tends to your starter Pokemon, you glare at Takeo, who stands nearby."
                                
                                a "I can't believe that happened! I could literally smack you right now!"
                                
                                show samurai
                                
                                t "Hey! I'm sorry! I didn't know that would happen... But don't worry!"
                                
                                t "If your heart is free of demons, you will never die!"
                                
                                a "UGH!"
                                
                                "Stomping your foot in frustration at losing your battle and having such a frightening encounter, you cross your arms and turn away."
                                
                                t "H-Hey... I'm sorry, alright? Look, I know I'm not supposed to do this, but I feel {i}really{/i} bad that your friends almost died."
                                
                                t "Uhh... Ahem. Here, take this. No one saw, okay?"
                                
                                "Takeo hurriedly thrusts a shiny thing into your hand."
                                
                                hide samurai
                                
                                "Upon closer inspection, you realize that it's the gym badge!"
                                     
                                "..."
                                
                                a "I really didn't expect that."
                                
                                "Without so much as looking back at Takeo, you grab your friend and turn leave the temple."
                                
                                stop sound
                                
                                jump choice13
                                
                            "Send out Raichu, who is injured!" :
                                
                                hide hari
                                
                                show raichu
                                                    
                                a "Let's go Raichu! You're the best!"
                                                        
                                "Raichu gets beaten up by Takeo's Hariyama."
                                                                   
                                hide raichu
                                
                                show samurai

                                t "Dude, your Raichu wasn't even full health to begin with!"
                                
                                "Ugh... I made a mistake."
                                
                                "You take your Raichu to the Pokemon center to get healed up."
                                
                                "..."
            
                                "You really should have had more insight."
                                
                                jump choice45
                                
        label choice13:
                            stop sound
                            
                            play sound ("bensound-buddy.mp3")
                            
                            t "Come visit me if you ever need any help, kids!"
                                                                              
                            t "It gets pretty lonely living out here in a temple."                                                  
                            
                            t "Good luck on your journey. May the love gods be in your favor!"
                                                                                              
                            "Takeo looks into the distance wistfully. He also looks a bit apologetic."
                                                                              
                            a "{i}What's up with this dude...{/i}"
                            
                            stop sound
                            
                            hide samurai
                            
                            hide intemple
                            
                            show road
                            
                            show lovein normal
                            
                            
                            e "Jeez, what the heck!"
                            
                            play sound ("bensound-love.mp3")
                                       
                            "You turn to look at your rival. They're blushing. You stifle a laugh."           
                                       
                            a "I fully believe that the protein shakes are getting to that guy's head."
                            
                            e "For saying whatever that thing was about love gods, and the fact that you had to save me!"
                            
                            a "Hey, chill out. I'm glad you're okay."
                            
                            "You give them a hug, and smile brightly."
                            
                            a "You know, we got the gym badge."
                            
                            e "Wait, seriously?! I can't believe you!"
                               
                            "Your rival laughs along with you, and the previous heartstopping events seem to have been forgotten."
                                                                                                                                  
                            hide lovein normal
                            
                            "...."
                                  
                            "You walk in comfortable silence."
                                                              
                            "That almost-catastrophe seems to have brought you two closer."   
                                                                                           
                            "...."                                                               
                            
                            a "We know where the last gym leader is."
                             
                            show lovein normal                                         
                                                                     
                            e "Your mom... She's waiting."                                         
                            
                            stop sound
                            
                            
                            
                            e "This has been the moment you've been waiting for!"
                            
                            a "Ah, I recognize this path more than anyone else. This is our old house, before I moved out to live with my dad."
                            
                            e "I guess this is where I drop you?"
                            
                            a "Yeah I'll see you ar-"
                                      
                            play sound ("bensound-romantic.mp3")         
                            
                            e "Listen... I've had a lot of fun going on this trip with you."
                            
                            e "I'm really happy you let me {i}nag{/i} along."
                            
                            e "Come see me if you need anything."
                                 
                            a "Fine, fine."
                                 
                            "Taken aback by their somewhat brutal and unexpected honesty, you can't help but blush."
                            
                            a "Uhm... You've been surprisingly nice recently. I guess. Uh..."
                                          
                            a "It's not even like we're not seeing each other again... Why are we getting so sentimental?"
                                                     
                            hide lovein normal                         
                                                     
                            "But as you say these words, memories flash through your mind."
                                                     
                            hide road
                            
                            stop sound
                            
                            play sound ("sad.mp3")
                                                     
                            show black                         
                                                     
                            "You can still hear the echo of the door closing in front of you, as your father holds you back."
                                                     
                            "Your chubby young fingers are reaching for the door. You can barely see out of your blurry, teary vision."
                                                     
                            a "M-Mom..."
                                                     
                            "Beside you, your childhood friend holds onto your hand reassuringly."
                                                     
                            e "It's okay. I'm here! We can be together. Forever..."
                                            
                            "The young voice echos through your mind..."
                                            
                            "{i}End flashback{/i}"
                                            
                            hide black
                            
                            hide hari
                            
                            show road
                                            
                            show lovein normal
                            
                            stop sound
                            
                            play sound ("bensound-romantic.mp3")
                                            
                            a "...Forever."
                                            
                            e "Huh?"
                                            
                            "They look surprised, and peer into your eyes inquisitively."
                                            
                            a "Ahh! Nothing!"
                                            
                            "You can't help but stammer, looking away and blushing heavily."
                                                                                            
                            a "I mean..."
                                         
                            a "We'll always be together. Forever."
                                  
                            a "That's what you said back then... And that's what I'll say now."
                                                                                               
                            e "Hey."
                                    
                            "You look up, and suddenly you're engulfed in a hug."
                                                           
                            e "I'll literally see you tomorrow morning if you want me to come. Don't get so sentimental on me, okay? I'm bad with this kind of stuff."
                                                                                                                                                                      
                            "But as these words leave their mouth, you can't help but to notice the blush staining their cheeks."                                                                                                                                          
                        
                            a "Jeez... I got it. See you around."
                                                                           
                            hide lovein                                               
                                                                           
                            "You squeeze them tightly and let go, turning to face the last challenge before you."                                               
                                                                                                            
                            stop sound
                            
                            hide lovein normal 
                            
                            hide road
                            
                            show home
                            
                            "It smells just like I left it, like fresh laundry and cheap perfume."
                            
                            b "Since you're back here I guess you're ready to take me on."
                            
                            a "Okay... This isn't a mystery. I know who's talking."
                            
                            show mom
                            
                            m "Do you know how much I've missed you?"
                            
                            a "I could take a guess."
                                                     
                            a "Mom, I just said bye to someone I cared about a lot, so let's get on with it."                         
                            
                            m "Are you sure you're ready to battle me?"
                            
                            m "I've been waiting since you were a child for this day!"
                            
                            m "You're finally going to take over the family gym!"
                            
                            m "Hurray, let's go outside!"
                                           
                            hide mom                
                            
                            a "Okay..."
                                           
                            hide home
                                           
                            show garden
                                           
                            show mom               
                                           
                            "Your mother turns to face you."
                                           
                            play sound ("by.mp3")               
                                           
                            m "I hope you're ready for this."
                                                             
                            "I have no choice. I have to send out both of my Pokemon if I want to win this!"
                                                                                                            
                            m "Go! Kangaskhan!!!"
                                                 
                            show kang
                                                 
                            "Kangaskhan appears before you, roaring into your face!"
                                                                                    
                            a "UGH! THAT SMELLS!"
                                                 
                            a "Come on guys, let's go!"
                                                 
                            hide kang
                                                 
                            show raichu                     
                                                 
                            "Together, Raichu and your starter use their strongest abilities on mom's Kangaskhan!" 
                                                                                                                  
                            a "Good job, Raichu!!! Your Thunderbolt has the giant kangaroo reeling!"
                                                                                                    
                            "Mom's Kangaskhan is paralyzed!"
                                 
                            a "Finish the job!"
                                 
                            hide raichu
                                 
                            show mom 
                                 
                            m "Not so fast! Kangaskhan, eat this Cheri Berry and use Body Slam!"
                                 
                            "Kangaskhan eats the Cheri Berry and its paralysis is cured!"
                                 
                            "With a roar, mom's kangaroo charges toward your defenseless Pokemon! Your starter dodges the attack but Raichu is injured!"
                                                                                                                                                        
                            a "Oh no... Raichu, return!"
                                                        
                            "..."
                                 
                            show black
                                 
                            e "Hey! You can do it!"
                                                   
                            hide black
                                                   
                            "........"                       
                                                   
                            "You open your eyes to see a certain redhead standing before you!"
                            
                            hide mom
                                                                                              
                            show lovein normal
                            
                            play sound ("by.mp3")
                                                                                              
                            e "Come on, I believe in you!"
                                                          
                            e "I know you and I know that you're stronger than this!"
                                                              
                            e "You can definitely defeat your mom!"                                  
                            
                            "They clasp your hands tightly, lending you their strength."
                                                              
                            a "I-"
                            
                            hide lovein normal
                                                              
                            "Just then, your starter Pokemon leaps up and scratches at Kangaskhan's eyes!"
                            
                            show kang
                                                                             
                            "{i}ROARRRRR{/i}"
                                             
                            "Crying in pain, the Kangaskhan falls over, pawing at its eyes."
                            
                            hide kang
                                                                                            
                            a "Ahh, good job!"
                                              
                            stop sound
                            
                            play sound ("congrat.mp3")
                                              
                            a "..."
                                   
                            "Your Pokemon leaps into your arms."
                                                                
                            "You turn to your mother, then to your friend, and let out a shaky laugh."
                                                                                                      
                            a "...Did we win?"
                            
                            show lovein normal
                            
                            e "YOU DID IT! I'M SO PROUD OF YOU!"
                            
                            a "OH MY GOSH!"
                            
                            "I leap into their arms!"
                            
                            a "I'm so happy right now!"
                            
                            "I laugh hysterically, obviously in disbelief."
                            
                            stop sound
                            
                            play sound ("bensound-romantic.mp3")
                            
                            e "I'm so proud of you!"
                            
                            "..."
                            
                            "They peer into my face, eyes filled with joy and pride."
                            
                            hide lovein normal
                            
                            a "Ahh..."
                            
                            a "Uhm, thank you... I didn't think you'd come back."
                            
                            show lovein normal
                            
                            e "How could I just leave you here?"
                            
                            e "What if you lost? Who's going to be there to comfort you if I'm not around?"
                            
                            a "...Heheh. I guess you're ri-"
                            
                            "..."
                            
                            "!!!"
                            
                            "I freeze as they brought their face next to mine."
                            
                            e "You know, I..."
                            
                            "My eyes widen as they whisper something in my ear."
                            
                            hide lovein normal
                            
                            "..."
                            
                            "My surprise turns into a blush, then into a smile."
                            
                            a "Hey, I know. Me too."
                            
                            "..."
                            
                            "... And this is just the beginning of my journey."
                            
                            return
                            
      
        
        
        
        label choice8:
                
                show forest 
                
                stop sound
                
                play sound ("oko.mp3")
                
                "On my way to Olempec Town, I ran into a giant red and blue blob."
                
                a "AHH! It's you! WHY ARE YOU FOLLOWING ME?!@"
                
                "..."
                
                e "There's no one here..."
                
                "The blob whizzes past and hides behind a tree!"
                
                a "Hey... Who do you think I am? It's not like I don't know how you are."
                
                show lovein normal
                
                stop sound
                
                play sound ("normal.mp3")
                
                e "Yeah, okay, I was following you."
                
                "The redhead grumbles and comes out of hiding."
                
                a "You still salty after that battle?"
                
                e "{i}NO{/i}, obviously not!"
                
                "They so obviously are."
                
                e "Ready for another battle?"
                
                a "Ready to leave me alone?"
                
                e "Now let {i}me{/i} think about it."
                
                e "..........."
                
                e "Nah, I love it when you get ticked off."
                
                a "Alright alright, let's go!"
                
                hide lovein normal
            
                stop sound
                
                play sound ("bensound-epic.mp3")

                menu:
                    
                    "Use your starter!":
                        
                        show drag
                        
                        e "I've gotten used to your pokemon's tricks!"
                        
                        "Their Dragonite used Dragonbreath!"
                        
                        a "Oh no! Watch out!"
                        
                        "Your Pokemon is hit by the Dragonbreath! They flounder and fall into your arms!"
                        
                        a "AHHH! NO!"
                        
                        hide drag
                        
                        show lovein normal
                        
                        e "Try harder next time, and cry harder while you're at it!"
                        
                        a "I'm so tired of this...."
                        
                        e "I could give you some tips on winning if you want?"
                        
                        a "Ugh, I'm out of here!"
                        
                        "You dash out of the forest, cradling your wounded Pokemon in your arms."
                        
                        hide lovein normal
                        
                        hide forest
                        
                        jump choice10
                        
            
                    
                    "Use Raichu":
                        
                        show raichu
                        
                        a "Come on Raichu, let's go! I believe in you!"
                        
                        "Raichu used Discharge!"
                        
                        "{i}RAWRRRR{/i}"
                         
                        "Your rival's Dragonite is hit hard! It becomes paralyzed and falls to the ground!"
                                    
                        a "YES! YOU GO RAICHU!"
                                    
                        hide raichu
                                    
                        stop sound            
                                    
                        show lovein normal  
                                    
                        play sound ("normal.mp3")            
                        
                        e "WHAT?! How'd you get so strong?!@"            
                                    
                        e "That was insane!" 
                        
                        e "I'll report you to the Pokemon League for cheating! How did my Dragonite lose to your Raichu?!"
                        
                        e "Did you give your pokemon steriods or something?"
                        
                        a "We only really need the bare mininum to beat you."
                        
                        e "Haha, you're so funny!"
                        
                        e "...Do you think you could teach me how to battle sometime?"
                                                                                      
                        "You can't help but laugh."
                                 
                        a "You're cute."         
                        
                        a "Maybe later, if I have time!"
                        
                        hide lovein normal
                        
                        hide forest 
                        
                        jump choice10
                        
            
        label choice10:
                
                stop sound
                                                        
                play sound ("happy.mp3")                                        
                
                show mountain
            
                a "Let's see... Which way do I have to go?"
            
                a "I think I have to climb that mountain over there...?"
            
                a "This is gonna be abuse on my legs."
                       
                a "Jeez, I wish I ate before I left."
                       
                "... You breathe in, and start humming to hype yourself up."
            
                "Better get started right now! We can do it!"
                
                "..."
                       
                a "{i}Should really stop talking to myself before people think I'm a weirdo.{/i}"
                       
                stop sound       
                
                hide mountain
                
                show mtown
                
                a "That took way too long to get here."
                                                       
                a "Why is there so much steam floating around?"  
                                                               
                "..."
                     
                "You glance around the town."
                
                a "What is this, some kind of bathhouse town?"                                                                                                    
                
                show lovein normal
                
                play sound ("bensound-buddy.mp3")
                                                
                "..."
                     
                a "Ahh!"
                
                e "You know, it's really weird when you talk to yourself."
                
                e "It almost makes it seem like you have friends!"
                                
                a "{i}Hah! That was so funny!{/i}"
                                
                a "Wait, stop following me!"                
                
                "How did I know they were following me...?"
                                
                "Guess it's just my intuition. Been friends our entire lives, after all."
                
                e "Think that there is a volcano or something underneath the mountain, and that's why there are so many bath houses."
                   
                a "I guess that makes sense..."
                
                e "Hey. You heading to the gym?"
                
                a "Did you think I climbed the mountain to take a bath?"
                
                e "Well no.... Ugh, you're so hard to talk to! See you later, {i}prickly{/i}."
                
                hide lovein normal
                
                a "........ That was weird."
                                            
                a "Ah, well, onwards!"
                
                stop sound
                
                hide city
                
                hide mtown
                
                show peak
                                      
                a "I think we're here!"
                              
                a "Oops, I'm talking to myself again."
                
                a "Okay, I'm going to take this gym down!"
                
                show spork smile 
                
                s "Are you really now?"
                
                "Oh man, this lady heard me babbling."
                
                s "Well you're in for a {i}shock{/i}, kid, because I don't lose easily!"
                                                                         
                a "..."
                                                                         
                a "Your jokes aren't funny."
                                            
                a "WAIT. Wait. You're the gym leader?!"
                                   
                s "Man. Seriously? You came all the way up here not knowing who you were fighting?"
                                   
                a "... Didn't expect you to look like this."
                                                            
                a "Expected some sort of crazy spiky explosion-induced chemist hair."
                                                                                     
                s "..."
                       
                s "Ahem."
                    
                hide spork smile
                       
                show spork angry
                       
                s "You're real funny!"
                       
                s "I'm Electra, the leader of the Olempec Gym! Prepare to get shut {i}down{/i}!"
                  
                "Electra's expression is kind of scaring me... Oh man."
                
                s "Snap out of it! You ready?! Let's fight, RIGHT NOW!"
                                                                       
                "..."
                     
                a "WAIT!"
                         
                a "One sec."
                
                a "Real quick, before we start, why are we fighting so high above the ground?"
                
                s "..."
                
                s "Less talking. More fighting! I felt like building the gym here, okay?!"


        label choice78:
                play sound ("bensound-epic.mp3")
                
                d "Gym Leader Electra sent out Luxray!"
                
                show lux 
                
                hide spork angry
                
                menu:
                    
                    "Send out ya starter pokemon":
                        
                        
                                                 
                        a "HEY, LET'S GO! BEAT UP THAT LUXRAY!"
                                    
                        "Your starter used Tackle! It was weak but the Luxray got hurt by it anyway!"
                        
                        "..."
                                    
                        s "NO! LUXRAY!"
                        
                        s "Come back!"
                        
                        hide lux
                                    
                        "You can't help but to burst out laughing!"
                        
                        a "Awww yeah! That was way too easy!"
                        
                        jump choice0
                        
                    "Send out Raichu":
                        
                        hide lux
                        
                        show raichu
                        
                        a "Why did I choose an Electric type to fight an Electric type again?"
                        
                        "Raichu was struck by Thunder Wave!"
                        
                        a "Ah, shoot! Raichu, be careful!"
                        
                        s "Too late! It's over!"
                        
                        "You scream, running over to your Raichu."
                        
                        hide raichu
                        
                        a "...I'll be back!"
                        
                        s "Grow up, kid!"
                        
                        "Hurriedly, you run to a nearby PokeCenter to heal your wounded Raichu."
                        
                        stop sound
                        
                        "..."
                        
                        a "{i}I should be smarter about this next time.{/i}"
                    
                        jump choice78
                        
        label choice0:
                        
                        hide lux
                        
                        hide spork angry
                        
                        stop sound
                        
                        show spork smile
                        
                        s "Hey, that was kind of impressive."
                        
                        s "You really know your stuff, kid. You put up a lot of {i}resistance{/i}!"
                        
                        a "Thank you for taking the time to fight me!"
                        
                        s "Stay safe! Here's the Olempec Gym Badge!"
                        
                        "..."
                        
                        "You obtained the Gym Badge! Carefully, you put it in a case along with your Lowestof Badge."
                        
                        "You wave to Electra as you head down the precariously slippery mountain."
                        
                        hide spork smile
                        
                        hide peak
                        
                        jump choice11
                    
                    
        label choice11:
                    
                    stop sound
                    
                    show templeroad
                    
                    "..."
                    
                    "{i}HUFF...{/i}"
                    
                    a "Ugh, man! I'm so exhausted!"
                                   
                    a "How am I going to have energy for the gym battle?"
                    
                    "{i}WORRIES...{/i}"
                    
                    a "What if I've come this far, just to fail!"
                    
                    "I will not! mother, I'm going to do this for the two of us!"
                    
                    hide templeroad
                    
                    show shrine 
                    
                    "... Whew..."
                    
                    show lovein normal
                    
                    "What? Uhm..."
                                           
                    "Uhh... Remind me why they're here again?"
                                                              
                    a "Hello, do I know you?!"                                        
                    
                    e "Well, Well, Well!"
                                         
                    e "Did you miss me?"
                    
                    "Your redhead friend peers at you with curiosity."
                    
                    e "Where are ya headed?"
                                            
                    a "Where do you think? I just beat Electra and took a leisurely hike down the mountain."
                                            
                    e "I know you're on your way to a battle. You think I'm an airhead or something?"
                    
                    a "{i}Wouldn't be surprised.{/i}"
                    
                    e "Why not refresh your skills before you take an L?"
                    
                    a "What's an L?"
                    
                    e "...A loss, you dummy."
                    
                    a "Okay sure, Mr.I THINK I Know It All!"
                    
                    e "Fine, let's fight since you came all this way to see me."
                    
                    play sound ("bensound-epic.mp3")
                    
                    "You face off with your rival/childhood companion/best friend!"
                    
                    hide lovein normal
                    
                    show drag
                    
                    e "Go, Dragonite!"
            
                    a "Alright, we can do this!"
                    
                    menu:
                    
                        "Use your starter!":
                            
                            "You send our your starter Pokemon!"
                            
                            a "Let's go! Beat up that fat dragon!"
                            
                            "Your Pokemon leaps towards the Dragonite and scratches its wings!"
                            
                            "{i}ROARRRRRR!{/i}"
                            
                            "The Dragonite is wounded and falls to the ground!"
                            
                            "It's unable to use its wings!"
                            
                            "Your starter Pokemon launches a flurry of attacks, and the Dragonite cries out in pain!"
                            
                            e "That's enough! Come back, Dragonite!"
                            
                            hide drag
                            
                            a "Dude. Know your place!"
                            
                            "..."
                            
                            stop sound
                            
                            show lovein normal
                            
                            e "Okay. Okay, I got it. Good luck on your next gym battle."
                        
                            e "You'll need it. I heard that the gym leader is a samurai!"
                            
                            a "...Wh"
                            
                            a "What? Serious? Samurai still exist in this day and age?!"
                            
                            e "Apparently so!"
                            
                            e "Look, I know I'm aggressive and all towards you."
                            
                            e "But I'm just trying to give you more battle experience!"
                            
                            a "At least you can be more obvious about trying to help me."
                            
                            "They smirk and stick out their tongue at you."
                            
                            a "Moving on. See you later."
                            
                            jump choice14
                        
                        
                            
                        "{i}Raichu{i}":
                            
                            show raichu
                            
                            e "Dude, your Raichu kind of sucks!"
                            
                            a "Ah man, I've been sending our my Raichu the entire day. It's kind of tired."
                            
                            e "Well, your loss."
                            
                            "The Dragonite smacks Raichu with its fat tail and Raichu faints!"
                            
                            hide raichu
                    
                            e "Wow! I thought you were supposed to be getting better!"
                            
                            e "Your Pokemon barely put up a fight."
                                
                            a "Hey, you know what?!"
                            
                            a "I'm determined! My training will pay off eventually!"
                            
                            "You stomp your foot and cross your arms."
                            
                            e "Whatever, just don't make that same mistake."
                             
                            e "Hope you're ready for that samurai!"
                            
                            a "Whatever... See you later, hater."
                            
                            jump choice14
                
                
                
        label choice14:    
                    
                    stop sound
                    
                    hide lovein normal
                    
                    hide shrine
                    
                    show temple 
                    
                    a "Oh man! This is it, no turning back!"
                    
                    "THIS IS FOR YOU, MOM!"
                    
                    "I think to myself, as I continue onward to the temple."
                    
                    hide temple    
               
                    show intemple
                    
                    "Whoa... This place is kind of crazy."
                    
                    play sound ("oko.mp3")
                    
                    b "Who goes there?"
                    
                    "I look around, but I don't see anyone."
                                
                    "{i}BANG!{/i}"   
                    
                    show samurai
                    
                    "A man with a sword suddenly appears in front of me!"
                    
                    "He almost falls over!"
                    
                    t "I'm sorry about that rusty entrance but hi,"
                       
                    t "I'm The Takeo Gym Leader. I was told to expect you from a special someone..."
                    
                    a "Hello, I'm here to battle you, Master Takeo."
                    
                    t "That's what I'm here for lad, step in my arena, get ready to begin!"
                    
                    stop sound
    
        label choice76:
                    
                    play sound ("bensound-epic.mp3")
                    
                    "Gym Leader Takeo sends out Hariyama!"
                    
                    hide samurai
                    
                    show hari
                    
                    menu:
                        "Use your starter!":
                                           
                            a "AHH!!!"
                        
                            a "I LOST!"
                            
                            "You black out."
                            
                            "..."
                            
                            hide hari
                            
                            stop sound
                            
                            jump choice76
                            
                            
                        "{i}Raichu{i}":
                        
                            t "OH MY! I didn't expect that powerful pokemon."
                                             
                            t "How did I let a twerp beat me?! Scram! BEAT IT!"
                            
                            jump choice15
                            
                            hide hari
                        
        label choice15:
                    stop sound
                    
                    hide intemple 
                    
                    hide samurai
                    
                    show city
                    
                    "I want to hurry, how can I make it to home fast enough?"
                    
        label choice001_for:
                    
                    "What do I use?"
                    
                    menu:
                        
                        "Get a car ride from a stranger":
                                             
                            "Uhh... Mom told me not to trust strangers."
                                                 
                            jump choice001_for
                        
                        
                        "Bike":
                            
                            jump choice001_done

                        
        label choice001_done:
                    
                    hide city
                    
                    show road
                    
                    show prof normal
                    
                    play sound ("bensound-funkyelement.mp3")
                    
                    c "So you've made it back in one piece, how are Raichu and your starter holding up?"
                                
                    a "Pretty healthy ma'am. We're on our way to our last gym battle."
                                                
                    a "Any advice you're able to give?"
                    
                    c "Yes, I sure do."
                    
                    c "Don't let those nerves effect your outcome on your next battle. Clear year mind and you won't lose."
                    
                    a "Thank you so much helping me out in the beginning. I have to go visit my Mom. I'll {i}catch{/i} you later."
                    
                    "HAHA! Pokemon puns... I sure am funny."
                    
                    hide road 
                    
                    hide prof normal
                    
                    stop sound
                    
                    show house 
                    
                    "Yes! I've made it!"
                    
                    hide house 
                    
                    show mom 
                    
                    m "Hi Sweety, How was your battling experience with Master Takeo?"
                    
                    m "I told him to expect you, but I have some terrible news and I need your help right away!"
                    
                    a "Of course Mom, what is it?"
                    
                    stop sound
                    
                    play sound ("by.mp3")
                    
                    m "See, I wanted to surprise you and be your last gym leader battle, but this person came and took over my gym!"
                       
                    m "They asked to battle you."
                    
                    a "What?! Take me there, NOW!"
                    
                    "Who would take over an innocent lady's property, just to battle with me?"
                    
                    
                    show mom
                    
                    m "You see, that person right there!"
                    
                    hide mom
                    
                    show lovein normal
                    
                    e "Hello darling, nice to see that she follows directions. What does this battle and this Gym mean to you and your precious mother?! {i}HAHA{/i}!!"
                    
                    a "Honestly, I don't care! You've crossed the line here!"
                    
        label choicefinal:
                    
                    stop sound
                    
                    play sound ("by.mp3")
                    
                    "IT'S THE FINAL BATTLE FOR MY MOM'S GYM!"
                    
                    hide lovein normal
                    
                    show drag
                    
                    "Your rival sends out Dragonite!"
                        
                    menu:
                    
                            "Use your starter!":
                                
                                e "Wow, your starter's gotten really good!"                      
                                                      
                                e "Fair fight."
                                               
                                e "You've really trained too... I'll stop bothering you guys now."
                                
                                hide drag
                            
                                jump choice16
                                
                            "{i}Raichu{i}":
                                
                                e "Dude, your Raichu is nowhere near ready to beat my Dragonite."
                                
                                "You and your Pokemon pass out."
                                
                                "You really messed up this time."
                                
                                "Of course, you still get another chance because this is a game and we can send you back to the part where you messed up."
                                
                                stop sound
                                
                                jump choicefinal
                                
                                
                                
                                
        label choice16:
                    
                    stop sound
                    
                    play sound ("bensound-november.mp3")
                    
                    hide lovein normal
                    
                    show mom 
                    
                    m "Thank you so much sweety, words can't describe how much I love you and appreciate your skills!"
                                                           
                                                           
                    m "I want you to use those skills you learned and take care of our gym. Mom's really getting tired."
                    
                    m " Don't let ANYONE come in between you and your journey. You can become the BEST Gym Leader!"
                    
                    "OBTAINED THE GYM KEY"
                    
                    m "Now I'm going home. How about you go check out your new gym?"
                    
                    a "Okay, thank you Mom."
                    
                    a "I love you so much. See you later!"
                    
                    "You run off excitedly."
                    
                    hide mom normal
                    
                    show colosseum
                    
                    "THIS is mine? THIS is what I've spent my journey to accquire?  ...Did I achieve my goal?"
                    
                    stop sound
                    
                    return
                        
                    
                                    
                       
                        
      

