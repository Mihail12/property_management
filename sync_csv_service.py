

class SyncCsvService(object):
    """
    There is a model called Service2
    where all data from csv files saved which were taken after parse the files
    """
    def __init__(self):
        super(SyncCsvService, self).__init__()
        self.valid_data = []
        self.parsed_data = []
        self.files = ['', '']

    def parse_ftp_for_csv(self):
        "parsing thought ftp server for new files"
        "than save it to own directory"
        ":return all names of files from own directory and save to self.files"
        NotImplemented()

    def process_csv_data(self):
        "process all files which were found"
        files = self.parse_ftp_for_csv()
        for file in files:
            self.parse_csv_file(file)
            if self.validate_info():
                self.save_data_to_db()
            self.send_message_invalid_data_to_service()

    def parse_csv_file(self, file):
        "parse file and create a dict with all the data and save it to self.parsed_data"
        NotImplemented()

    def validate_info(self):
        """
        Serialize data base on self.parsed_data, set to valid_data data which ready to save
        :param data:
        :return: True/False
        :rtype: Boolean
        """
        self.valid_data = [] # example validated data

    def save_data_to_db(self):
        "Use self.validated_data for saving in Service1 instance"
        NotImplemented()

    def send_message_invalid_data_to_service(self):
        "provide a simple message that service sent an invalid data"
        "add error data"
        "this could be an .csv file"
        NotImplemented()