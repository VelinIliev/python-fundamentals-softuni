class Weapon:
    def __init__(self, bullets: int):
        bullets = bullets

    def shoot(self):
        if bullets >= 1:
            bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f'Remaining bullets: {bullets}'

