#!/bin/bash
#DanielVila

#hacer git de toda la carpeta
git add *
#Escribir comentario
echo 'Dime el mensaje para el commit : '
read nombre

git commit -m "$nombre"
#hacer el push para subir los archivos
git push -u origen master
