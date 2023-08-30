from collections import deque
class Playlist:
    def __init__(self, file):
        self.queue = deque()
        self.load_playlist(file)

    def load_playlist(self, file):
        with open(file, 'r') as file:
            songs = file.read()

    def display_playlist(self, file):
        with open(file, 'r') as file:
            songs = file.read()
            print(songs)

    def add_song(self, song):
        self.queue.append(song)
        self.save_playlist()

    def save_playlist(self):
        with open("playlist.txt", 'a') as file:
            for song in self.queue:
                file.write(song + '\n')

    def remove_songs(self, file, song_to_delete):
        songs_to_keep = []

        with open(file, 'r') as file:
            for line in file:
                if line.strip() != song_to_delete:
                    songs_to_keep.append(line)

        with open(updated_file, 'w') as file:
            file.writelines(songs_to_keep)


print("Welcome to MP3 playlist manager! ")
while True:
    action = int(
        input("What do you want to do today? \n 1. View playlist \n 2. Add song to playlist \n 3. remove song from "
              "playlist\n  0 to end program\n "))

    file = "playlist.txt"
    updated_file = "playlist.txt"
    playlist = Playlist(file)

    if action == 1:
        playlist.display_playlist(file)

    if action == 2:
        new_song = input("Add a new song: ")
        playlist.add_song(new_song)
    if action == 3:
        while True:
            song_to_delete = input("which song to delete or k to go back: ")
            playlist.remove_songs(file, song_to_delete)
            print("Song removed successfully")
            playlist.display_playlist(updated_file)
            if song_to_delete == "k".lower():
                break
    elif action == 0:
        break
