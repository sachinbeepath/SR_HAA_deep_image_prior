#!/bin/bash

#SBATCH --account=def-sfabbro

#SBATCH --time=0-2:00

#SBATCH --array=1-349

#SBATCH --mem=8000M

./my_executable.exe $(($SLURM_ARRAY_TASK_ID*6 -6))

