import argparse
import errorDatos as err
import send_post as send
import core as core


def main():
    my_parser = argparse.ArgumentParser(prog='reservar.py', usage='%(prog)s day start-time end-time email place', description='Script para reservar puesto en Affluences')

    my_parser.add_argument('--day', '-d', type=int, help='día para reservar', required=True)
    my_parser.add_argument('--start-time', '-st', type=str, help='Hora de comienzo', required=True)
    my_parser.add_argument('--end-time', '-et', type=str, help='Hora de finalización', required=True)
    my_parser.add_argument('--email', '-e', type=str, help='Email para reservar', required=True)
    my_parser.add_argument('--place', '-p', type=int, help='Número del puesto', required=True)

    arguments = my_parser.parse_args()
    reserva = vars(arguments)   
    core.book(reserva['day'], reserva['start_time'], reserva['end_time'], reserva['email'], reserva['place'])

if __name__ == "__main__":
    try:
        main()
    except err.ErrorDatos:
        print('Error, introduce una fecha correcta')
    except send.BookError:
        pass


