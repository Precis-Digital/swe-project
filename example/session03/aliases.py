type SongName = str
type Lyrics = str
type SongToLyrics = dict[SongName, Lyrics]
type ArtistName = str
type ArtistToSongs = dict[ArtistName, SongToLyrics]


def show_lyrics(
    query: list[str],
    lyrics: ArtistToSongs,
) -> None: ...
