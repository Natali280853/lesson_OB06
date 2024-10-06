### Код игры "Битва героев"

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()

        self.declare_winner()

    def player_turn(self):
        print(f"{self.player.name} здоровье: {self.player.health}")
        print(f"{self.computer.name} здоровье: {self.computer.health}")
        self.player.attack(self.computer)

    def computer_turn(self):
        print(f"{self.computer.name} атакует {self.player.name}!")
        self.computer.attack(self.player)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
