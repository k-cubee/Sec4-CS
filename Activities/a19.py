class album:
    def __init__(self, title, name, year, genre):
        self.title = title
        self.name = name
        self.year = year
        self.genre = genre


album_list = []
getting_info = True

while getting_info:
    title = input("Enter title: ")
    name = input("Enter name: ")
    year = int(input("Enter release year: "))
    genre = input("Enter genre: ")
    album_list.append(album(title, name, year, genre))

    while True:
        answer = input("Will you enter another album: ").upper()
        if answer == "NO":
            getting_info = False
            break
        elif answer == "YES":
            break

search_name = input("Enter the name of the ablum to search: ")
count = 0

for i in album_list:
    count += 1
    if i.title == search_name:
        print(
            f"Title: {i.title}, Artist: {i.name}, Year: {i.year}, Genre: {i.genre}")

if count == len(album_list) and album_list[len(album_list)-1].title != search_name:
    print("Not found")
