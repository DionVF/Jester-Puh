label start:     

    #show text "{color=#000}Sauce Time Studios Presents...{/color}"  with dissolve

    #$ renpy.pause(1.0)

    #hide text with dissolve

    #$ renpy.pause(2.0)

    #show text "A Date with {color=#f00}Terah{/color}." with dissolve

    #$ renpy.pause(2.0)

    #hide text with dissolve

    #$ renpy.pause(3.0)

    scene bg black

    jump NamePrompt # Jumps to the NamePrompt.rpy script. Handles the settings of the Player's Name and runs easter egg checks
    # before jumping back to ScriptContinue (Label just under this comment)

label ScriptContinue:

    scene bg bedroom
    with fade

    Player_Internal "You're blinded by the sun shining in your eyes as it decided it was your time to be thrust into the spotlight."

    Player_Internal "The cars outside your apartment revved their engines which finally brought you to open your eyes."

    Player_Internal "You reluctantly greet the blinding light, the bright glow seeming to hold a grudge against you as not even turning to lay on your side offered much relief."

    Player_Internal "Tossing the blanket off yourself, you sluggishly move each of your limbs with great effort until you manage to perch on the edge of the bed."

    Player_Internal "Somehow the sun feels even brighter today, but that could also be because you've woken up much earlier than you would've liked."

    Player_Internal "Regardless, there's no going back to sleep now as much as you'd love to."

    scene bg black

    Player_Internal "The creak of the floors echo beneath your feet as you make your way into the kitchen to grab a drink."

    scene bg kitchen
    with fade

    Player_Internal "You still had some time to kill before work so you decided to fit a few things in beforehand. Maybe you'll finally be able to finish that one project that's been brewing in your mind for the last week."

    Player_Internal "You check your email, still no response from jobs you've applied to but that's no surprise."

    scene bg black

    Player_Internal "Instead of being productive, you decide to go on a walk. It usually helps to clear your mind and get you relaxed enough so you can spare some extra patience with the more… difficult customers."

    scene bg outside street
    with fade

    Player_Internal "Many more people are walking the streets. Or at least more than you're used to. Is there a massive event going on and nobody told you? You doubt it since Liam would've talked your ear off about whatever it was."

    Player_Internal "Just as the thought crosses your mind, your phone vibrates in your pocket. Speak of the devil."

    scene bg phone liam # Transition to Phone Ringing BG
    with dissolve

    Player_Internal "Think..? Of the devil?"

    Player_Internal "Whatever."

    L "Hello? Shit, didn't expect you to be up this early."

    Player "'Morning to you too, and trust me it wasn't by choice."

    L "Have you seen the posters around recently?"

    Player "Uhm… no?"

    L "Haven't you looked outside?"

    Player "I {b}am{/b} outside, I haven't seen a thing."

    L "Then just look around! They're everywhere!"

    # Transition to other side of road BG

    Player_Internal "You do just that and glance across the street to the row of stores, but there isn't a poster in sight."

    Player "What posters are you talking about?"

    L "Just hold on, I'll send you a picture then if you're really that blind."

    Player_Internal "A few seconds later your phone dings with a new message from Liam."

    scene bg phone basic
    with dissolve

    Player "A circus?"

    L "Yeah! Apparently they're gonna be performing for the next week or so."

    # Transition back to Liam Phone Call BG

    L "Our breaks will probably be cut short, the streets are already filled with three times the amount of people."

    Player "That's your problem, I'll gladly let you deal with the customers while I lounge in the back."

    L "I'll make sure your shift is torture if you even dare."

    Player "Fine, but you'll be the one to handle the rude ones."

    L "What? Wake up on the wrong side of the bed this morning?"

    Player "Yes, actually, the side that had the sun burning my face."

    L "You have curtains don't you?"

    Player "Yeah? So what?"

    L "Maybe think about closing them."

    Player_Internal "You can hear a brief laugh come from the other side of the phone before you hang up, an amused huff leaving you."

    scene outside street # Transition back to Walking Down Sidewalk BG

    jump chapter1
