#!/bin/bash
#SBATCH --job-name="CNN2x4"
#SBATCH --workdir=.
#SBATCH --output=CNN2x4_%j.out
#SBATCH --error=CNN2x4_%j.err
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=6:00:00

echo "NODE 1: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}')
echo "NODE 2: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}')

horovodrun -np 8 -H $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}'):4,$(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}'):4 --timeline-filename timeline2x4.json --autotune --autotune-log-file autotune2x4.csv python mainHorovod.py
