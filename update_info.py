

class CreateUpdatePerson(object):
    """
    Update or create information about a person in the property
    There are Person instance with whole info about each person
    """

    def create_person(self):
        "add to Person instance"
        email = 'example@exp.com'
        self.send_mail_to_person(email)

    def update_person(self):
        "here will be updating by getting all data from tables(each service instance)"
        "where persons data saved"
        self.synchronize_with_other_services()
        "add extra information if needed"

    def synchronize_with_other_services(self):
        "Save all data to Person"
        "Data are taken from tables(each service instance)(such as Service1 and Service2)"
        "after the method for all lines in the tables set boolean True to synchronized field"
        NotImplemented()

    def send_mail_to_person(self, email):
        "just send mail to person who has parameter email"
        NotImplemented()