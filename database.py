import sqlite3

from scripts.resource_path import resource_path


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect('DATABASE.db')
        self.cur = self.con.cursor()
    def get_login(self, login : str, password):
        res = self.cur.execute(f"SELECT id, Name, Surname FROM Users WHERE Email = '{login.strip()}' and Password = '{password}'").fetchone()
        if res is not None:
            return res
        else:
            return False
    def registration (self, email, name, surname, password):
        search = self.cur.execute(f"SELECT Email FROM Users WHERE Email=='{email}'").fetchone()   
        if search is not None:
            return 'Такая почта уже зарегестрирована'

        else:
            self.cur.execute(f"INSERT INTO Users(Name, Surname, Email, Password) VALUES ('{name}', '{surname}', '{email}', '{password}')")
            self.con.commit()
    def send_meters_data(self, hot_water, cold_water,  month, user_id, year, price,  electricity):
        id = self.cur.execute(f"INSERT INTO Meters(Hot_water, Cold_water, Month, Users_id, Year, Price, Electricity) VALUES ({hot_water}, {cold_water}, {month}, {user_id}, {year}, {price}, {electricity}) RETURNING id").fetchone()
        self.con.commit()
        return id[0]
    def get_metersdata(self, user_id, month, year, price):
        return self.cur.execute(f'SELECT * FROM Meters Where Users_id={user_id} AND Price={price} AND Month={month} AND Year={year} ').fetchone()
    def show_data(self, user_id):
        return self.cur.execute(f'SELECT * FROM Meters LEFT JOIN Repforuser on Meters.id = Repforuser.Meters_id WHERE Users_id = {user_id}').fetchall()
    def get_user(self, user_id):
        return self.cur.execute(f'SELECT * FROM Users WHERE id = {user_id}').fetchone()
    def add_check(self, meters_id, paymentdate):
        self.cur.execute(f"INSERT INTO Repforuser (Meters_id, Paymentdate) VALUES ('{ meters_id}', '{paymentdate}')")
        self.con.commit()
    def get_graphic(self, user_id):
        return self.cur.execute(f"SELECT Month, Year, Cold_water, Hot_water, Electricity FROM Meters WHERE Users_id = {user_id} ORDER BY Year, Month").fetchall()



        



