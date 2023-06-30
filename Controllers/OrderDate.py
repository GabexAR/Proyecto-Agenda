import datetime 

class OrderDate():
    def order_date(date: str):
        try:
            birthday = datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            birthday = datetime.datetime.strptime(date, '%m-%d-%Y')

        birthday_order = birthday.strptime(birthday,'%Y-%m-%d')      

        return birthday_order 