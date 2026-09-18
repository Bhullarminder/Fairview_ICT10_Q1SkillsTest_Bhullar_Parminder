from pyscript import display, document


def calculate_total(e):

    document.getElementById("receipt").innerHTML = ""

    americano = document.getElementById("americano").checked
    spanish_latte = document.getElementById("spanish_latte").checked
    cold_brew_malt = document.getElementById("cold_brew_malt").checked
    affogato = document.getElementById("affogato").checked

    subtotal = (americano * 120) + (spanish_latte * 150) + (cold_brew_malt * 168) + (affogato * 180)

    tax = subtotal * 0.12

    total = subtotal + tax

    display("Receipt", target="receipt")
    display(f"Subtotal: ₱{subtotal}", target="receipt")
    display(f"Tax: ₱{tax}", target="receipt")
    display(f"Total: ₱{total}", target="receipt")