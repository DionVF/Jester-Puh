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
            Player_Internal ""

        "Draw":
            Player "Uh"

        "Watch a show":
            Player "Um"

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

    Jester "{b}{i}Excuse me?{/i}{/b}"

    Player_Internal "A woman's voice calls to you from across the counter, you jump slightly in surprise."

    Player_Internal "The source of your scare chuckles, leading you to look over."

    # Once complete, add an Internal Dialogue describing the Jester's design.

    Player_Internal "She waves your attention back to her."

    Jester "You scare too easily."

    Player_Internal "Your eyebrow raises at her statement. What did she expect? Despite the bells, she's as quiet as a mouse."

    Player_Internal "Or a butterfly, to be more accurate."

    Jester "Just these."

    Player_Internal "Your eyes drop down to the items she places on the desk. Just a couple snacks and drinks. Huh."

    Player_Internal "For a performer you'd expect her to choose snacks less… sugary…"

    Player_Internal "You're not one to judge though, eating a few sweets surely wouldn't inhibit her ability to put on a good show."

    menu: # Finish this menu!!
        "What should I do?" 

        "Mention it.":
            Player "Is it a good idea to eat all of this stuff before a show?"

        "Stay silent.":
            Player_Internal "You don't say a word."

        "Compliment her.":
            Player "Fuh me."

    Player_Internal "Silence settles for a few seconds as you finish scanning the last item. Then, just as the scanner beeps for the final time-{nw}"

    Jester "{cps=90}You wouldn't mind if I placed one of our posters in the window, would you?"

    Player_Internal "It isn't really your place to say no."

    Player_Internal "Honestly, someone could walk in with a whole cardboard cut out, place it in the middle of the store and you'd probably just shrug it off."

    Player_Internal "Over your time working here the window to the left of the door had become a mural for upcoming artists, performers and others of the sort to tape their posters and pages to."

    Player_Internal "You watch as the odd jester places a colourful poster on the store's window. Straight away, you recognize the poster as the very same one Liam sent to you."

    Player "You're with the group that's been putting up all those posters for the show, right?"

    Jester "How long did it take you to figure that one out?"

    Player_Internal "You let out a huff at the jester's comment. After a long shift the last thing you need is a jester mocking you."

    Jester "but yeah, we got here yesterday."

    Player_Internal "The jester finishes placing the poster on the window. She walks back to the counter."

    Player "Isn't it a bit late for you to be promoting? It's like 8."

    Jester "What's the harm in putting up some posters at this hour?"

    Jester "It's not illegal, is it?"

    Player_Internal "If you didn't know any better, you'd think she sounded sincere."

    Player "No, not the last time I checked."

    Jester "Then it looks like we've come to an understanding."



