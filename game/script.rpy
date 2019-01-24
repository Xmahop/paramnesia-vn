# Вы можете расположить сценарий своей игры в этом файле.
image tanya:
    "Sprites/Prologue/Tanya/Tanya_1.1.png"
    xzoom 0.7
    yzoom 0.7
image oleg:
    "Sprites/Prologue/Oleg/Oleg_1.1.png"
    xzoom 0.7
    yzoom 0.7

image tanya_angry_open:
    xzoom 0.7
    yzoom 0.7
    "Sprites/Prologue/Tanya/Tanya_2.3.png"
    pause 3.0
    "Sprites/Prologue/Tanya/Tanya_2.2.png"
    pause 3.0
    "Sprites/Prologue/Tanya/Tanya_1.2.png" with dissolve

# Определение персонажей игры.
define tanya = Character('Таня', color="#c8ffc8",who_xpos = -10, who_ypos = -40)
define gg = Character('...', color="#ffffff",who_xpos = -10, who_ypos = -40)
define oleg_young = Character("Олег", color="#ff0000", who_xpos = -10, who_ypos = -40)


image bg = "bg1.png"
image bg2_prologue = "Backgrouds/prologue/bg2_prologue.png"
image bg3_prologue = "Backgrouds/prologue/bg3_prologue.png"

$ rep = 0
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
label splashscreen:
    scene black with dissolve
    pause 1 
    show text "Ваш текст" with dissolve
    pause 2
    show text "Ваш текст"
    pause 2
    scene black with dissolve
    pause 1
    return
# Игра начинается здесь:
label start:
    gg "Долго нам еще идти?"
    oleg_young "Подождите"
    oleg_young "О, нашел, пошлите быстрее!"
    scene bg2_prologue with dissolve
    $ rep =+ 1
    gg "Да иду я, иду"
    tanya "Куда вы так бежите, мне за вами не угнаться"
    $persistent.unlock_1 = True
    show oleg at hflip, almostleft with dissolve
    oleg_young "Тань, послушай, без тебя там никак"

    show tanya_angry_open at almostright with dissolve
    tanya "Если опять твои шуточки, я тебе тресну"
    show tanya at almostright with dissolve
    oleg_young "Нет, что ты"

    scene bg3_prologue with dissolve

    oleg_young "Вот теперь аккуратно"
    gg "И что я не видел здесь? Ради чего мы тащились, просто посмотреть на твой штаб?"
    oleg_young "Тихо, дурак. Смотри"
    return
