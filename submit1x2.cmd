#!/bin/bash
#SBATCH --job-name="CNN1x2"
#SBATCH --workdir=.
#SBATCH --output=CNN1x2_%j.out
#SBATCH --error=CNN1x2_%j.err
#SBATCH --ntasks=2
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=6:00:00

horovodrun -np 2 --timeline-filename timeline1x2.json --autotune --autotune-log-file autotune1x2.csv python mainHorovod.py
