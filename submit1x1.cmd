#!/bin/bash
#SBATCH --job-name="CNN1x1"
#SBATCH --workdir=.
#SBATCH --output=CNN1x1_%j.out
#SBATCH --error=CNN1x1_%j.err
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=19:00:00

python main.py
