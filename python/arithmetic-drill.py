import random

def play_game():
    a, b = random.randrange(1, 10), random.randrange(0, 10)
    try:
        while True:
            print a, "+", b, "=",
            answer = raw_input()

            if answer == "?":
                print a + b
            else:
                answer = int(answer)
                if answer == a + b:
                    print "Right!"
                else:
                    print "Wrong, try again!"
                    continue

            a, b = random.randrange(1, 10), random.randrange(0, 10)
    except:
        print "Goodbye!"
            
            
if __name__ == "__main__":
    play_game()
