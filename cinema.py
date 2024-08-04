class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}  # словарь для хранения фильмов {movie_id: movie_name}
        self.users = {}  # словарь для хранения пользователей {user_id: user_name}
        self.tickets = (
            {}
        )  # словарь для хранения билетов {ticket_id: (user_id, movie_id)}
        self.movie_id_counter = 1
        self.user_id_counter = 1
        self.ticket_id_counter = 1

    def addMovie(self, movie_name):
        self.movies[self.movie_id_counter] = movie_name
        self.movie_id_counter += 1

    def showAllMovies(self):
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, user_name):
        self.users[self.user_id_counter] = user_name
        self.user_id_counter += 1

    def buyTicket(self, user_id, movie_id):
        if user_id in self.users and movie_id in self.movies:
            self.tickets[self.ticket_id_counter] = (user_id, movie_id)
            self.ticket_id_counter += 1
        else:
            print("Неправильный ID фильма или пользователя")

    def cancelTicket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
        else:
            print("Билет не найден")


def main():
    system = CinemaTicketSystem()

    while True:
        print(
            "\nЗдравствуйте, у вас есть следующие доступные функции:\n1. Добавить новый фильм;\n2. Показать все доступные фильмы;\n3. Добавить нового пользователя;\n4. Купить билет;\n5. Отменить покупку билета;"
        )
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            movie_name = input("Введите название фильма: ")
            system.addMovie(movie_name)

        elif choice == "2":
            system.showAllMovies()

        elif choice == "3":
            user_name = input("Введите имя пользователя: ")
            system.addUser(user_name)

        elif choice == "4":
            user_id = int(input("Введите ID пользователя: "))
            movie_id = int(input("Введите ID фильма: "))
            system.buyTicket(user_id, movie_id)

        elif choice == "5":
            ticket_id = int(input("Введите ID билета: "))
            system.cancelTicket(ticket_id)


if __name__ == "__main__":
    main()
