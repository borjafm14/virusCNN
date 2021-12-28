#!/bin/bash
#SBATCH --job-name="CNN2x2"
#SBATCH --workdir=.
#SBATCH --output=CNN2x2_%j.out
#SBATCH --error=CNN2x2_%j.err
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=2
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=6:00:00

echo "NODE 1: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}')
echo "NODE 2: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}')

horovodrun -np 4 -H $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}'):2,$(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}'):2 --timeline-filename timeline2x2.json --autotune --autotune-log-file autotune2x2.csv python mainHorovod.py
