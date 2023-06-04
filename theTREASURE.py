import random

file_path = "myfile.txt"

# Modify the file content
with open(file_path, "w") as treasure:
    for num in range(10):
        times = random.randint(1, 20)
        treasure.write(str(num) * times)

    treasure.write("TREASURE")

    for num in range(9, -1, -1):
        times = random.randint(1, 20)
        for num in range(times):
            treasure.write(str(num))


###############################################step 2
def play(file_path):
    with open(file_path, "r") as treasure:
        content = treasure.read()
        treasure.seek(0)
        count = 0
        while True:
            side = int(input("Where do you want to move? [1 - forward, 2 - backward]: "))
            if side == 1:
                steps = int(input("How many characters? "))
                treasure.seek(treasure.tell() + steps)
            elif side == 2:
                steps = int(input("How many characters? "))
                treasure.seek(treasure.tell() - steps)
            else:
                print("Invalid input. Try again.")
                continue
            count += 1
            current_pos = treasure.tell()
            if current_pos >= len(content):
                print("You reached the end of the file.")
                treasure.seek(treasure.tell() - steps)
            else:
                print(f"You hit: {content[current_pos]}")

            if not content[current_pos].isdigit():
                print(f"Congratulations! You found the letter '{content[current_pos]}' of the word 'TREASURE'!")
                print(f"Program finished. Well done! Number of turns: {count}")
                break

            print("... again ... until hit one of the 'TREASURE' letters ...")


file_path = "myfile.txt"
play(file_path)
