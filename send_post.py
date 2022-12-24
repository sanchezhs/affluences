
import requests, json

class BookError(Exception): pass

class SendPost:

    def __init__(self, headers, json, resource_id):
        self.headers = headers
        self.json    = json
        self.resource_id = resource_id
        self.url = 'https://reservation.affluences.com/api/reserve/'+str(resource_id)

    def send_post(self):
        response = requests.post(self.url, headers=self.headers, json=self.json) 
        if response.status_code != 201:
            json_msg = json.loads(response.text)
            print(json_msg['errorMessage'])
            raise BookError()
        else:
            print('Reserva correcta')


