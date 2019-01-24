init:
    image blossoms = SnowBlossom(Animation("mouse.png", 0.20,
                                           "mouse.png", 0.20))


    image lluvia = SnowBlossom("mouse.png", count=10000, border=500, xspeed=(1), yspeed=(500), start=(100), horizontal=False)

    image bala = SnowBlossom("mouse.png", count=10, border=50, xspeed=(1000), yspeed=(0), start=(100), horizontal=True)
