# welcome-demo 
[![Build Status](https://github.com/infolab-csail/welcome-demo/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/infolab-csail/welcome-demo/actions/workflows/python-package.yml)

Welcome to the InfoLab! Please follow these instructions to get familiar with our lab's Github workflow.

## Steps

1. Clone this repository, `git clone git@github.com:infolab-csail/welcome-demo.git`.
1. The previous step will have cloned the repo into a new subdirectory
named `welcome-demo`. `cd` to it.
1. Create a branch named after yourself, `git checkout -b add-<yourname>-fav-num`.
1. Add your name and favorite number to `numbers.csv`.
  * Your name must start with a capital letter
  * Your favorite number must be a valid int
1. Stage and commit your changes.

   ```
   git add numbers.csv
   git commit -m "Add <your name>'s favorite number"
   git push origin add-<yourname>-fav-num
   ```

   (Hint: For a one-line log message like in this Welcome Demo, `git
   commit -m` is convenient.  However, you should often write longer
   log messages, with an initial subject line and a descriptive body.
   In that case, omit the `-m` option.  Git will open up a text editor
   for you to enter your log message, so that you can edit multi-line
   messages with access to convenient editing commands like filling
   paragraphs.  (You can configure your account to use a different
   editor if you don't like the default editor.)  To submit the log
   message, save the editor buffer and exit in the standard way for
   that editor.)

1. Create a [pull request](https://help.github.com/articles/using-pull-requests/) (PR) with your changes.
1. Wait for [Github Actions](https://github.com/infolab-csail/welcome-demo/actions/workflows/python-package.yml)
checks to pass. If checks fail, your change probably broke the format
of the `numbers.csv` file. Make modifications by pushing more changes
to the `add-<yourname>-fav-num` branch.
1. Request a review from Sue by adding her as a reviewer and an assignee for the PR. If you followed these steps correctly, Sue will say your PR looks good and will assign it back to you. Then, [merge it](https://help.github.com/articles/merging-a-pull-request/) by clicking "Merge pull request".  Since you will not be using this branch for any future commits, delete it by clicking "Delete branch" in the closed PR.

Now that you are familiar with the basics, see [Infolab Github Workflow](https://projects.csail.mit.edu/cgi-bin/wiki/view/Infolab/GithubWorkflow) for some more details about using Git and GitHub well.
