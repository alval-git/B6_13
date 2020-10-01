
import json
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import sma
@route("/albums/<artist>")
def albums(artist):
	albums_list = sma.Find(artist)
	counter = sma.CountAlbums(artist)
	if not albums_list:
		message = "Альбомов {} не найдено".format(artist)
		result = HTTPError(404, message)
	else:
		album_names = [album.album for album in albums_list]
		result = "Количество альбомов {0} : {1}. Список альбомов {0}:\n".format(artist,counter)
		result += ",\n".join(album_names)		
	return result
@route("/albums", method="POST")
def reqALbum():
	album = {
		  "year" : request.forms.get("year"),
		  "artist" : request.forms.get("artist"),
	      "genre" : request.forms.get("genre"),
	      "album" : request.forms.get("album")
	}
	message_1 = "Год указывается в формате 4-х цифр"
	message_2 = "Данный альбом уже в базе данных"
	if len(album["year"]) != 4:
		return HTTPError(406, message_1)
	
	elif sma.DublicationFinder(album["album"]):
		return HTTPError(409, message_2)
	else:
		sma.save(album)
		return("Данные успешно сохранены")
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)

