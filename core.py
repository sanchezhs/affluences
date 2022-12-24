###################################################################################################
# Falta: mostrar errores, tratar excepciones, saltar la confirmacion de correo, automatizar reserva
###################################################################################################
import send_post as send
import get_request as get
import parse_resources as p
from errorDatos import ErrorDatos
from datetime import datetime
from json_data import JsonGet as jg, JsonPost as jp


def search_resource(day):
    respuesta = get.GetRequest(jg.headers_get, jg.params_get).search(day)
    return respuesta

def check_resource(puestos, num_puesto):
    i = 0
    while i < len(puestos):
        if puestos[i] == str('{:0>3d}'.format(num_puesto)):
            return puestos[i-1]
        i += 1
    if i >= len(puestos):
        print('El puesto no está disponible para ninguna hora')
        return -1


def make_post(day, start_time, end_time, email, ident):
    actual_date = datetime.today()
    actual_date = actual_date.replace(day=day).strftime('%Y-%m-%d')
    jp.json_data_post['date'] = actual_date
    jp.json_data_post['start_time'] = start_time
    jp.json_data_post['end_time'] = end_time
    jp.json_data_post['email'] = email
    post = send.SendPost(jp.headers_post, jp.json_data_post, ident)
    post.send_post()

def book(day, start_time, end_time, email, num_puesto):
    if day > 31: raise ErrorDatos()
    respuesta = search_resource(day)
    puestos = p.Parser(respuesta.text).to_list()
    ident = check_resource(puestos, num_puesto)
    make_post(day, start_time, end_time, email, ident)