# welcome-demo [![Build Status](https://travis-ci.org/infolab-csail/welcome-demo.svg)](https://travis-ci.org/infolab-csail/welcome-demo)
Welcome to the InfoLab! Please follow these instructions to get familiar with the our lab's Github workflow.

## Steps

1. Clone this repository, `git clone git@github.com:infolab-csail/welcome-demo.git`.
1. Create a branch named after yourself, `git checkout -b <yourname>`.
1. Add your name and favorite number to `numbers.csv`.
  * Your name must start with a capital letter
  * Your favorite number must be a valid int
1. Stage and commit your changes.

   ```
   git add numbers.csv
   git commit -m "Add <your name>'s favorite number"
   git push origin <yourname>
   ```
1. Create a [pull request](https://help.github.com/articles/using-pull-requests/) (PR) with your changes.
1. Wait for [Travis](https://travis-ci.org/infolab-csail/welcome-demo) checks to pass. If the checks fail, your change probably broke the format of the `numbers.csv` file. Make modifications by pushing more changes to the `<yourname>` branch.
1. Assign the PR to Sue. Sue will merge your PR if all checks pass.
