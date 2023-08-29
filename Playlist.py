from collections import deque
name = input("name your play list: ")
if name == "":
    print("New Playlist")
print(name.upper())

class Playlist:
    def __init__(self, file):
        self.queue= deque()
        self.load_playlist(file)
        
    def load_playlist(self, file):
        with open(file, 'r') as file:
            for line in file:
                song = line.strip()
                print(song)
    
    #def add_song(self, song):
        #with open(file, 'a') as file
    
    def remove_track(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "Playlist is empty"
    
            
    
file = "playlist.txt"    
playlist = Playlist(file)
