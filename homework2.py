import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	autos = [

		('Ford', 'Tauras', 52),
		('Ford', 'Escape', 15),
		('Ford', 'Explorer', 42),
		('Honda', 'Accord', 58),
		('Honda', 'CRX', 26)
		]

	c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', autos)