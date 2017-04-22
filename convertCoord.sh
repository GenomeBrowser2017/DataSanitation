#!/bin/bash

#configuration
convertPy="/home/hubert/class/gbrowse/convertCoords/convertCoord.py"

#runConvertCoordinates - replaces the original gff file with the recoordinated file and archives the original to original.old
function runConvertCoordinates(){
  #echo $1;
  targetFile=$1;
  #rename originalFile to originalFile.old
  eval "mv $targetFile $targetFile.old"
  #generate the recoordinated file in its place
  eval "python $convertPy $targetFile.old > $targetFile"
}

function runConvertCoordinates_Folder(){
  targetFolder=$1;
  #get array of files in folder
  gffFiles=($targetFolder/*.gff);
  for file in "${gffFiles[@]}"; do
    if [[ ! "$file" =~ ^.*/Genes.gff$ ]]; then
      echo "runningConvertCoordinates on $file"
      runConvertCoordinates $file;
    fi
  done;
}

#runConvertCoordinates $1;
runConvertCoordinates_Folder $1;
