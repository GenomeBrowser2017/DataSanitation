# DataSanitation

This repository is meant to collaborate on the data sanitation process. Following is a list of the files/data in this repository: (Please modify this file if you decide to change something.)

* `convertCoord.py` is a Python script that goes through an existing GFF3 file and fixes issues such as naming and coordinate locations.

* `convertCoord.sh` is a Bash script that wraps `convertCoord.py` and scripts the process of running that script for all GFF3 files in a directory.

* `preprocessPilerCR.sh` is a Bash script for for Fixing the PilerCR output.

* `runPipeline.sh` is a Bash script for running the whole data clean up pipeline
