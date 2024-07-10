#!/bin/tcsh
#SBATCH --job-name=MYJOB          # Job name
#SBATCH --output=OUTPUT_LOG       # Output file
#SBATCH --error=ERROR_LOG         # Error file
#SBATCH --ntasks=1                # Number of tasks (CPUs) to allocate
#SBATCH --mem=2G                  # Memory per node
#SBATCH --time=01:00:00           # Walltime limit

# Load any necessary modules
module load anaconda3
conda activate ENVIRONMENT_NAME
echo "I am running on ${HOSTNAME}"
cd OUTPUT_DIR
echo "I am running in ${PWD}"
# Run your executable or script or ANYTHING YOU WANT
python train.py --config config.json