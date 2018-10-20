def rpsls(option):
    if option == "RPSLS":
        line = "-"
        import random
        #main
        player_rps = input('Rock, Paper, Scissors, Lizard, or Spock:\t').upper()
        computer_rps = ['ROCK', 'PAPER', 'SCISSORS', 'SPOCK', 'LIZARD']
        game_rps = random.choice(computer_rps)
        # Player
        if player_rps == 'ROCK':
            print('Player picked Rock')
        elif player_rps == 'PAPER':
            print('Player picked Paper')
        elif player_rps == 'SCISSORS':
            print('Player picked Scissors')
        elif player_rps == 'SPOCK':
            print('Player picked Spock')
        elif player_rps == 'LIZARD':
            print('Player picked Lizard')
        # Computer
        if game_rps == 'ROCK':
            print('Computer picked Rock')
        elif game_rps == 'PAPER':
            print('Computer picked Paper')
        elif game_rps == 'SCISSORS':
            print('Computer picked Scissors')
        elif game_rps == 'SPOCK':
            print('Computer picked Spock')
        elif game_rps == 'LIZARD':
            print('Computer picked Lizard')
        # Output for rock
        if player_rps == "ROCK" and game_rps == "SCISSORS":
            print("Rock crushes scissors, the Player wins!")
        if player_rps == "SCISSORS" and game_rps == "ROCK":
            print("Rock crushes scissors, the Computer wins!")
        if player_rps == "ROCK" and game_rps == "PAPER":
            print("Paper covers rock, the Computer wins!")
        if player_rps == "PAPER" and game_rps == "ROCK":
            print("Paper covers rock, the Player wins!")
        if player_rps == "ROCK" and game_rps == "SPOCK":
            print("Spock vaporizes rock, the Computer wins!")
        if player_rps == "SPOCK" and game_rps == "ROCK":
            print("Spock vaporizes rock, the Player wins!")
        if player_rps == "ROCK" and game_rps == "LIZARD":
            print("Rock crushes lizard, the Player wins!")
        if player_rps == "LIZARD" and game_rps == "ROCK":
            print("Rock crushes lizard, the Computer wins!")
        # Output for paper
        if player_rps == "PAPER" and game_rps == "LIZARD":
            print("Lizard eats paper, the Computer wins!")
        if player_rps == "LIZARD" and game_rps == "PAPER":
            print("Lizard eats paper, the Player wins!")
        if player_rps == "PAPER" and game_rps == "SCISSORS":
            print("Scissors cuts paper, the Computer wins!")
        if player_rps == "SCISSORS" and game_rps == "PAPER":
            print("Scissors cuts paper, the Player wins!")
        if player_rps == "PAPER" and game_rps == "SPOCK":
            print("Paper disproves spock, the Player wins!")
        if player_rps == "SPOCK" and game_rps == "PAPER":
            print("Paper disproves spock, the Computer wins!")
            # Output for scissors
        if player_rps == "SCISSORS" and game_rps == "SPOCK":
            print("Spock smashes scissors, the Computer wins!")
        if player_rps == "SPOCK" and game_rps == "SCISSORS":
            print("Spock smashes scissors, the Computer wins!")
        if player_rps == "SCISSORS" and game_rps == "LIZARD":
            print("Scissors decapitates lizard, the Player wins!")
        if player_rps == "LIZARD" and game_rps == "SCISSORS":
            print("Scissors decapitates lizard, the Computer wins!")
        # Output for spock
        if player_rps == "SPOCK" and game_rps == "LIZARD":
            print("Lizard poisons spock, the Computer wins!")
        if player_rps == "LIZARD" and game_rps == "SPOCK":
            print("Lizard poisons spock, the Player wins!")
        if player_rps == game_rps:
            print("It's a tie!")
        print(line * 45)
