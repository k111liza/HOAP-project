import sqlite3

from scripts.resource_path import resource_path


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect(resource_path('DATABASE.db'))
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
    def count_meters(self, user_id, cold_water, hot_water, electricity):
        flist=[]
        list = self.cur.execute(f"SELECT Cold_water FROM Meters WHERE Users_id={user_id} and Cold_water = {cold_water} ORDER BY Year, Month DESK LIMIT 2 ").fetchall()
        res = list[1]-list[0]
        list1 = self.cur.execute(f"SELECT Hot_water FROM Meters WHERE Users_id={user_id} and Hot_water = {hot_water} ORDER BY Year, Month DESK LIMIT 2 ").fetchall()
        res1 = list1[1]-list1[0]
        list2 = self.cur.execute( f"SELECT Electricity FROM Meters WHERE Users_id={user_id} and Electricity = {electricity} ORDER BY Year  , Month DESK LIMIT 2 ").fetchall()
        res2 = list2[1]-list2[0]
        return flist+[[27.72*res+27.72*res1+4.12*res2], [27.72*res], [27.72*res1],[4.12*res2]]
    def get_metersdata(self, user_id, month, year, price):
        return self.cur.execute(f'SELECT * FROM Meters Where Users_id={user_id} AND Price={price} AND Month={month} AND Year={year} ').fetchone()
    def show_data(self, user_id):
        return self.cur.execute(f'SELECT * FROM Meters LEFT JOIN Repforuser on Meters.id = Repforuser.Meters_id WHERE Users_id = {user_id}').fetchall()
    def get_user(self, user_id):
        return self.cur.execute(f'SELECT * FROM Users WHERE id = {user_id}').fetchone()
    def add_check(self, meters_id, paymentdate):
        self.cur.execute(f"INSERT INTO Repforuser (Meters_id, Paymentdate) VALUES ('{meters_id}', '{paymentdate}')")
        self.con.commit()
    def get_graphic(self, user_id):
        return self.cur.execute(f"SELECT Month, Year, Cold_water, Hot_water, Electricity FROM Meters WHERE Users_id = {user_id} ORDER BY Year, Month").fetchall()

    def get_notification(self):
        return self.cur.execute(f"SELECT *  FROM Notifications ORDER BY id DESC").fetchall()

        



