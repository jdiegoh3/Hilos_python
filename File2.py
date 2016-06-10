#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

def worker():
    print threading.currentThread().getName(), ': Lanzado'
    time.sleep(2)
    print threading.currentThread().getName(), ': Deteniendo'

def servicio():
    print threading.currentThread().getName(), ': Lanzado'
    print threading.currentThread().getName(), ': Deteniendo'

#Asignacion nombres y creacion de threads
t = threading.Thread(target=servicio, name='Servicio') #Se asigna el nombre al Thread de Servicio con la accion servicio()
w = threading.Thread(target=worker, name='Worker')  #Se asigna el nombre al Thread de Worker con la accion worker()
z = threading.Thread(target=worker) #Se la funcion worker y nombre autoasignado de Thread-1

print "Thread Z, se autonombro como : ", z.getName()

#Se lanzan los threads
w.start()
z.start()
t.start()
