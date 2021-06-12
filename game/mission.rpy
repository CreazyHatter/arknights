
label Chapter1_1:
    show text "{color=#17293b}{size=+40}Chapter 1{/size} \n\n\n1.1\n{size=+10}Colapso{/size}{/color}" with Pause(3.0)
    scene black with dissolve
    scene zone 1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg abyss 1
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show amiya faded:
        xalign 0.25
        yalign 0.75

    # These display lines of dialogue
    # El díalogo que viene no lo dice Amiya, lo dice la Médico aunque aparece como una "Voz distante", habría que corregirlo. Además recuerda que en estos diálogos Amiya en realidad aparece como "???" y no por su nombre.
    
    amy "...conciencia..."
    amy "Circulación restablecida... constantes estables... solución cardioestimulante inyectada..."
    amy "La temperatura corporal es baja... administrando 20 cc. de hexametasona..."
    amy "¡Coge el hemóstato!"
    amy "Condiciones estables... comenzando la resección... cuidado con la fibrilación ventricular..."
    amy "... Lo siento..."
    amy "... Por hacerte sufrir de nuevo..."
    amy "..."

    hide amiya faded
    #quit amiya intro

    show amiya stand:
        xalign 0.25
        yalign 0.75

    amy "{color=#96989A}Doctor{/color}..."
    amy "Doctor..."
    amy "¡... mano!"
    amy "¡Agarra mi...!"
    amy "¡Agarra mi mano!"
    amy "..."
    amy "Emergencia..."
    amy "... Ayuda..."
    amy "...¡Está hecho!..."
    
    # Elimino el siguiente diálogo porque no pertenece al guión
    
    """
    amy "{color=#96989A}Doctor{/color} despierta .... despierta "

    show litia:
        xalign 0.75
        yalign 0.75

    amy "{color=#0000ffff}huh huh.... Amiya! corres muy rapido! nuestro escuadron no puede seguirte el paso{/color}"
    amy "{color=#0000ffff}Tu.. rompiste el muro...{/color}"
    amy "{color=#0000ffff}Esto es muy peligroso tu de Rhodes la -------{/color}"
    am "No es lo que importa ahora, Medico!"
    am "Ven hechale un vistaso al {color=#96989A}Doctor{/color}!"
    am "No parece estar conciente, pero el recien se agarro de mi"
    #aparence of random pj od rodos
    lil "O..... ok. No seas tan impaciente, yo tambien he estado buscando al {color=#96989A}Doctor{/color} por un largo tiempo"
    lil "Ya seriamente Amiya deberias ser más cuidadosa..."
    am "Estas bien {color=#96989A}Doctor{/color}?"
    lil "emm.... la respiracion es debil, precion arterial normal, ligeros espasmos respiratoriaos, esta bien"
    lil "aah..... Cuidado!"
    """
    # Agrego diálogo que no existía. Los participantes son Amiya y la médico, lleva fondo negro.
    
    am "¡Doctor!¡Doctor!"
    am "Médico, ¿cómo se encuentra?"
    am "Pero... hace un momento... sostenía mi mano..."
    am "Entonces, ¿por qué? ¿Por qué el Doctor no se despierta?"
    
    # A partir de este punto Amiya pasa a llamarse Amiya como tal, ya no ???
    
    lil "¡Amiya! ¡No entres en pánico, primero cálmate!"
    am "Ah... L-Lo siento."
    lil "Siempre te pones muy nerviosa cuando se trata del Doctor"
    lil "Pero, Amiya, si lo peor llegara a pasar... ¿qué harías entonces?"
    am "... Ya estoy mentalmente preparada para ello. Seguiríamos adelante con el plan."
    lil "... Lo comprendo. De todos modos, haré lo que me has pedido."
    am "De acuerdo... te lo agradezco."
    am "Sobre el Doctor..."
    lil "No te preocupes, Amiya. Todos sus signos vitales están estables ahora."
    lil "Haré una inspección más, sólo por ti"
    am "¡Gracias!... ¡Muchas gracias!"
    lil "La respiración es ligeramente superficial, pero la presión sanguínea es normal. No hay motivos para preocuparse."
    
    
    with Dissolve(5.0)

    scene bg indoor 1

    show amiya stand:
        xalign 0.25
        yalign 0.75
    show litia:
        xalign 0.75
        yalign 0.75
    am  "¡...!"
    lil "..."
    lil "¿Estás despierto?"
    lil "¡Amiya, lo hemos conseguido! El Doctor ha despertado."
    am "¿{color=#96989A}Doctor{/color}...?"
    am "Me alegra tanto... Doctor..."
    lil "¡Cuidado! No deberías hacer eso..."
    lil "No intentes moverte. Tu cuerpo todavía no se ha adaptado por completo a esto."
    am "¿Doctor?..."
    doc "¿Quién... eres?"
    am "Ah, {color=#96989A}Doctor{/color}... soy yo..."
    am "..."
    am "Soy yo, Amiya."
    am "Hemos venido a rescatarte."
    doc "¿Quién... soy?"
    #intro de name of the player
    #init var of player
    $ player_name = renpy.input("Introduzca su nombre:")
    $ player_name = player_name.strip()
    if not player_name:
        $player_name = "Yolo"
    am "Tú..."
    am "Tú eres miembro de Rhode Island, igual que nosotras..."
    am "Así como mi compañero."
    am "Dr" #Aquí debes configurar lo que sea para que muestre el nombre del jugador, yo en eso no me meto.
    am "Eres la persona más importante para mí."
    am "Doctor... ¿no lo recuerdas?"
    # También tenemos que discutir qué pasa aquí. En el script aquí se abre una múltiple elección con diferentes respuestas.
    doc "*niega con la cabeza"
    lil "como... esto es verdaderamente....."
    am "esto...."
    am "esta bien, igual esto tambien esta bien"

    hide amiya stand
    hide litia

    show ran pj:
        xalign 0.25
        yalign 0.75

    op "Cuidadio alguien se acerca"

    hide ran pj
    show rn emy:
        xalign 0.75
        yalign 0.75

    ren "------"
    hide rn emy

    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "no teman preparence para el combate"
    am "donde esta el telecomundador de Kalt'sit"
    hide amiya stand
    show ran pj:
        xalign 0.25
        yalign 0.75
    op "ha sido interrumpida hace tiempo, el dispositivo de comunicacion dejo de funcionar"
    op "Amiya a donde vamos ahora"
    hide ran pj
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "fue cortado por alguien"
    am "entonces Kalt'sit no puede darnos apoyo"
    hide amiya stand
    show ran pj:
        xalign 0.25
        yalign 0.75
    op "Entonces Amiya tu sola podras!..."
    hide ran pj
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "-----"
    am "No. yo---- puedo pelear"
    am "------ yo quisiera q Doc. [player_name] tome le cotrol"
    am "Doc. [player_name]"
    am "Aunque haya perdido la memoria... sige siendo .... pelée junto a nosotros Doc [player_name]"
    am "Nosotros hemos pasado por mucho juntos"
    am "Tu puedes llevarnos a la victoria"
    with Dissolve(3.0)
    #change bg
    scene bg wild a
    amy "Tu puedes llevarnos a la victoria"
    #return bg
    with Dissolve(3.0)
    scene bg indoor 1
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Se que es maleducado de mi parte preguntarte tan pronto"
    am "pero.... pudieras ayudarnos"
    am "Agradecida de ayudarte"
    am "-----"
    am "Yo creo en ti!"
    am "yo creo que puedes hacerlo"
    am "{color=#96989A}Doctor{/color} estoy tranfiriendote el cotrol"
    doc "una pregunta"
    am "Claro {color=#96989A}Doctor{/color}, siges sin poder recordar quien eres?..."
    am "Doc [player_name] desde el dia de hoy eres uno de nosotros"
    am "Por favor recuerdanos por nuestros nombre"
    am "Isla Rhodes"
    with Dissolve(10.0)

label Chapter1_2:
    show text "{color=#17293b}{size=+40}Chapter 1{/size} \n\n\n1.2\n{size=+10}Protección{/size}{/color}" with Pause(3.0)
    scene black with dissolve
    scene zone 1
    scene bg city a
    show npc stand:
        xalign 0.25
        yalign 0.75
    npc "NO! NO!!"
    npc "Ayuda NO!! NO!!!"
    npc "Porque, porque yo"
    npc "Ahhhhhh!!!"
    hide npc stand
    show litia:
        xalign 0.75
        yalign 0.75
    lil "Como es esto posible"
    lil "Todo estaba tranquilo cuando nos infiltramos"
    show doberm st izq:
        xalign 0.25
        yalign 0.75
    dob "Estuviste en el centro de todo asi que no sabes la situacion actual de Chernobog "
    with Dissolve(2.0)
    scene bg tv1
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "De hecho .... la ciudad entera es un caos.."
    dob "La policia y la milicia estan siendo destruida"
    dob "Lo que indica q la situacion de la comando de Chernobog esta paralizada a culpa de Reunion"
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Eso quiere decir que Reunion ha puesto su mira en el Gobierno de Chernobog desde el principio"
    dob "Si y tambien ...."
    dob "Fue demaciado facil colarnos en la ciudad sin ver a un simple guardia de seguridad"
    dob "Al menos eso creemos ----"
    dob "Ya Reunion tomo control de la ciudad desde que entramos"
    dob "Solo que decidieron darse cuenta ahora que estamos aqui"
    dob "Pesabamos que Reunion era solo un movimiento protestante que causan problemas"
    dob "Por ahora solo estoy agradecida que no soy yo quien tine que lidiar con este desastre"
    hide amiya stand
    show litia:
        xalign 0.25
        yalign 0.75
    lil "¿Pero que es lo que Reunion quiere? Porque"
    hide litia
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Este no es el momento para ese analisis"
    am "Lo que no preocupa ahora es salir del centro de todo esto... Cuanto antes mejor "
    am "Solo hasta que aseguremos al Doc. [player_name]"
    dob "Esta bien"
    dob "Por otro lado-----"
    dob "Enemy atack!!!"
    dob "Todos pocicion de Combate ahora!!"
    dob "Ha... he escuchado muchas veces tu nombre Doc. [player_name] por parte de Kal'tist"
    am "No seas tan duro con Doc. [player_name]"
    dob "Incluso si dices eso..."
    dob "La situacion no nos permite contenernos"
    dob "Vamos Doc. [player_name] es tiempo que pruebes tu valia "
    with Dissolve(5.0)
    scene bg city a
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "Bien suficiente!"
    dob "Rhodes necesita un cerebro como el tullo, no podemos dejar que Kal'tsit se sobrecarge"
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Doberman"
    dob "Ahora no, no podemos relajarnos todavia"
    dob "Muevan sus traceros!! Rapido"
    show bg city b
    am "hah,hah...."
    hide doberm stand
    show doc der:
        xalign 0.75
        yalign 0.75
    doc "Me disculpo Amiya"
    am "Ah, no, no, Doctor, soy yo la q necesita disculparse...."
    am "Tu no sabias nada y aun asi yo te arrastre a esta pelea...."
    am "Inclusive yo fui quien puso todo el peloton en peligro...."
    am "Soy una ......"
    am "Doctor.... huh? estas bien? lo hice muy bien"
    hide doc der
    show litia:
        xalign 0.75
        yalign 0.75
    lil "Tu dijiste durante la reunion de planificacion sobre el rescate del Doc. show [player_name] que la micion era arriesgada y peligrosa en si"
    lil "Pero era un importante compañero, que no podiamos rendirnos. Verdad?"
    hide litia
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "Yo me uni a esta operacion porque ya de por si aprove el plan"
    dob "Amiya. Mantente fuerte la seguridad de las fuerzas de Rhodes estan en tus manos"
    am "SI!"
    am "La nearl esta asegurando la retirada en el el centro del pueblo"
    am "Vamos con a ellos, no los hagamos esperar tanto!!"
    with Dissolve(10.0)

label Chapter1_3:
    show text "{color=#17293b}{size=+40}Chapter 1{/size} \n\n\n1.3\n{size=+10}Colapso{/size}{/color}" with Pause(3.0)
    scene black with dissolve
    scene zone 1
    scene bg city b

    show litia:
        xalign 0.75
        yalign 0.75

    lil "Que es eso allá en la distancia"
    show amiya stand:
        xalign 0.25
        yalign 0.75

    am ".... es el escuadron de Ace"
    hide litia
    show ran pj1:
        xalign 0.60
        yalign 0.75
    op "Jefe porque esta aqui?"

    show ace:
        xalign 0.90
        yalign 0.75

    op "Jefe porque esta aqui?"
    op1 "Tenia miedo que se toparan con miembros de Reunion, asi que vine a ayudar"
    hide amiya stand
    hide ran pj1

    show ace:
        xalign 0.90
        linear 0.3 xpos 0.75

    show doberm st izq:
        xalign 0.25
        yalign 0.75
    dob "Estas aqui?"
    op1 "Dobermann"
    dob "Por alla esta bien Nearl"
    op1 "Todavia nada que le cueste trabajo"
    op1 "Ademas, es una corasonada, pero estan en problemas?"
    dob "Si, Reunion lanzo un repentino ataque"
    dob "Lo mismo para nosotros, gracias a los comandos de Nearl, nos ahorro mucho trabajo"

    show ace:
        xalign 0.75
        linear 0.3 xpos 0.90

    show ran pj1:
        xalign 0.60
        yalign 0.75

    op "Bien.... ughh..."
    hide doberm st izq
    show litia:
        xalign 0.25
        yalign 0.75
    lil "Estas herido?, dejame curarte..."
    op "Disculpa"
    op "Todos los infectados de la zona en Chernobog, lo llaman algo como.... Azazel"
    op "Si ellos estuvieran de acuerdo en compartir informacion o cooperar"
    op "A lo mejor no estuvieramos tan a la defensiva"
    hide litia
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "No es asi"
    op "Amiya, tu estuviste en las negociaciones tambien"
    op "Esa arrogante y fria personalidad de ellos, solo estoy...."
    op "Tan cabreados con ellos"
    op1 "No podemos culparlos"
    op "Jefe tambien lo piensas"
    with Dissolve(5.0)
    scene bg chi
    show ace :
        xalign 0.75
        yalign 0.75
    op1 "Los infectados no son de confiar"
    op1 "Despues de tanto sufrimiento... claro que se volverian recelosos y cautelosos"
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Claro si no estan en cautela es muy probable que pueden resultar dañados"
    am "Incluso los infectados no pueden confiar entre si"
    am "En estas tierras ya sea en calidos grupos o en solitario... de igual manera es dificil vivir"
    am "Al menos sus acciones... puedo entenderlas y perdonarlas tambien"
    hide ace
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "infectados que no son como Rhodes o del extremadamente xenofobico Reunion son dificiles de ver"
    op "Istructor Dobermann"
    dob "Entiendo tu enfado y tu irritabilidad hacia los clinicos"
    dob "Naide se escapa de esta citacion, ellos tienen sus dificultades tambien"
    dob "Pero antes de solucionar los problemas de otros....."
    dob "Primero tenemos que solicionar los nuestros "
    dob "------"
    dob "Las siete en punto, las patrllas de Reunion, Muevanse!!"
    op1 "Enemigos!!! EN GUARDIA!"
    with Dissolve(5.0)
    scene bg city b
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "Enemigos eliminados"
    show amiya stand:
        xalign 0.25
        yalign 0.75
    dob "Solo mantenganlos en la oscridad, deberiamos poder salir seguros"
    am "Entendido"
    show amiya stand:
        xalign 0.25
        linear 0.3 xpos 0.10
    show litia:
        xalign 0.35
        yalign 0.75
    lil "Se abrio tu herida?"
    op "Ahora esta bien, gracias a ti"
    lil "No es nada.Huh? Los heridos de por alla... hey, esperen"
    hide litia
    show amiya stand:
        xalign 0.10
        linear 0.3 xpos 0.25
    op "Valla angel"
    am "Cada vez que la veo sudando. Siento que...."
    op "Si yo tambien lo siento, todavia no es tiempo de tomarselo con calma"
    am "Si stodavia estamos luchando por nosotros mismos"
    op "Antes estabas en lo correcto. Personas como nosotros somos la minoria"
    op "La mayor parte de nosotros los infectados son odiados por todos"
    op "Asi que deberiamos tener la misma actitud hacia ellos, o almenos asi era yo"
    op "Solo hasta que me uni a Rhodes me di cuenta que hay niños como ella"
    op "Ella es una persona normal... pero olvida si son infectados o no, ella esta en el campo de batalla junto a nosotros"
    am "Todos en Rhodes son buenas personas"
    am "Puede que muchas personas forman brechas entre ellos con miedo y hostilidad"
    am "Pero en Rhodes. Yo creo todos pueden descansar tranquilos y reolver sus malentendidos"
    op "estas en lo correcto Amiya"
    op "Heh...."
    am "Cuidado dejame ayudarte"
    op "No la necesito"
    op "Ah, Dr [player_name]"
    op "---- Gracias"
    op "Gracias a ti, pudimos escapar"
    op "Yo creo que tu y Amiya.... creen en todos en Rhodes"
    am "Yo creo en ti igualmente, es un hecho que sobrepasaremos esto"
    with Dissolve(10.0)

label Chapter1_4:
    show text "{color=#17293b}{size=+40}Chapter 1{/size} \n\n\n1.4\n{size=+10}Colapso{/size}{/color}" with Pause(3.0)
    scene black with dissolve
    scene zone 1
    scene bg city b
    show amiya stand:
        xalign 0.25
        yalign 0.75
    am "Esto no esta bien"
    show doberm stand:
        xalign 0.75
        yalign 0.75
    dob "Que pasa"
    
