import requests
from datetime import datetime


class DateException(Exception): pass
class GetRequest:

    def __init__(self, headers, params):
        self.headers = headers
        self.params  = params
        self.url     = "https://reservation.affluences.com/api/resources/9f9bd433-8932-41ce-8f36-4e66876286cd/available"


    def search(self, search_day):
        actual_date = datetime.today()
        if search_day - actual_date.day > 2:
            raise DateException('Error reservando para el día %r', search_day)
        elif search_day < actual_date.day:
            raise DateException('Error reservando para el día %r', search_day)
        else:
            actual_date = actual_date.replace(day=search_day)
            self.params['date'] = actual_date.strftime('%Y-%m-%d')
            #print('Parametros---------')
            #print(self.params)
            return self.send_request()


    def send_request(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response

    def print(self):
        print(self.headers)
        print(self.params)

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params




