# dataPy: [Git](https://git-scm.com/) and [Github](https://github.com/)

Git is, first and foremost, a [version control](https://en.wikipedia.org/wiki/Version_control) system. But what is a [version control](https://en.wikipedia.org/wiki/Version_control) system?

We've all been in a situation in which we are working in a document/code and we make changes but we still want to keep a copy of the previous state of the file in case something goes wrong. So what do we do? We usually try to keep track of the files by adding version numbers, but it usually takes just a couple of days for this system to start showing it's deficiencies: it's difficult to standardize/enforce. Even worse, in coding we usually work with several different files at the same time, which makes the manual system impossible to maintain in the long run.

[<img src="./media/phdTracking.png" width="50%">](https://twitter.com/phdcomics/status/826861642507882496?lang=en)

This is why, [git](https://git-scm.com/) exists: *To make persistent copies of the history of our source files so that we can always go back to a previously working version*.

<hr>

##  [Git](https://git-scm.com/)

[Git](https://git-scm.com/) is, as mentioned before, the most popular distributed version control system.

### Brief History


### Advantages

* **It's decentralized:** There is no central server where all the information is stored and "checked-out". Instead, everyone involved keeps a full copy of the
* **It's widely supported:** All major operating systems support git (Linux and MacOS can run it from the terminal "out of the box").
* **It has a large community:** If you find yourself ever having questions, there's always someone willing to answer it. Alternatively, there are lots of [books](https://git-scm.com/book/en/v2) and [online resources](https://swcarpentry.github.io/git-novice-es/).
* **It's relatively simple to use:** With some practice, everyone can learn the fundamentals of git and leverage it's benefits.
* **Colaboration:**

<hr>

##  [GitHub](www.github.com)

[GitHub](www.github.com) is the most popular web-based [version control](https://en.wikipedia.org/wiki/Version_control) service that uses the [git](https://git-scm.com/) protocol (it is so popular that git and github are colloquially used as synonims). It is very popular for programming projects due to its ability to provide access control, bug tracking, wikis, feature requests, amongst many other features.

<hr>

##  Exercise

###  Setup

```bash
git config --global user.name "MY_USERNAME"
git config --global user.email "MY_EMAIL@DOMAIN.COM"
git config --global core.editor "nano -w"
```

### Creating a Github Repo

<img src="./media/git01.png" width="50%">


<img src="./media/git02.png" width="50%">


### Linking to a [Github](https://github.com/) Repo

```bash
git init
git remote add origin https://github.com/Chipdelmal/helloGit.git
git remote -v
git pull origin master
```

### Creating a file

```bash
nano trackMe.py
```

### Staging and Committing

```bash
git status
git add trackMe.py
git status
git commit -m "Created a 'Hello World' file."
git push origin master
```

### Making Changes

```bash
nano trackMe.py
git add *
git commit -m "Repeating the message 8 times."
git push origin master
```

### Ignoring Files and Folders

```bash
nano .gitignore
git add *
git commit -m "Adding gitignore."
git log --oneline --graph --all --decorate
```

### Restoring to a previous state

```bash
git checkout LOG_ID trackMe.py
git commit -m "Reverting to a previous state."
git push origin master
```

<hr>

##  A More Detailed Explanation


<hr>

##  Collaborating

<hr>

## Other Resources

* [Git Carpentry Workshop](https://swcarpentry.github.io/git-novice-es/)
* ["Pro Git" Free Download Book](https://git-scm.com/book/en/v2)
