
screen extras:
    tag menu
    imagemap:
        ground "gui/extra_idle.png"
        idle "gui/extra_idle.png"
        hover "gui/extra_hover.png"

        hotspot (540, 665, 178, 58) action ShowMenu('gallery')
        hotspot (1221, 665, 133, 61) action ShowMenu('musicroom')
        hotspot (856, 835, 210, 12) action Return()



#######################################################################
#######################################################################
#### This the code for the customize Gallery
#### Almost the same with the default gallery but with some alterations.




init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("1.mp3", always_unlocked=True)
    mr.add("Digital Lemonade.mp3")

screen musicroom:
    tag menu
    imagemap:
        ground 'gui/msc_idle.png'
        idle 'gui/msc_idle.png'
        hover 'gui/msc_hover.png'
        selected_idle 'gui/msc_hover.png'
        cache False

        # The buttons that play each track.
        hotspot (587, 167, 510, 82) action mr.Play ("1.mp3")
        hotspot (643, 314, 378, 58) action mr.Play("Happy Alley.mp3")

        # Buttons that let us advance tracks.
        hotspot (845, 492, 95, 95) action mr.Next()
        hotspot (717, 492, 101, 95) action mr.Previous()

        # Return
        hotspot (35, 557, 199, 91) action Return()

        # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "Happy Alley.mp3")
