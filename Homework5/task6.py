"""
🎵 TASK 6 — Playlist Update
Topic: dict of lists (mutations) + loops

Playlist: {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
Add one new artist to each genre list, then print all genres and artists.

"""
# Starter:
playlist = {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
# TODO: append one artist per genre; then print genre -> list
playlist["rock"] = playlist.get("rock", []) + ["Metallica"]
playlist["pop"] = playlist.get("pop", []) + ["Lady Gaga"]
playlist["jazz"] = playlist.get("jazz", []) + ["Louis Armstrong"]
for genre in playlist:
    print(genre, end=": ")
    for artist in playlist[genre]:
        print(artist, end=" ")
    print()