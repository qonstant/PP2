import random
def guess_the_number():
    name = input('Hello! What is your name?' + '\n')
    number = random.randint(1, 20)
    guess = int(input('Well, ' + name + ', I am thinking of a number between 1 and 20.' +'\n' + 'Take a guess.' + '\n'))
    cnt = 1
    while guess != number:
        if number < guess:
            guess = int(input('Your guess is too large.' + '\n' + 'Take a guess.' + '\n'))
        elif number > guess:
            guess = int(input('Your guess is too low.' + '\n' + 'Take a guess.' + '\n'))
        cnt += 1
    print('Good job, ' + name + '! You guessed my number in ' + str(cnt) + ' guesses!')
guess_the_number()