# If adding anymore easter egg name checks in the future, make sure to keep the name UNCAPITALIZED as the purpose of lower() is to make it non-capital and generalize it
# so that no matter the capitalization of the entered name, the player will always get the easter egg event (Unless they spelt it wrong, then they get NOTHING)


label NamePrompt:
    python:
        MC_Name = renpy.input("What is your name?", length=25)

        if not MC_Name:
            MC_Name = "Riley"

    if MC_Name.lower() == "test":
        jump TestPlayground

    if MC_Name.lower() == "jester":
        Jester "A bit unoriginal, aren't you?"
        jump NamePrompt

    if MC_Name.lower() == "liam":
        L "Hey! That's my name!"
        jump NamePrompt

    if MC_Name.lower() == "gaster":
        $ renpy.quit()
    
    #if MC_Name.lower() == "monroe":
        Acrobat "I'm flattered you want to use my name, but surely you can think of something else, little one?"
        jump NamePrompt

    if MC_Name.lower() == "max johnson":
        Max "I'm Max Johnson!"
        jump NamePrompt

    #if MC_Name.lower() == "gaster":
        $ renpy.quit()

    #if MC_Name.lower() == "gaster":
        $ renpy.quit()
    
    python:
        Dog_Name = renpy.input("What would you like to name your dog?", length=25)

        if not Dog_Name:
            Dog_Name = "Coco"

    

    jump ScriptContinue