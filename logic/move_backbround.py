def move_background(SCREEN, img, elemento, velocidad):
    X = (elemento["x"] - velocidad) % 1280
    SCREEN.blit(img, (X - 1280, elemento["y"]))
    if X < 1280:
        SCREEN.blit(img, (X, elemento["y"]))
    elemento["x"] = X