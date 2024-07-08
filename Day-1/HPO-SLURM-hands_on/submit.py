import json
from joblib import Parallel, delayed
import subprocess
import os, uuid
from itertools import product
import argparse

def run_setting(script_to_run: str):
    subprocess.run(['tcsh', script_to_run])

def submit_slurm_job(configuration, output_dir, isSLURM=False):
    sweep_dict = {}
    sweep_dict["hidden_layer_sizes"] = [[100], [100, 50], [100, 50, 25]]
    sweep_dict["activation"] = ['relu', 'tanh']
    sweep_dict["alpha"] = [0.0001, 0.001, 0.01]
    joblib_Scripts = []
    # Generate all combinations of parameters
    keys, values = zip(*sweep_dict.items())
    
    for idx, combination in enumerate(product(*values)):
        # Update configuration with the current combination
        unqiue_identifier = str(uuid.uuid4())
        configuration["unique_identifier"] = unqiue_identifier
        for key, value in zip(keys, combination):
            configuration[key] = value
        # Create a directory for the output
        tmp_outdir = os.path.join(output_dir, "setting_" + str(idx))
        if os.path.exists(tmp_outdir):
            os.system(f"rm -rf {tmp_outdir}")
        os.makedirs(tmp_outdir, exist_ok=True)
        with open(os.path.join(tmp_outdir, "config.json"), "w") as f:
            json.dump(configuration, f)
        os.system(f"cp -r {args.script_dir}/* {tmp_outdir}/")
        # Update run.csh
        with open(os.path.join(tmp_outdir, "submit_train.csh"), "r") as f:
            lines = f.read()
        lines = lines.replace("OUTPUT_DIR", tmp_outdir)   
        lines = lines.replace("MYJOB", f"job_{idx}_{unqiue_identifier}")
        lines = lines.replace("OUTPUT_LOG", os.path.join(tmp_outdir, f"output_{idx}_{unqiue_identifier}.log"))
        lines = lines.replace("ERROR_LOG", os.path.join(tmp_outdir, f"error_{idx}_{unqiue_identifier}.log"))
        with open (os.path.join(tmp_outdir, "run.csh"), "w") as f:
            f.write(lines)
        if (isSLURM):
            sbatch_command = ['sbatch', os.path.join(tmp_outdir, "run.csh")]
            subprocess.run(sbatch_command)
        else:
            joblib_Scripts.append(os.path.join(tmp_outdir, "run.csh"))
    if (not isSLURM):
        Parallel(n_jobs=args.ncores)(delayed(run_setting)(script) for script in joblib_Scripts)

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', help='Output directory')
    parser.add_argument('--script_dir', type=str, help='Path to the script dir file')
    parser.add_argument('--isSLURM', type=str, help='is it slurm')
    parser.add_argument('--ncores', type=int, help='Number of cores', default=1)
    args = parser.parse_args()
    args.isSLURM = bool(args.isSLURM)
    
    if (not os.path.exists(args.output_dir)):
        os.makedirs(args.output_dir)
    if (not os.path.exists(args.script_dir)):
        print("Script file not found")
        exit(1)
    # Path to the config template
    config_template = os.path.join(args.script_dir, "config_template.json")

    # Generate configurations
    with open(config_template) as f:
        configurations = json.load(f)
    submit_slurm_job(configurations, args.output_dir, args.isSLURM)
        
