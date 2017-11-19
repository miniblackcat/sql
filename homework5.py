import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("""CREATE TABLE orders
				(make TEXT, model TEXT, order_date TEXT)
				""")

	dates = [
			('Ford', 'Taurus', '2017-01-01'),
			('Ford', 'Taurus', '2017-06-02'),
			('Ford', 'Taurus', '2017-07-15'),
			('Ford', 'Escape', '2017-01-12'),
			('Ford', 'Escape', '2017-03-15'),
			('Ford', 'Escape', '2017-06-03'),
			('Ford', 'Explorer', '2017-02-05'),
			('Ford', 'Explorer', '2017-05-06'),
			('Ford', 'Explorer', '2017-06-06'),
			('Honda', 'Accord', '2017-03-01'),
			('Honda', 'Accord', '2017-04-02'),
			('Honda', 'Accord', '2017-06-03'),
			('Honda', 'CRX', '2017-10-01'),
			('Honda', 'CRX', '2017-10-15'),
			('Honda', 'CRX', '2017-11-01')
			]

	c.executemany("INSERT INTO orders VALUES(?, ?, ?)", dates)