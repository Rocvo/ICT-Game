def start_game():
    print("Du bist in einem dunklen Wald. Es ist kalt und du hörst seltsame Geräusche.")
    print("Es gibt zwei Wege vor dir. Welchen wirst du wählen?")
    choose_path()

def choose_path():
    choice = input("Willst du nach links oder rechts gehen? (links/rechts): ").lower()

    if choice == "links":
        go_left()
    elif choice == "rechts":
        go_right()
    else:
        print("Bitte wähle 'links' oder 'rechts'.")
        choose_path()

def go_left():
    print("Du gehst nach links und siehst einen Fluss. Der Fluss ist breit und sieht gefährlich aus.")
    choice = input("Willst du schwimmen oder nach einer Brücke suchen? (schwimmen/brücke): ").lower()

    if choice == "schwimmen":
        print("Du schwimmst durch den Fluss. Das Wasser ist eisig und die Strömung stark.")
        print("Du schaffst es ans andere Ufer, aber verlierst dich im Wald. Spiel vorbei.")
    elif choice == "brücke":
        print("Du findest eine alte Holzbrücke. Sie sieht nicht stabil aus.")
        bridge_event()
    else:
        print("Bitte wähle 'schwimmen' oder 'brücke'.")
        go_left()

def bridge_event():
    print("Du entscheidest dich, über die Brücke zu gehen.")
    print("Die Brücke knarrt unter deinen Füßen. Plötzlich hörst du ein lautes Knacken!")
    choice = input("Willst du weitergehen oder zurückkehren? (weiter/zurück): ").lower()

    if choice == "weiter":
        print("Die Brücke bricht zusammen und du fällst in den Fluss. Du ertrinkst. Spiel vorbei.")
    elif choice == "zurück":
        print("Du gehst zurück und suchst einen anderen Weg.")
        print("Nach Stunden findest du endlich einen sicheren Pfad durch den Wald. Du überlebst, aber ohne Schatz.")
    else:
        print("Bitte wähle 'weiter' oder 'zurück'.")
        bridge_event()

def go_right():
    print("Du gehst nach rechts und siehst eine Höhle. Vor der Höhle stehen seltsame Zeichen auf dem Boden.")
    choice = input("Willst du die Höhle betreten oder außen herumgehen? (betreten/herum): ").lower()

    if choice == "betreten":
        cave_event()
    elif choice == "herum":
        print("Du gehst um die Höhle herum, doch plötzlich steht ein Monster vor dir!")
        print("Das Monster ist riesig und hat scharfe Zähne.")
        print("Du hast keine Chance zu entkommen. Spiel vorbei.")
    else:
        print("Bitte wähle 'betreten' oder 'herum'.")
        go_right()

def cave_event():
    print("Du betrittst die Höhle. Die Luft ist kalt und du siehst kleine Lichtpunkte an den Wänden.")
    print("Im Inneren der Höhle findest du einen alten Schlüssel.")
    choice = input("Willst du den Schlüssel nehmen oder ihn liegen lassen? (nehmen/liegenlassen): ").lower()

    if choice == "nehmen":
        print("Du nimmst den Schlüssel und gehst tiefer in die Höhle.")
        print("Am Ende der Höhle findest du eine große Schatztruhe.")
        print("Du öffnest sie mit dem Schlüssel und findest Gold und Juwelen! Du hast gewonnen!")
    elif choice == "liegenlassen":
        print("Du lässt den Schlüssel liegen und gehst weiter.")
        print("Plötzlich hörst du ein lautes Geräusch und die Höhle beginnt einzustürzen.")
        print("Du wirst von den Steinen begraben. Spiel vorbei.")
    else:
        print("Bitte wähle 'nehmen' oder 'liegenlassen'.")
        cave_event()

start_game()
