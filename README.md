![build](https://github.com/fissoreg/timefunc-prep/actions/workflows/build.yml/badge.svg)

# timefunc-prep
A simple benchmarking function.

# Usage

To measure execution time of `print("Hello world!")`:

```python
from timefunc.time_func import time_func

time_func(print, "Hello world!")
```

# Setting up the environment

```
$ cd *path_to*/timefunc-package
$ python -m venv env
```

# Activating the environment

Always use this environment when developing the package.
Activate the venv from the `timefunc-package` directory.
```
$ . venv/bin/activate
```

# Packaging

Execute this in the directory that should be packaged (which contains the `pyproject.toml` file):
```
$ flit init
```

# Installing

The `-s` argument symlinks the package, so that modifications are loaded without reinstalling. Useful for development.

```
$ flit install -s --env 
```
