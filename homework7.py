import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# create a dictionary of sql queries
	sql = {'Taurus count': "SELECT count(make) FROM orders WHERE model = 'Taurus'",
			'Escape count': "SELECT count(make) FROM orders WHERE model = 'Escape'"}
			

	for keys, values in sql.items():
		c.execute(values)

		result = c.fetchone()

		print(keys + ":", result[0])

