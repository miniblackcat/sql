import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	print("\nFORD DATA:\n")

	c.execute("SELECT * from inventory WHERE Make = 'Ford'")

	rows = c.fetchall()

	print('Make Model Quantity')
	print('-------------------')

	for r in rows:
		print(r[0], r[1], r[2])
`