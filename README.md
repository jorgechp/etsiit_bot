# ETSIIT Bot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./License)
[![Releases](https://img.shields.io/github/v/release/jorgechp/etsiit_bot)](https://github.com/jorgechp/etsiit_bot/releases)
![.github/workflows/test.yml](https://github.com/jorgechp/etsiit_bot/workflows/.github/workflows/test.yml/badge.svg?branch=master)
![.github/workflows/lint.yml](https://github.com/jorgechp/etsiit_bot/workflows/.github/workflows/lint.yml/badge.svg?branch=master)

## Descripción

**ETSIIT Bot** es un Bot de Telegram que tiene como finalidad ofrecer
información sobre diferentes servicios y herramientas de la [Escuela Técnica
Superior de Ingenierías Informática y de Telecomunicación
(ETSIIT)](https://etsiit.ugr.es/) de la
[Universidad de Granada](https://www.ugr.es/).

ETSIIT Bot te facilita:

- [x] :bus: Suscribirte a **grupos de Meetup** en los que estés interesado.
- [x] :fork\_and\_knife: Ver desde Telegram el menú de los **Comedores
  Universitarios**, tanto para hoy como para toda la semana.
- [x] :link: Acceder directamente los **enlaces** más relevantes para tu día a
  día en la Universidad (CIGES, Información sobre guías docentes...)
- [x] :newspaper: Suscripción a páginas de noticias de la Universidad, de la
  ETSIIT, [OSL](https://osl.ugr.es/),
  [Delegación de Estudiantes](https://deiit.ugr.es/),
  [Antiguos Estudiantes](https://aesit.es/)...

Este bot está basado en un esqueleto ejemplo del paquete de [Python Telegram
Bot](https://github.com/python-telegram-bot/python-telegram-bot).

Para más información, échale un vistazo a la [Wiki del
proyecto](https://github.com/jorgechp/etsiit_bot/wiki).

## Ejecutar test y pasar la prueba del algodón

Para la automatización del proyecto utilizamos
[`nox`](https://github.com/theacodes/nox), herramienta la cual se puede
instalar ejecutando:

```bash
pip install nox
```

Una vez instalado, es posible ver una lista de opciones disponibles con el
siguiente comando:

```bash
nox -l
```

Ahora, para ejecutar las herramientas de linting sobre el código de Python:

```bash
nox -e lintpy
```

Si queremos pasar la herramienta de lint para los archivos Markdown es
necesario instalar el siguiente paquete de ruby:
[gem](https://github.com/markdownlint/markdownlint). Para ello escribimos lo
siguiente en el intérprete de órdenes:

```bash
gem install mdl
```

Finalmente para usar el linter de Markdown:

```bash
nox -e lintmd
```

Si queremos correr los tests podemos introducir el siguiente comando:

```bash
nox -e test
```

