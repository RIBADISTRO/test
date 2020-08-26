#!/bin/bash
# interactivo.sh Ejemplo de  un script interactivo
echo -n "Bienvenido bash shell"
echo -n "Digame su nombre:"
read NOMBRE
read -p "Y su apellido: " APELLIDO
printf "Hola %s %s" $NOMBRE $APELLIDO

