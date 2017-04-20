To execute the cells in foo.ipynb:
```sh
jupyter nbconvert foo.ipynb --to notebook --execute
```

This will create a file called foo.nbconvert.ipynb which includes the output.

To run a slideshow (including output)
```sh
jupyter nbconvert foo.nbconvert.ipynb --to slides --post serve
```
