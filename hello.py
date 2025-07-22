#!/c/Users/bruno/AppData/Local/Programs/Python/Python313/python
"""Hello World Multi Language Program.
Depending on the language, it will print "Hello World!" in different languages.

How to run:
Tenha a variavel LANG devidamente configurada ex:
export LANG=en_US.UTF-8

Execução:
python3 hello.py or ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Bruno Alberto Spigariol"
__license__ = "Unlicense"

# Dunder
import os

current_language = os.getenv("LANG","en_US")[:5]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour le monde!"
elif current_language == "es_ES":
    msg = "¡Hola Mundo!"

print (msg)
