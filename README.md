# 💻 MDT-text-data-mining

:id: _[@00santiagob](https://github.com/00santiagob)_

## Resumen

Este repositorio sirve para la materia **_Mineria de Datos de Texto_** dictada en el *FaMAF - UNC*.
Para dicha materia se realizo la guía **_spaCy 101_** la cual incluye el curso iterativo **_Advanced NLP with SpaCy_** al cual se le designo un apartado especial.

## :wrench: Requerimientos

* Para instalar los paquetes recomiendo usar **_venv_**.

```bash
pip install -U pip setuptools wheel
git clone https://www.github.com/00santiagob/ML-NLP-PYTHON
cd ML-NLP-PYTHON
python3 -m venv env
source env/bin/activate
```

> Si no esta instalado, puedes hacerlo con el comando `pip install venv`

* Los paquetes que nos interesa instalar son: **_NumPy_**, **_SciPy_**, **_Scikit-Learn_**, **_MatplotLib_**, **_Pandas_** y **_SpaCy_**.

```bash
python3 -m pip install -r requirements.txt
pip install --no-build-isolation --editable .
```

> **Nota:** Para instalar algun paquete extra de **_SpaCy_**: `pip install --no-build-isolation --editable .[lookups,cuda102]`
>
> **Recomiendo:** Correr el comando `python -m spacy validate` para verificar que todos los paquetes instalados son compatibles con la version instalada de **_SpaCy_**.

## :pushpin: Tips

* Usar la GPU para el paquete *SpaCy*:

  ```python
  import spacy
  spacy.prefer.gpu()
  nlp = spacy.load("es_core_web_sm")
  ```
