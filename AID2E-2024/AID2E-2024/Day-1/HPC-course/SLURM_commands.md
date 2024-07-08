# Introduction to SLURM

SLURM is like a manager for a group of powerful computers. It helps you schedule and run tasks on these computers efficiently. Think of it as a smart assistant that helps you book time on a shared resource, like a community kitchen, so everyone gets a turn without conflicts.

## Interactive execution

Imagine you want to cook a meal in a community kitchen. You need to book a time slot and specify what resources (like stove, oven, and counter space) you need. salloc is the command you use to book these resources for an interactive session.

### Booking Resources with `salloc`

```bash
salloc --ntasks=2 --mem=4G --time=01:00:00
```

- `--ntasks=2`: This means you are booking 2 CPUs.
- `--mem=4G`: This means you need 4GB of memory.
- `--time=01:00:00`: This means you want allocatio for an hour.

This should produce a output similar to 

```bash
salloc: Granted job allocation 12345
salloc: Waiting for resource configuration
salloc: Nodes compute-node-01 are ready for job
```

```{admonition} Try this
:class: tip

Navigate to the git repo, and add a new text file `third_file.txt` to it, and push it to a new branch named `slurm-branch`
```


## Submitting jobs through `sbatch`

Once you have written your script or executable file, you can submit it as a job to be executed on the SLURM cluster using the `sbatch` command. This allows you to run your code in a batch mode, without the need for an interactive session.

To submit a job using `sbatch`, you need to create a submission script that specifies the necessary resources and commands for your job. Here's an example of a submission script, you can name it `run_job.csh`, ofcourse we need to modify some info here:

```bash
#!/bin/tcsh
#SBATCH --job-name=myjob           # Job name
#SBATCH --output=<path/to/output/output.log>        # Output file
#SBATCH --error=<path/to/output/error.log>       # Error file
#SBATCH --ntasks=1                 # Number of tasks (CPUs) to allocate
#SBATCH --mem=1G                   # Memory per node
#SBATCH --time=01:00:00            # Walltime limit

# Load any necessary modules
module load python/3.8
module load anaconda3

# Run your executable or script or ANYTHING YOU WANT
echo "I am going to sleep for 10s"
sleep 10s
python -c "print (1+3+4+5)"
sleep 15s
echo "I am going run something that does not exist"
AID2E_IS_AWESOME
echo "I am going to gracefully end this job"
```

Let's break down the different parts of the submission script:

- `#!/bin/bash`: This line specifies the interpreter to be used for the script (in this case, Bash).

- `#SBATCH --job-name=myjob`: This line sets the name of your job. You can choose any name you like.

- `#SBATCH --output=output.log`: This line specifies the file where the standard output of your job will be written.

- `#SBATCH --error=error.log`: This line specifies the file where the standard error of your job will be written.

- `#SBATCH --ntasks=1`: This line specifies the number of tasks (CPUs) to allocate for your job. You can adjust this number based on the requirements of your code.

- `#SBATCH --mem=1G`: This line specifies the amount of memory to allocate per node for your job. Again, you can adjust this based on your code's memory requirements.

- `#SBATCH --time=01:00:00`: This line sets the walltime limit for your job. It specifies the maximum amount of time your job can run.

To submit your job, save the submission script to a file (e.g., `myscript.csh`) and use the following command:

```bash
sbatch myscript.csh
```

This will submit your job to the SLURM cluster, and you will receive a job ID as output. You can use this job ID to monitor the status of your job using the `squeue` command.

That's it! You have successfully submitted a job using SLURM. Now you can sit back and let SLURM manage the execution of your code on the cluster.
