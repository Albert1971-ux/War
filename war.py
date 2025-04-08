import random
import time


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        # Вариация силы удара для большей непредсказуемости
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))

        # Шанс критического удара (25%)
        if random.random() < 0.25:
            damage = int(damage * 1.5)
            print(f"🔥 КРИТИЧЕСКИЙ УДАР! 🔥 {self.name} наносит {damage} урона!")
        else:
            print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

        other.health -= damage

        # Здоровье не может быть отрицательным
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        return self.health > 0

    def status(self):
        health_bar = "❤️" * (self.health // 10) + "◽" * ((100 - self.health) // 10)
        return f"{self.name}: {health_bar} ({self.health}/100)"


class Game:
    def __init__(self):
        print("=== БИТВА ГЕРОЕВ ===")
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)

        computer_names = ["Дракула", "Мордор", "Кощей", "Тёмный рыцарь", "Чародей Хаоса"]
        computer_name = random.choice(computer_names)
        self.computer = Hero(computer_name)

        print(f"\nБитва начинается: {self.player.name} против {self.computer.name}!")
        print("Приготовьтесь к бою!\n")
        time.sleep(1)

    def display_status(self):
        print("\n" + "-" * 50)
        print(self.player.status())
        print(self.computer.status())
        print("-" * 50 + "\n")

    def player_turn(self):
        print(f"Ход {self.player.name}:")
        input("Нажмите Enter для атаки... ")
        self.player.attack(self.computer)
        time.sleep(1)

    def computer_turn(self):
        print(f"\nХод {self.computer.name}:")
        time.sleep(1.5)  # Небольшая задержка для драматичности
        self.computer.attack(self.player)
        time.sleep(1)

    def start(self):
        round_num = 1

        # Определение, кто ходит первым (50/50 шанс)
        player_first = random.choice([True, False])

        if player_first:
            print(f"{self.player.name} ходит первым!")
        else:
            print(f"{self.computer.name} ходит первым!")

        time.sleep(1)

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== РАУНД {round_num} ===")
            self.display_status()

            if player_first:
                self.player_turn()
                if not self.computer.is_alive():
                    break

                self.computer_turn()
                if not self.player.is_alive():
                    break
            else:
                self.computer_turn()
                if not self.player.is_alive():
                    break

                self.player_turn()
                if not self.computer.is_alive():
                    break

            round_num += 1

        self.display_status()

        if self.player.is_alive():
            print(f"\n🏆 Поздравляем! {self.player.name} победил! 🏆")
        else:
            print(f"\n💀 {self.computer.name} победил! Вы проиграли! 💀")

        print("\nИгра окончена!")


if __name__ == "__main__":
    game = Game()
    game.start()

    # Предложение сыграть еще раз
    while True:
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again in ["да", "y", "yes", "д"]:
            print("\n" + "=" * 60 + "\n")
            game = Game()
            game.start()
        else:
            print("\nСпасибо за игру! До встречи!")
            break
