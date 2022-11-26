class album:
    def __init__(self, title, name, year, genre):
        self.title = title
        self.name = name
        self.year = year
        self.genre = genre


def main():
    album_list = []
    again = True
    enter(album_list)

    while again:
        while True:
            answer = input("Will you use the program again: ").upper()
            if answer == "NO":
                again = False
                break
            elif answer == "YES":
                while True:
                    action = input(
                        "Enter or search for an ablum (E/S): ").upper()
                    if action == "E":
                        enter(album_list)
                        break
                    elif action == "S":
                        search(album_list)
                        break


def enter(album_list):
    title = input("Enter title: ")
    name = input("Enter name: ")
    year = int(input("Enter release year: "))
    genre = input("Enter genre: ")
    album_list.append(album(title, name, year, genre))


def search(album_list):
    search_name = input("Enter the name of the ablum to search: ")
    found = False

    for i in album_list:
        if i.title == search_name:
            found = True
            print(
                f"Title: {i.title}, Artist: {i.name}, Year: {i.year}, Genre: {i.genre}")

    if found == False:
        print("Not found")


main()
