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
