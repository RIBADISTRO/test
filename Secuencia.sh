#!/bin/bash
clear; 
echo “CARGANDO, ESPERE POR FAVOR”;
echo “”;
for (( int j=1; j<=10;j++ ));
do
   echo -e “EJEMPLO $j \c” ;
   for (( i=0; i<=30; i++ ));
   do
      echo -e “\033[0;34m.\c”;
	sleep 0.05;
	done; 
      echo -e “\c”;
      echo -e “\t\033[0;32m[OK]\033[0m";
      done; 
      echo -e "\033[0;32mCARGADO CON EXITO\033[0m";
