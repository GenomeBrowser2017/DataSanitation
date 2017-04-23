#!/bin/bash

scriptFolder="."
OBFolder=$1

for i in $(seq -f "%04g" 5 24)
do
  echo $i
  eval "$scriptFolder/preprocessPilerCR.sh $OBFolder/OB$i/Pilercr.gff"
  eval "$scriptFolder/convertCoord.sh $OBFolder/OB$i/"
done
