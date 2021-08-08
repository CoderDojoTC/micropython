# Creating a Conda Environment for MicroPython

Conda is a powerful tool for building consistent and stable Python environments.  These environments include all the Python libraries that you need to be a productive MicroPython developer. Using Conda allows you to keep each of your Python projects cleanly separated.  This may not be important on your 2nd or 3rd Python project, but as you do more Python projects you will benefit from isolated environments that each have their own versions of each Python libraries that will not conflict with each other.

## Getting started
To get started, it is best to go directly to the [Conda web site](https://docs.conda.io/en/latest/#) and follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) for you specific version of your operating system.  There are many variations of installation not just for Windows, Mac and Linux, but each version my had different steps required.

Once you can open a terminal and type in ```conda --version``` you have successfully installed Conda.  For this document we have used conda:

```sh
conda --version
```

which returns:

```
conda 4.10.1
```

## Creating Your Conda Environment

Our fist job is to create a desktop environment that allows us to run Python programs that support the MicroPython development process.  

```sh
conda create -n micropython python=3
```

This process may take about five minutes, since all the most current libraries must be downloaded onto your desktop.  Once this process finsihes you must remember to deactivate your current conda environment (if you have one and then activate your new micropython environment.

## References

## Raspberry Pi Pico Forum on MicroPython Site
[MicroPython Pico Forum](https://forum.micropython.org/viewforum.php?f=21)

### MicroPython PyCopy (pycopy)
[MicroPython PyCopy](https://github.com/pfalcon/pycopy)