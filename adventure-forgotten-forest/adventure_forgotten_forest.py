print("======================================")
print(" Adventure into the Forgotten Forest")
print("======================================\n")

name = input("Type your name: ")
print("Welcome", name, "to this adventure!\n")

print("Before you begin, choose a power to aid you: ")
while True:
    power = input("Strength, Magic, or Stealth: ").lower()

    if power in ["strength", "magic", "stealth"]:
        print("You have chosen the power of", power.capitalize() + "!\n")
        break
    else:
        print("Select a power for this adventure from the available powers.\n")

# Start
answer = input(
    "You stand at the edge of the Forgotten Forest.\n"
    "Two paths lie ahead:\n"
    " - left towards the dark mountains\n"
    " - right towards the glowing village.\n\n"
    "Which way would you like to go? (left/right): ").lower()

# ---------------- LEFT PATH ----------------
if answer == "left":
    answer = input(
        "\nYou head towards the mountains and reach a massive cave.\n"
        "Do you want to enter the cave or climb the mountain? (cave/climb): ").lower()

    # CAVE PATH
    if answer == "cave":
        answer = input(
            "\nInside the cave, a sleeping dragon guards a pile of treasure.\n"
            "Do you sneak past the dragon, attack it, or try to befriend it? (sneak/attack/befriend): ").lower()

        if answer == "sneak":
            if power == "stealth":
                print("\nYou slip silently past the dragon and grab a strange glowing gem.\n"
                      "The gem pulses with hidden energy as you move deeper into the cave.")
            else:
                print("\nYou trip on a loose rock! The dragon stirs, but suddenly a rockslide collapses part of the cave,\n"
                      "blocking its path. You escape deeper inside, heart racing.")
        elif answer == "attack":
            if power == "strength":
                print("\nWith a mighty roar, you strike the dragon’s tail!\n"
                      "It thrashes, but you land a lucky blow and knock it unconscious.\n"
                      "Among the treasure, you find a silver shield and carry it onward.")
            else:
                print("\nYou swing at the dragon, but it awakens enraged.\n"
                      "Before it can kill you, you flee deeper into the cave, wounded but alive.")
        elif answer == "befriend":
            if power == "magic":
                print("\nUsing your magic, you speak to the dragon in ancient tongue.\n"
                      "It warns you of a cursed ruin deeper in the cave and allows you to pass.\n"
                      "The dragon even gives you a glowing scale for protection.")
            else:
                print("\nThe dragon only growls at your attempts. Luckily, it doesn’t attack,\n"
                      "and you slip further inside the cave while it watches.")
        else:
            print("\nNot a valid option. You wander aimlessly until you are lost.")
            quit()

        # Next step after cave
        answer = input(
            "\nDeeper inside, you discover an ancient ruin lit by torches.\n"
            "Do you push open the heavy stone door or search the side tunnels? (door/tunnels): ").lower()

        if answer == "door":
            print("\nThe stone door creaks open, revealing a stairway leading up towards the mountain peak...")
        elif answer == "tunnels":
            print("\nThe tunnels twist endlessly, but you eventually find sunlight at the mountain’s side exit...")
        else:
            print("\nNot a valid option. You become trapped in the darkness.")
            quit()

    # CLIMB PATH
    elif answer == "climb":
        answer = input(
            "\nYou climb the steep mountain path and reach a rope bridge over a canyon.\n"
            "Do you cross the bridge or search for another way? (cross/search): ").lower()

        if answer == "cross":
            if power == "strength":
                print("\nYou grip the ropes tightly and cross safely, even as the planks crack beneath you.")
            else:
                print("\nHalfway across, the ropes begin to fray! You dash forward just in time to reach the other side.")
        elif answer == "search":
            print("\nAfter hours of climbing, you find a hidden goat trail that circles around the canyon.")
        else:
            print("\nNot a valid option. You slip and fall.")
            quit()

        # Next step after mountain
        answer = input(
            "\nAt the top of the path, you find an abandoned watchtower.\n"
            "Do you investigate the tower or continue towards the peak? (tower/peak): ").lower()

        if answer == "tower":
            print("\nInside the tower, you discover maps of the forest and a steel sword left behind by a knight.")
        elif answer == "peak":
            print("\nYou ignore the tower and push onwards, climbing closer to the clouds.")
        else:
            print("\nNot a valid option. You wander until exhaustion takes you.")
            quit()

    else:
        print("\nNot a valid option. You lose.")
        quit()

    # Final step for LEFT path
    answer = input(
        "\nAt last, you emerge at the Mountain Summit, where an ancient altar awaits.\n"
        "A voice asks: Will you claim the Forest’s Power or Destroy it? (claim/destroy): ").lower()

    if answer == "claim":
        print("\nYou touch the altar and power floods your veins.\n"
              "The Forgotten Forest bows to your will.\n"
              "FINAL ENDING: Master of the Forest (Victory).")
    elif answer == "destroy":
        print("\nYou shatter the altar with all your strength.\n"
              "The curse is lifted, but the forest crumbles into ruin.\n"
              "FINAL ENDING: The Last Hero (Bittersweet Victory).")
    else:
        print("\nNot a valid option. The altar vanishes, leaving you with nothing.")

# ---------------- RIGHT PATH ----------------
elif answer == "right":
    answer = input(
        "\nYou arrive at a glowing village.\n"
        "The villagers warn you about bandits nearby.\n"
        "Do you stay in the village or explore the forest? (stay/explore): ").lower()

    # STAY IN VILLAGE
    if answer == "stay":
        answer = input(
            "\nThe villagers invite you to a festival.\n"
            "Do you join the celebration or rest at the inn? (festival/inn): ").lower()

        if answer == "festival":
            print("\nAt the festival, a masked figure offers you a mysterious potion.\n"
                  "You refuse to drink it, but gain their trust.\n"
                  "They whisper of a hidden temple deep in the forest...")
        elif answer == "inn":
            print("\nYou sleep peacefully and wake to find a map slipped under your door,\n"
                  "pointing towards the forest temple.")
        else:
            print("\nNot a valid option. You oversleep and miss your chance.")
            quit()

    # EXPLORE FOREST
    elif answer == "explore":
        answer = input(
            "\nYou venture into the forest and meet a hooded stranger.\n"
            "Do you talk to them or avoid them? (talk/avoid): ").lower()

        if answer == "talk":
            if power == "magic":
                print("\nThe stranger reveals themselves as a wizard.\n"
                      "They grant you a magical sword, glowing faintly with runes.")
            else:
                print("\nThe stranger gives you a riddle about a hidden temple, then vanishes in smoke.")
        elif answer == "avoid":
            print("\nYou avoid the stranger but soon stumble upon strange ruins half-buried in moss.")
        else:
            print("\nNot a valid option. You wander until lost.")
            quit()
    else:
        print("\nNot a valid option. You lose.")
        quit()

    # Final step for RIGHT path
    answer = input(
        "\nAfter your journey, you arrive at the Hidden Temple of the Forest.\n"
        "Inside, an ancient crown rests upon a stone pedestal.\n"
        "Do you wear the crown or leave it untouched? (wear/leave): ").lower()

    if answer == "wear":
        if power == "magic":
            print("\nThe crown accepts your magic.\n"
                  "You are crowned ruler of the Forgotten Forest.\n"
                  "FINAL ENDING: Crowned Sorcerer (Victory).")
        else:
            print("\nThe crown corrupts your soul, turning you into a tyrant.\n"
                  "FINAL ENDING: Shadow King (Defeat).")
    elif answer == "leave":
        print("\nYou leave the crown untouched.\n"
              "The temple blesses you with eternal peace.\n"
              "FINAL ENDING: Guardian of Balance (Victory).")
    else:
        print("\nNot a valid option. The temple fades away.")

else:
    print("\nNot a valid option. You lose.")

print("\nThank you for playing,", name, "the Great Adventurer!")

