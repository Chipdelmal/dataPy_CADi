# dataPy: Environments

Virtual environments attempt to solve a variety of problems that arise when working in several programming projects at the same time. In this section of our bootcamp we will go through some of these uses and we will setup the environment that we will be using for the rest of the workshop.

<hr>

## What is an environment and why should I use one?

There are various reasons to use environments, most of which relate to "good practices" in coding.

###  Packages "Hygene"

One of Python's greatest strengths is the availability of community packages to tackle a wide variety of scientific/engineering tasks. This, however, leads to an unintended problem: **What happens when some of my packages require different versions other packages? (or even different versions of Python)**

For example, if we create our own package that requires [numpy](https://www.numpy.org/), but the developers are announcing some upcoming changes that might break the functionality of my code; how can we ensure that our package will continue to work if I update [numpy](https://www.numpy.org/) to work in another project in my computer?

Environments solve this problem in an elegant way by providing "workspaces" within our system in which we can install/uninstall packages without affecting the dependencies of other projects we might be working on.

### Portability

Another problem environments address is the "shipping" of our code. This is: **How do I share my code with collaborators and users without them having to install and figure out packages dependencies by themselves?**

By creating a virtual environment, we are already making sure that we have everything necessary to run our code, so we can simply share it with our collaborators for them to be able to run the code too.


### Reproducibility

Paramount in science, reproducibility is a must for any kind of publication. Providing a self-contained environment can ensure that any interested reader can run our code.

<hr>

## Exercises

##  [Exercise 1: Creating an environment with virtualenv](./virtualenv.md)

##  [Exercise 2: Creating an environment with anaconda](./anaconda.md)
