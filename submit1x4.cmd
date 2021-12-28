#!/bin/bash
#SBATCH --job-name="CNN1x4"
#SBATCH --workdir=.
#SBATCH --output=CNN1x4_%j.out
#SBATCH --error=CNN1x4_%j.err
#SBATCH --ntasks=4
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=6:00:00

horovodrun -np 4 --timeline-filename timeline1x4.json --autotune --autotune-log-file autotune1x4.csv python mainHorovod.py
