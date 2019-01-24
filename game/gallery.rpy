###############GALLERY##################
init python:

   # Step 1. Create the gallery object.
    g = Gallery()

    g.locked_button = "gui/commonlock.png" #this is the thumbnail image for ALL LOCKED gallery previews, found in the images folder

   # Step 2. Add buttons and images to the gallery.

   # A button that contains an image that automatically unlocks.
    g.button("prologue_1") #this is the name/label associated with your button for a particular image
    g.condition("persistent.unlock_1") #this is the requirement/condition that must be met for this gallery image to unlock
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png") #this creates a gallery image that overlaps a foreground on top of a bg, you can also use a single flattened image here

    g.button("prologue_2")
    g.condition("persistent.unlock_2")
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png")

    g.button("prologue_3")
    g.condition("persistent.unlock_3")
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png")

    g.button("prologue_4")
    g.condition("persistent.unlock_4")
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png")

    g.button("prologue_5")
    g.condition("persistent.unlock_5")
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png")

    g.button("prologue_6")
    g.condition("persistent.unlock_6")
    g.image("gui/game_menu.png", "gallery/prologue_1_max.png")

    #Step 3: generate the gallery and how it looks
screen gallery:

   # Ensure this replaces the main menu.
    tag menu

   # The background.
    imagemap:
        ground "gui/cg_ground.png"
        idle "gui/cg_ground.png" #this is the bg image for the gallery; found in the images folder
        hover "gui/cg_hover.png"

        hotspot (112, 991, 185, 74) action Return()
        hotspot (403, 892, 172, 76) action ShowMenu('gallery')
        hotspot (1221, 665, 133, 61) action ShowMenu('gallery')

   # A grid of buttons.
    add g.make_button("prologue_1", "gallery/prologue_1_min.png", xalign=0.219, yalign=0.05)
    add g.make_button("prologue_2", "gallery/prologue_1_min.png", xalign=0.500, yalign=0.05)
    add g.make_button("prologue_3", "gallery/prologue_1_min.png", xalign=0.781, yalign=0.05)

    add g.make_button("prologue_4", "gallery/prologue_1_min.png", xalign=0.219, yalign=0.605)
    add g.make_button("prologue_5", "gallery/prologue_1_min.png", xalign=0.500, yalign=0.605)
    add g.make_button("prologue_6", "gallery/prologue_1_min.png", xalign=0.781, yalign=0.605)
