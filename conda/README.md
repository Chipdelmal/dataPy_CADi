# dataPy CADi: Conda Environment

Export:

```bash
conda env export > dataPy.yml
```

Add to the kernels list:

```bash
source activate dataPy
python -m ipykernel install --user --name dataPy
```

Install package:

```bash
pip install pandas
```

Upgrade package:

```bash
pip install --upgrade pandas
```

Uninstall package:

```bash
pip uninstall pandas
```

Create environment from **YML**:

```bash
conda env create -f environment.yml
```

List environments:

```bash
conda list
```

Uninstall environment:

```bash
conda env remove -n dataPy
```
