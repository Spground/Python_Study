
number = 7;
guess = -1;
print("Guess a number:\n");
while guess != number:
        guess = int(input("Is it ..."));

        if guess == number:
                print("You got it!");
                break;
        elif guess < number:
                print("It is bigger");
        elif guess > number:
                print("It is not so big...");
input("Press any key to return");
