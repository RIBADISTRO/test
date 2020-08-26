#!/bin/bash
# interactivo.sh Ejemplo de  un script interactiv

=======
echo -n "Bienvenido bash shell"
>>>>>>> julio
echo -n "Digame su nombre:"
read NOMBRE
read -p "Y su apellido: " APELLIDO
printf "Hola %s %s" $NOMBRE $APELLIDO

