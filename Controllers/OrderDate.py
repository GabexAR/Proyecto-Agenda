import datetime

class OrderDate:
    def order_date(date: str):
        if len(date) == 10:
            if date[2] == "-" and date[5] == "-":
                # El formato es dd-mm-yyyy
                try:
                    birthday = datetime.datetime.strptime(date, '%d-%m-%Y')
                    close = True
                except ValueError:
                    print("Formato de fecha incorrecto")
                    close = False
                    birthday = None
            elif date[2] == "-" and date[5] == "-":
                # El formato es mm-dd-yyyy
                try:
                    birthday = datetime.datetime.strptime(date, '%m-%d-%Y')
                    
                except ValueError:
                    print("Formato de fecha incorrecto")
                    close = False
                    birthday = None


            else:
                birthday = datetime.datetime.strptime(date, '%Y-%m-%d')
                close = True
        else:
            print("Formato de fecha incorrecto")
            close = False
            birthday = None
        
        return birthday, close