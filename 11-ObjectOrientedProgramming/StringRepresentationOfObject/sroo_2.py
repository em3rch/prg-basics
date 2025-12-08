# class definition
class Song():
    def __init__(self, artist, track_title, album, year) -> None:
       self.artist = artist
       self.track_title = track_title
       self.album = album
       self.year = year
    
    def __str__(self):
        return (f"Performer: {self.artist}\n"
                f"Title:     {self.track_title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")

def main() -> None:
    # object creation
    song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
    song2 = Song("Queen", "Bohemian Rhapsody", "A Night At the Opera", 1975)

    print(song1)
    print()
    print(song2)




if __name__ == "__main__":
    main()