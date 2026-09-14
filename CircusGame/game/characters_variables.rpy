# Characters must use 'define' while variables must use 'default'
# This script should hold all of the game's variables and characters so
# that they are out of the way and easily accessible from anywhere in the project.

define config.default_textshader = 'typewriter'


define Guppy = Character("Gup", color="#13e200", what_font="Bebas.ttf", font="Bebas.ttf")
define Max = Character("Max Johnson", color="#CCCCFF", what_font="Bebas.ttf", font="Bebas.ttf")


define Player_Internal = Character("[MC_Name]", what_color="#8f8f8f", color="#ccede8", what_font="Lora.ttf", font="Lora.ttf")
define Player = Character("[MC_Name]", color="#ccede8", what_font="Lora.ttf", font="Lora.ttf")
define L = Character("Liam", color="#573b31")

define Jester = Character("Jester", color="#e05441", what_font="PTSerifCaption.ttf", font="Quintessential.ttf", what_slow_cps=35)
define Acrobat = Character("Acrobat", color="#6400a7", what_font="PTSerifCaption.ttf", font="Quintessential.ttf")
define Ringmaster = Character("Ringmaster", color="#862514", what_font="PTSerifCaption.ttf", font="Quintessential.ttf")
define Mime = Character("Mime", color="#666666", what_font="PTSerifCaption.ttf", font="Quintessential.ttf", what_size=15)
define Equil = Character("Equil", color="#55aa06", what_font="PTSerifCaption.ttf", font="Quintessential.ttf")
define Contort = Character("Contort", color="#bbb9b8", what_font="PTSerifCaption.ttf", font="Quintessential.ttf")
define Strongman = Character("Strongman", color="#dab53c", what_font="PTSerifCaption.ttf", font="Quintessential.ttf")
define Unknown = Character("???", color="#f1e9e8", what_font="PTSerifCaption.ttf", font="Quintessential.ttf", what_slow_cps=35)



default Micheal = True
default Love = 0
default CurrentSpeaker = "Nobody"

default JesterAffection = 0
default AcrobatAffection = 0
default RingmasterAffection = 0
default MimeAffection = 0
default EquilAffection = 0
default ContortAffection = 0
default StrongmanAffection = 0

transform FocusSpeaker:
    matrixcolor BrightnessMatrix(0.0)
    
transform DimSpeaker:
    matrixcolor BrightnessMatrix(-0.4)
    
