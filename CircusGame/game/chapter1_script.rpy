label chapter1:

    scene bg black # Silly Time, just an example commit!

    Player_Internal "You slide your phone back into your pocket and finish up your walk, ticking off any errands you had to do along the way."

    scene bg living room
    with fade

    Player_Internal "By the time you make it home, two hours have already passed. Only a few more hours until your dreaded shift begins."

    menu: # Finish this menu!!
        "What should I do?" 

        "Read":
            Player_Internal "You glance over at your shelf."
            Player_Internal "It's been a good while since you've touched any of your books. Most of them now caked in a thick layer of dust."
            Player_Internal "You pick up your newest addition, flipping open to the bookmarked page as you pop a squat down on your swivel chair."
            Player_Internal "It isn't hard to get comfortable when you're sitting back in this thing. It's like being cradled by a cloud."
            Player_Internal "You let out a sigh and sink into the soft cushions, beginning the next chapter."
            Player_Internal "You read a few pages before your eyes begin to feel heavy."
            scene bg black with fade
            Player_Internal "Tiredness gets the best of you. Your eyes close, and you fall asleep."



        "Play games":
            Player_Internal "What's a better way to spend your time then hopping on your favourite game?"
            Player_Internal "It's been a while since you've played any game really, life's really been kicking you in the ass."
            Player_Internal "You sit down in your chair and turn on the game, watching the loading bar gradually fill the bottom until it reaches the end."
            Player_Internal "You lose track of time, an hour feeling like ten minutes as you continue to play."
            Player_Internal "When your eyes begin to sting, you think it's from staring at the game for too long and pouring your focus into it, but tearing your eyes away from the screen offers no relief."



        "Draw":
            Player_Internal "Glancing over at your sketchpad, you realise that you haven't really drawn much at all. The last few weeks of your life have been so filled with things to do that you forgot about it entirely."
            Player_Internal "It takes you a few minutes to find your pencils and you scoop up your sketchbook on the way to your swivel chair tucked into the corner of the living room."
            Player_Internal "You flip the pages, catching brief flashes of old doodles and drawings that have been gradually filling the book."
            Player_Internal "A clean page soon presents itself and you get to work filling it with little drawings and sketches."
            Player_Internal "Not long after when the page is half filled, you feel your eyelids grow heavy. With each minute it gets harder for you to stay awake."
            Player_Internal "It's a losing battle as you fight to stay awake, your sketchbook slipping from your hands as it topples down onto the floor."
            Player_Internal "Black is the only thing you can see, and you let yourself lose the battle against your fatigue and you decide that maybe it is best to take a small nap."



        "Watch a show":
            Player_Internal "Searching for the remote took longer than you would've liked, and you have a sneaky suspicion on why that is."
            Player_Internal "You soon find it piled with a few other toys, thanking the heavens that this time [Dog_Name] hadn't chewed it to shreds."
            Player_Internal "It isn't before long you decide on a suitable candidate and let your mind focus on the show, refusing to think about work or anything that'll stress you out."
            Player_Internal "The continuous sound of the show drifts into the background as you feel your mind begin to relax a little more than expected."
            Player_Internal "Your eyes begin to flutter, and soon, sleep overcomes you. There's no harm in a small nap before work."
            Player_Internal "Darkness invades your vision as time slips by while the show drones on in the background."

        "Tidy the apartment":
            Player "Hm"

    scene bg living room with fade

    Player_Internal "For the second time today the sun is determined to disturb your sleep and force you awake."

    Player_Internal "You begin to panic, thinking you've slept past the time of your shift, but taking one glance at the clock reveals you still have an hour remaining until your shift."

    scene bg black
    with fade

    Player_Internal "You leave the house, and head to the convenience store to begin your long, long shift."

    scene bg store interior # Transition to Store Interior, behind counter.

    Player_Internal "Your feet drag across the floor as you step through the doors of the convenience store and join Liam behind the counter."

    L "You look down in the dumps today, who put a bee in your bonnet?" # PLEASE FUCKING CHANGE FOR RELEASE (Keep for Leon Version though)

    Player "Thanks for noticing..."

    Player "and pointing it out."

    L "Anytime."

    Player_Internal "Time passes and nothing stands out to you. It is considerably more busy than usual but nothing you and Liam can't handle."

    Player_Internal "Liam and you exchange some small talk to numb the boredom of waiting for customers."

    Player_Internal "It isn't until it hits 8PM that {i}something{/i} catches your eye." 

    Player_Internal "Liam has gone into the back for whatever reason."
    
    Player_Internal "He didn't care to say and you didn't care to ask."

    Player_Internal "The all-too-familiar bell rings once more and you glance up, attempting to get a look at the next customer."

    Player_Internal "But they're already rounding into an aisle before you can get a proper look."

    Player_Internal "The most you get is a glimpse of bright colour and a small jingle from bells that definitely aren't connected to the door."

    Player_Internal "Your eyes casually glance around, trying to get another peak at the stranger."

    Unknown "{b}{i}Excuse me?{/i}{/b}"

    Player_Internal "A woman's voice calls to you from across the counter, you jump slightly in surprise."

    Player_Internal "The source of your scare chuckles, leading you to look over."

    # Once design is finalized, add an Internal Dialogue describing the Jester's design.

    Player_Internal "She waves your attention back to her."

    Unknown "You scare too easily."

    Player_Internal "Your eyebrow raises at her statement. What did she expect? Despite the bells, she's as quiet as a mouse."

    Player_Internal "Or a butterfly, to be more accurate."

    Unknown "Just these."

    Player_Internal "Your eyes drop down to the items she places on the desk. Just a couple snacks and drinks. Huh."

    Player_Internal "For a performer you'd expect her to choose snacks less… sugary…"

    Player_Internal "You're not one to judge though, eating a few sweets surely wouldn't inhibit her ability to put on a good show."

    Player_Internal "The rain outside picks up, hammering against the store windows."

    Player_Internal "That's when you take notice of the way her hair is askew, droplets still clinging to the strands."

    Player_Internal "Several strands are out of place. You ask yourself if it's wise to tell her."

    menu: # Finish this menu!!
        "What should I do?" 

        "Mention it.": # Neutral-Positive option.
            Player "I think your hair got messed up by the rain."
            Unknown "Oh..."
            Unknown "thanks."
            Player_Internal "The Jester runs her hand through her hair, straightening the wild hairs."
            $ JesterAffection + 1
            # Increase Terah Affection by 1 point.
            

        "Stay silent.": # Neutral option.
            Player_Internal "You don't say a word."

        "Compliment her.": # Positive option.
            Player "Fuh me."

    Player_Internal "You continue to scan and bag the last of the jester's items."

    Player_Internal "Silence settles for a few seconds as you grab the final item. Then, just as the scanner beeps-{nw}"

    Unknown "{cps=90}You wouldn't mind if I placed one of our posters in the window, would you?"

    Player_Internal "A strange thing to suddenly ask but not the worst thing you've heard."

    Player_Internal "It isn't really your place to say no."

    Player_Internal "Honestly, someone could walk in with a whole cardboard cut out, place it in the middle of the store and you'd probably just shrug it off."

    Player_Internal "Over your time working here the window to the left of the door had become a mural for upcoming artists, performers and others of the sort to tape their posters and pages to."

    Player_Internal "You watch as the odd jester places a colourful poster on the store's window. Straight away, you recognize the poster as the very same one Liam sent to you."

    Player "You're with the group that's been putting up all those posters for the show, right?"

    Unknown "How long did it take you to figure that one out?"

    Player_Internal "You let out a huff at the jester's comment. After a long shift the last thing you need is a jester mocking you."

    Unknown "but yeah, we got here yesterday."

    Player_Internal "The jester finishes placing the poster on the window. She walks back to the counter."

    Player "Isn't it a bit late for you to be promoting? It's like 8."

    Unknown "What's the harm in putting up some posters at this hour?"

    Unknown "It's not illegal, is it?"

    Player_Internal "If you didn't know any better, you'd think she sounded sincere."

    Player "No, not the last time I checked."

    Unknown "Then it looks like we've come to an understanding."

    Unknown "Soooo..."

    Unknown "Ever think of coming to the circus?"

    menu:
        "What should I say?"

        "Looks interesting.": # Neutral option
            Player " Im, gonjna kill myself"

        "Hasn't crossed my mind.": # Negative option
            Player "Genji"

        "If you're there.": # Positive option
            Player_Internal "Loser."



