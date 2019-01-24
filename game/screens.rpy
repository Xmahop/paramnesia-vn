# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
##############################################################################

# Zishy notes: I only changed the main menu, preference, save/load, quickmenu and the yes/no prompt. That is all I customized in this tutorial.
# The NVL is pretty easy to customize so I leave that to you :3
# Every GUI here has their own psd file in the folders, be sure to check them!
# Oh but I didn't include the psd file for the textbox, namebox and quickmenu! Sorry OvO);
# Anyway, I hope this codes will help even a little.

##############################################################################
##############################################################################

# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5


        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:
                    if chosen:
                        button:
                            action action
                            style "menu_choice_chosen_button"

                            text caption style "menu_choice_chosen"
                    else:
                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                else:
                    text caption style "menu_caption"



init python:
    #### Выбор вариантов
    style.menu_choice_button.background = Frame("choice_chosen.png",44,44)
    style.menu_choice_button.hover_background = Frame("hchoice.png",44,44)
    style.menu_choice_chosen_button.background = Frame("choice.png",44,44)
    style.menu_choice_chosen_button.hover_background = Frame("hchosen.png",44,44)

    ####  Выбор шрифта в вариантах
    style.menu_choice.color = "#1a0d00"
    style.menu_choice_chosen.color = "#006666"
    style.menu_choice.size = 33



init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.44)
        xmaximum int(config.screen_width * 0.77)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu
    # The background of the main menu.
    window:
        style "mm_root"

    imagemap:
        add SnowBlossom("snow.png", count=10000, xspeed=(20, 50), yspeed=(999,100))
        add SnowBlossom("snow.png", count=10000, xspeed=(20, 50), yspeed=(99,100))

        idle "gui/mm_idle.png"
        hover "gui/mm_hover.png"
        hotspot (718, 684, 507, 90) action Start()
        hotspot (740, 764, 493, 87) action ShowMenu("load")
        hotspot (741, 843, 440, 80) action ShowMenu("preferences")
        hotspot (675, 916, 577, 75) action ShowMenu("extras")
        hotspot (911, 474, 182, 104) action Quit(confirm=False)

        ### How to get the 4 dimensions? (1) Open the Main Menu.psd in the folders, (2) Right Click CROP and Click SLICE TOOL, (3) then Right click the area where the button is placed/sliced and hit EDIT SLICE OPTIONS
        ### Same thing with the other psd files and menus.

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Слот для сохранения"), FileSaveName(number))
    add FileScreenshot(number) xpos -1 ypos 0
    text file_text xpos 11 ypos -24 size 15  color "#ffffff"

screen load:

    tag menu

    imagemap:
        ground 'saveload_ground.png'
        idle 'saveload_idle.png'
        hover 'saveload_hover.png'
        selected_idle 'saveload_selected.png'
        selected_hover 'saveload_hover.png'
        cache False

        hotspot (1182,873, 148, 103) action FilePage(1)
        hotspot (936, 873, 148, 91) action FilePage(2)

        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (619, 274, 301, 233) action FileAction(1):
            use load_save_slot(number=1)
        hotspot (987, 274, 301, 222) action FileAction(2):
            use load_save_slot(number=2)
        hotspot (1358, 274, 298, 220) action FileAction(3):
            use load_save_slot(number=3)
        hotspot (617, 555, 304, 225) action FileAction(4):
            use load_save_slot(number=4)
        hotspot (987, 556, 201, 244) action FileAction(5):
            use load_save_slot(number=5)
        hotspot (1358, 555, 304, 226) action FileAction(6):
            use load_save_slot(number=6)


        hotspot (81, 531, 252, 99) action ShowMenu('preferences')
        hotspot (13, 630, 369, 97) action ShowMenu('load')
        hotspot (10, 731, 365, 93) action ShowMenu('save')
        hotspot (33, 832, 284, 87) action MainMenu()
        hotspot (38, 327, 373, 106) action Return()



screen save:

    tag menu

    imagemap:
        ground 'saveload_ground.png'
        idle 'saveload_idle.png'
        hover 'saveload_hover.png'
        selected_idle 'saveload_selected.png'
        selected_hover 'saveload_hover.png'
        cache False

        hotspot (1182,873, 148, 103) action FilePage(1)
        hotspot (936, 873, 148, 91) action FilePage(2)

        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (619, 274, 301, 233) action FileAction(1):
            use load_save_slot(number=1)
        hotspot (987, 274, 301, 222) action FileAction(2):
            use load_save_slot(number=2)
        hotspot (1358, 274, 298, 220) action FileAction(3):
            use load_save_slot(number=3)
        hotspot (617, 555, 304, 225) action FileAction(4):
            use load_save_slot(number=4)
        hotspot (987, 556, 201, 244) action FileAction(5):
            use load_save_slot(number=5)
        hotspot (1358, 555, 304, 226) action FileAction(6):
            use load_save_slot(number=6)


        hotspot (81, 531, 252, 99) action ShowMenu('preferences')
        hotspot (13, 630, 369, 97) action ShowMenu('load')
        hotspot (10, 731, 365, 93) action ShowMenu('save')
        hotspot (33, 832, 284, 87) action MainMenu()
        hotspot (38, 327, 373, 106) action Return()

init python:
    config.thumbnail_width = 340
    config.thumbnail_height = 245
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu

    imagemap:
        ground 'gui/config_ground.png'
        idle 'gui/config_idle.png'
        hover 'gui/config_hover.png'
        selected_idle 'gui/config_sidle.png'
        selected_hover 'gui/config_shover.png'
        cache False

        ## DISPLAY
        hotspot (788, 178, 163, 61) action Preference('display', 'fullscreen')
        hotspot (1015, 174, 152, 60) action Preference('display', 'window')

        ## TRANSITION
        hotspot (825, 360, 89, 56) action Preference('transitions', 'all')
        hotspot (1045, 357, 94, 62) action Preference('transitions', 'none')

        ## SKIP
        hotspot (781, 524, 291, 63) action Preference('skip', 'seen')
        hotspot (1106, 519, 88, 66) action Preference('skip', 'all')

        ## AFTER CHOICES
        #hotspot (940, 532, 105, 58) action Preference('after choices', 'stop')
        #hotspot (1055, 532, 114, 56) action Preference('after choices', 'skip')
        ## BEGIN SKIPPING
        #hotspot (696, 624, 260, 63) action Preference('begin skipping')


        hotbar (269, 168, 328, 44) value Preference('text speed')
        hotbar (270,354,327,39) value Preference('music volume')
        hotbar (267, 522, 330, 40) value Preference('sound volume')
        #hotbar (421, 529, 302, 56) value Preference('auto-forward time')


        hotspot (1627, 205, 224, 73) action ShowMenu('preferences')
        hotspot (1574, 293, 333, 79) action ShowMenu('load')
        hotspot (1578, 384, 329, 75) action ShowMenu('save')
        hotspot (1615, 466, 261, 82) action MainMenu()
        hotspot (1626, 649, 228, 76) action Quit()
        hotspot (1572, 25, 336, 76) action Return()


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    imagemap:
        ground 'gui/yesno_ground.png'
        idle 'gui/yesno_idle.png'
        hover 'gui/yesno_hover.png'

        hotspot (383, 356, 234, 154) action yes_action
        hotspot (703, 356, 252, 154) action no_action

    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_sure.png"

    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete.png"

    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite.png"

    elif message == layout.LOADING:
        add "gui/yesno_load.png"

    elif message == layout.QUIT:
        add "gui/yesno_quit.png"

    elif message == layout.MAIN_MENU:
        add "gui/yesno_mm.png"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    hbox:
        style_group "quickmenu"

        xalign 1.0
        yalign 0.0


        imagemap:
            ground "gui/qm_idle.png"
            idle "gui/qm_idle.png"
            hover "gui/qm_hover.png"
            selected_idle "gui/qm_selected"
            selected_hover "gui/qm_selected.png"

            hotspot (1660, 791, 30, 39) action ShowMenu('preferences')
            hotspot (1699, 791, 33, 36) action ShowMenu("save")
            hotspot (1793, 845, 68, 155) action Preference("auto-forward", "toggle")
            hotspot (1615, 793, 36, 36) action Skip()
            hotspot (60, 822, 67, 186) action Rollback()
