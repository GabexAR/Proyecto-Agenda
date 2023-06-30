from ..Entities.Contact import Contact
from ..Context import Context

class Date_Format: 

    def get_date_format(self, username):
        with Context() as context1:
            query = "select birthday from contact where state = 1 and username = %s "
            values = (username,)
            context1.mycursor.execute(query,values)
            date_birthday = context1.mycursor.fetchone()
        return date_birthday