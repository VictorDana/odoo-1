#!/bin/bash
#DanielVila

#hacer git de toda la carpeta
git add *
#hacer commit - cambiar el mensaje por el que queremos
#Parte comentario automatico
echo 'Dime el mensaje para el commit : '
read nombre

git commit -m $nombre
#hacer el push para subir los archivos
git push -u origen master
