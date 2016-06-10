#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

#Funcion que desempeña el thread
def worker(valor):
    print 'Thread tipo ', valor
    return
#Fin funcion que desempeña el thread

threads = list()

#Se añaden los threads a la lista
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

#Se les da un start a los threads para que hagan su funcion
for i in threads:
    i.start()
