# pelonalysis

This is a very limited set of analytics for Peloton data.  I made this primarily to analyze weekly effort to understand the effect on my performance. Use at your own risk.  I likely won't maintain this repo... sorry!

## Checkout this repo

```
cd /path/to/src
git clone https://github.com/tbreloff/pelonalysis.git
```

## Setup your python environment

Use Conda or Pip to install pandas and matplotlib.

## Download your data

Log in to your Peloton account from your computer, go to `Profile --> Workouts`, and then click on the `Download Workouts` button at the top of the screen.  This should trigger the downloading of a CSV file to your computer.  Copy that file to `pelonalysis/data/data.csv` (or pass your filename into the `load_dataframe` method).

## Run the notebook

Do you want to look at your weekly output, just like I did? Great! Just open and run all cells in `notebooks/peloton.ipynb`.

## Do your own analysis

If you want to dig into the numbers yourself, please feel free to look at the methods in `pelonalysis/__init__.py` and adjust/improve to your liking.  I'm happy to accept PRs for analytics or visualizations to include.
