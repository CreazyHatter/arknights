# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define amy = Character("??????")
define am = Character("Amiya")
define lil = Character("Operador Medico", color="#0000ffff", what_color="#0000ffff")
define doc = Character("Doctor", color="#96989A", what_color="#96989A" )
define op = Character("Operador de Rhodes")
define ren = Character("Miembro de Reunion")
define pln = Character("[player_name]")
define npc = Character("Ciudadano")
define dob = Character("Doberman")
define op1 = Character("Elite operador de Rhodes")

# The game starts here.
default player_name = "YOLO"
label start:
    jump Chapter1_1
    jump Chapter1_2
    jump Chapter1_3


        # This ends the game.

    return
