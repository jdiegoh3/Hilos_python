#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import logging
import time

#Damos el formato para la sentencia logging.debug así [LEVELNAME] - Nombre del thread : Mensaje
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')

def worker():
    logging.debug('Lanzado') #Llamamos al logging creado
    time.sleep(2)
    logging.debug('Deteniendo') #Llamamos al logging creado

w = threading.Thread(target=worker, name='Worker') #Crearmos el thread
w.start() #Iniciamos el thread
