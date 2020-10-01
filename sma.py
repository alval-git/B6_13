import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()
class Album(Base):
	__tablename__ = "album"
	id = sa.Column(sa.INTEGER, primary_key=True)
	year = sa.Column(sa.INTEGER)
	artist = sa.Column(sa.TEXT)
	genre = sa.Column(sa.TEXT)
	album = sa.Column(sa.TEXT)
def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()
def Find(artist):
	session = connect_db()
	albums = session.query(Album).filter(Album.artist == artist).all()
	return albums
def CountAlbums(artist):
	session = connect_db()
	albums = Find(artist)
	count = len(albums)
	return str(count)
def save(album):
	session = connect_db()
	new_album = Album(year = album["year"],
					  artist = album["artist"],
					  genre = album["genre"],
					  album = album["album"],)
	session.add(new_album)
	session.commit()
def DublicationFinder(name_album):
	session = connect_db()
	if session.query(Album).filter(Album.album == name_album).count() > 0:
		return True