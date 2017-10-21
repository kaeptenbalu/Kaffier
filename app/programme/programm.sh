#!/bin/bash

i="0"

while [ $i -eq 0] do
read Barcode
echo "update bier set Anzahl = Anzahl + 1 where  Strichcode like $Barcode;" | sqlite3 ./sql/Data.db
echo "update EK set vorhanden = vorhanden - 1 where Produkt like Bier;" | sqlite3 ./sql/Data.db
done

