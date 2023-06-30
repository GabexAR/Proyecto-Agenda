import datetime

class OrderDate:
    def order_date(date: str):
        if len(date) == 10:
            if date[2] == "-" and date[5] == "-":
                # El formato es dd-mm-yyyy
                try:
                    birthday = datetime.datetime.strptime(date, '%d-%m-%Y')
                except ValueError:
                    print("Formato de fecha incorrecto")
            elif date[2] == "-" and date[5] == "-":
                # El formato es mm-dd-yyyy
                try:
                    birthday = datetime.datetime.strptime(date, '%m-%d-%Y')
                except ValueError:
                    print("Formato de fecha incorrecto")
            
            else:
                birthday = datetime.datetime.strptime(date, '%Y-%m-%d')
        else:
            print("Formato de fecha incorrecto")
        
        return birthday