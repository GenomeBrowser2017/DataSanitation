#!/bin/bash

function convertSpaceDelimitedToTabDelimited() {
  inputFile=$1
  eval "tr -s ' ' '\t' < $inputFile > $inputFile.tabbed"
  eval "mv $inputFile $inputFile.orig.spaced"
  eval "mv $inputFile.tabbed $inputFile"
}

convertSpaceDelimitedToTabDelimited $1
