# dataPy: [virtualenv](https://virtualenv.pypa.io/en/latest/)

Virtualenv is a lightweight way to create an environment for us to work on. To create an environment, we simply run the following command:

```bash
virtualenv env/dataPy
```

A new feature for portability is the **relocatable** argument, although it's still in experimental phases:

```bash
virtualenv --relocatable env/dataPy
```


The environment will be created in the specified folder (taking the command line location as root). Once we have created our environment, we can activate it with:

```bash
source env/dataPy/bin/activate
# In Windows: \path\to\env\Scripts\activate
```

Once we have finished working, we can deactivate the environment with:

```bash
deactivate
```


For more information on how to use virtualenv, we can go to their [documentation](https://virtualenv.pypa.io/en/latest/userguide/).
