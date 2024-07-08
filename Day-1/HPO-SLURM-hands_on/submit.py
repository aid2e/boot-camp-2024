import json
import subprocess
import os
import itertools
import argparse

def generate_configurations(config_template):
    # Load the config template
    with open(config_template, 'r') as f:
        template = json.load(f)

    # Generate all possible combinations of parameters
    keys = template.keys()
    values = template.values()
    configurations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]

    return configurations

def submit_slurm_job(configuration, output_dir):
    # Fill in the variables in the configuration
    # ...

    # Submit the SLURM job
    # ...

    # Example command to submit a SLURM job
    # subprocess.run(['sbatch', 'job_script.sh'])

    # Print the configuration and output directory
    print(f"Configuration: {configuration}")
    print(f"Output Directory: {output_dir}")

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('output_dir', help='Output directory')
    args = parser.parse_args()

    # Path to the config template
    config_template = 'config_template.json'

    # Generate configurations
    configurations = generate_configurations(config_template)

    # Submit SLURM jobs for each configuration
    for configuration in configurations:
        submit_slurm_job(configuration, args.output_dir)