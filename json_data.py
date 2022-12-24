

class JsonGet():
        ## Cabecera y cuerpo para GET
    headers_get = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'es',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://affluences.com',
        'Connection': 'keep-alive',
        'Referer': 'https://affluences.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'If-None-Match': 'W/"8350e-3/6ZIm0P4ekQLASvlu+LdFF2jkw"',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    params_get = {
        'date': '2022-06-14',
        'type': '3455',
    }


class JsonPost():
    ## Cabecera y cuerpo para POST
    headers_post = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'es',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Origin': 'https://affluences.com',
        'Connection': 'keep-alive',
        'Referer': 'https://affluences.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    json_data_post = {
        'email': 'samuelsanchez@uma.es',
        'date': '2022-06-16',
        'start_time': '12:00',
        'end_time': '13:00',
        'note': None,
        'user_firstname': None,
        'user_lastname': None,
        'user_phone': None,
        'person_count': 1,
    }


