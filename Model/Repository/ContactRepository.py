from ..Entities.Contact import Contact
from ..Context import Context
import datetime 
class ContactRepository:

    def get_contacts_by_user(self, username):
        with Context() as context1:            
            query = "SELECT * FROM contact WHERE state = 1 && username = %s "
            values = (username,)
            context1.mycursor.execute(query,values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
           
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]            
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            date_str = contactDB[6] 
            if not date_str == None:
                contact.birthday = date_str.strftime('%d-%m-%Y')
                print("Prueba")
            else:
                contact.birthday = date_str
            contacts.append(contact)
        return contacts
    
    def get_contact(self, contact):
        with Context() as context1:
            query = "SELECT * FROM contact WHERE idcontact = %s"
            values = (contact.id,)
            context1.mycursor.execute(query, values)
            contactDB = context1.mycursor.fetchone()
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
        return contact
    
    def add_contact(self, contact):
        with Context() as context1:
            query = "INSERT INTO contact (name, surname, email, username, state, birthday) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (contact.name, contact.surname, contact.email, contact.username, contact.state, contact.birthday)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            contact.id = context1.mycursor.lastrowid
        return contact

    def update_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET name = %s, surname = %s, email = %s WHERE idcontact = %s AND username = %s"
            values = (contact.name, contact.surname, contact.email, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET state = %s WHERE idcontact = %s AND username = %s"
            values = (0, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
        
