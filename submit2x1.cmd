#!/bin/bash
#SBATCH --job-name="CNN2x1"
#SBATCH --workdir=.
#SBATCH --output=CNN2x1_%j.out
#SBATCH --error=CNN2x1_%j.err
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --mem-per-cpu=31000MB
#SBATCH --time=6:00:00

echo "NODE 1: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}')
echo "NODE 2: " $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}')

horovodrun -np 2 -H $(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==1'{print $1}'):1,$(scontrol show hostnames $SLURM_JOB_NODELIST | awk NR==2'{print $1}'):1 --timeline-filename timeline2x1.json --autotune --autotune-log-file autotune2x1.csv python mainHorovod.py
