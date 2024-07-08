
# William & Mary Research Computing: File Systems Tutorial

## Overview
William & Mary Research Computing offers multiple file systems for different purposes. This tutorial will guide you through each file system, its use case, and how to interact with it. Most of the content in this page has been taken from the lecture given at [W&M by W&M Research Computing](https://www.wm.edu/offices/it/services/researchcomputing/using/tutorials/introtohpc_0921231.pdf)

## File Systems

### 1. **Home Directory (`/sciclone/home`)**
- **Purpose**: Long-term storage for personal files and software installations.
- **Backup**: Yes.
- **Usage**:
  ```bash
  # Navigate to home directory
  cd /sciclone/home/<username>
  ```

### 2. **Data Directory (`/sciclone/data10`)**
- **Purpose**: Long-term storage for project data.
- **Backup**: Yes.
- **Usage**:
  ```bash
  # Navigate to data directory
  cd /sciclone/data10/<username>
  ```

### 3. **Scratch Directory (`/sciclone/scr10`)**
- **Purpose**: Temporary storage for running jobs. Files are purged after 90 days.
- **Backup**: No.
- **Usage**:
  ```bash
  # Navigate to scratch directory
  cd /sciclone/scr10/<username>
  ```

### 4. **Project Scratch Directory (`/sciclone/pscr`)**
- **Purpose**: Temporary storage for project-related jobs. Files are purged after 90 days.
- **Backup**: No.
- **Usage**:
  ```bash
  # Navigate to project scratch directory
  cd /sciclone/pscr/<username>
  ```

## Best Practices

- **Use Scratch Space for Jobs**: Always use scratch directories for running jobs to avoid overloading the home and data directories.
- **Backup Important Data**: Regularly backup important data stored in scratch directories to avoid data loss.
- **Responsible Usage**: Be mindful of disk space usage to ensure fair resource distribution among users.

## Transferring Files

### Using Globus
- **Purpose**: Efficiently transfer files between local systems and W&M clusters. Check out [globus.org](https://www.globus.org/)
- **Usage**:
  ```bash
  # Example command to transfer files using Globus
  globus transfer <source_endpoint> <destination_endpoint>
  ```

## Permissions and Sharing

### Changing Permissions
- **Commands**:
  ```bash
  # Change group ownership
  chgrp <group> <file/directory>

  # Change permissions
  chmod <permissions> <file/directory>
  ```


## Conclusion
Understanding and effectively using the different file systems at William & Mary Research Computing is crucial for efficient and responsible resource usage. For more detailed information, refer to the [Research Computing documentation](https://www.wm.edu/offices/it/services/researchcomputing/using/index.php).


```{admonition} Try this
:class: tip

Can you perform the git exercise here in at one of the HPC systems? Try to create a directory at `sciclone/home/<username>/data10/`
```