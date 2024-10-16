def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    global round_number
    return choices[round_number % 3]

def determine_winner(player, computer):
    if player == computer:
        return "Ничья"
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        return "Игрок"
    else:
        return "Компьютер"

def play_round():
    player_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    
    if player_choice not in ["камень", "ножницы", "бумага"]:
        print("Некорректный ввод, попробуйте снова.")
        return None, None

    computer_choice = get_computer_choice()
    
    print(f"Компьютер выбрал: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    
    return player_choice, winner

def play_game():
    global round_number
    round_number = 0
    player_score = 0
    computer_score = 0

    for round_number in range(3):
        print(f"\nРаунд {round_number + 1}")
        player_choice, winner = play_round()
        
        if player_choice is None:
            round_number -= 1
            continue
        

        if winner == "Игрок":
            player_score += 1
            print("Вы выиграли этот раунд!")
        elif winner == "Компьютер":
            computer_score += 1
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд закончился вничью.")

    print("\nИтог игры:")
    if player_score > computer_score:
        print("Вы победили в игре!")
    elif computer_score > player_score:
        print("Компьютер победил в игре!")
    else:
        print("Игра закончилась вничью.")

play_game()
