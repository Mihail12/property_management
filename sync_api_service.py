

class SyncApiService(object):
    model = Service1
    """
    There is a model called Service1
    where all data saved which were taken from the api
    """
    def __init__(self):
        super(SyncApiService, self).__init__()
        self.valid_data = []

    def get(self):
        "prowide a GET method to the api for information about new persons"
        data=[] # expample data
        if self.validate_info(data):
            self.save_data_to_db()
        self.send_message_invalid_data_to_service()


    def validate_info(self, data):
        """
        Serialize data which was provided, set to valid_data data which ready to save
        :param data:
        :return: True/False
        :rtype: Boolean
        """
        self.valid_data = [] # example validated data

    def save_data_to_db(self):
        "Use self.validated_data for saving in Service1 instance"
        NotImplemented()

    def send_message_invalid_data_to_service(self):
        "provide a simple message that service send an invalid data"
        "add error data"
        NotImplemented()
