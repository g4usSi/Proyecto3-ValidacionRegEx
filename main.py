import re

class RegexRules:

    rules = {
        # Ejemplos prácticos del documento
        "numero_entero": r"^[0-9]+$",                  # Solo dígitos, sin decimales ni signos
        "palabra_minuscula": r"^[a-z]+$",              # Solo letras minúsculas
        "nombre_mayuscula_inicial": r"^[A-Z][a-z]+$",  # Nombre con inicial mayúscula
        "telefono_con_guiones": r"[0-9]{3}-[0-9]{4}-[0-9]{4}",  # Teléfono con guiones

        # Ejemplos de reglas generales
        "inicio_cadena": r"^",              # Inicio de cadena
        "fin_cadena": r"$",                 # Fin de cadena
        "conjunto_abc": r"[abc]",           # Solo a, b o c
        "digito": r"[0-9]",                 # Cualquier dígito
        "mayuscula": r"[A-Z]",              # Letra mayúscula
        "minuscula": r"[a-z]",              # Letra minúscula
        "no_digito": r"[^0-9]",             # Cualquier carácter que no sea dígito
        "cero_o_mas": r"a*",                # Cero o más veces "a"
        "uno_o_mas": r"a+",                 # Una o más veces "a"
        "cero_o_una": r"a?",                # Cero o una vez "a"
        "exactamente_n": r"[0-9]{4}",       # Exactamente 4 dígitos
        "al_menos_n": r"[a-z]{3,}",         # Al menos 3 letras minúsculas
        "entre_n_m": r"[0-9]{2,4}",         # Entre 2 y 4 dígitos
        "cualquier_caracter": r".",         # Cualquier caracter excepto salto de línea
        "alternativa": r"(perro|gato)",     # perro o gato
        "punto_literal": r"\.",             # Punto literal
        "grupo_ab": r"(ab)+",               # Repite grupo "ab"
        "binario_3": r"(0|1){3}",           # Cadenas binarias de 3 símbolos
    }

    @classmethod
    def listar_reglas(cls):
        return list(cls.rules.keys())

    @classmethod
    def get_rule(cls, name: str):
        return cls.rules.get(name, None)


def validar_regex(regex):
    try:
        re.compile(regex)
        return True, ""
    except re.error as e:
        return False, str(e)


def resaltar_coincidencias(texto, regex):
    coincidencias = list(re.finditer(regex, texto))
    texto_resaltado = texto
    offset = 0
    for match in coincidencias:
        inicio, fin = match.span()
        texto_resaltado = (
                texto_resaltado[:inicio + offset] +
                "[" + texto_resaltado[inicio + offset:fin + offset] + "]" +
                texto_resaltado[fin + offset:]
        )
        offset += 2  # por los corchetes añadidos
    return texto_resaltado, [m.group() for m in coincidencias]


def main():

    listar = input("¿Deseas ver la lista de reglas predefinidas? (s/n): ").strip().lower()
    if listar == 's':
        print("Reglas predefinidas:")
        for nombre in RegexRules.listar_reglas():
            print(f"- {nombre}: {RegexRules.get_rule(nombre)}")
    print("\n")

    regex = input("> Ingresa una expresión regular: ")
    es_valida, error = validar_regex(regex)
    if not es_valida:
        print(f"Error en la expresión regular: {error}")
        return

    print("Ingresa el texto (minimo 5 líneas). Finaliza con una línea vacía:")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    texto = "\n".join(lineas)

    if len(lineas) < 5:
        print("El texto debe tener al menos 5 lineas.")
        return

    texto_resaltado, coincidencias = resaltar_coincidencias(texto, regex)

    print("\nTexto con coincidencias resaltadas:")
    print(texto_resaltado)
    print("\n Lista de coincidencias encontradas:")
    print(coincidencias)


if __name__ == "__main__":
    main()

class RegEx:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, string):
        return string == self.pattern

    def patern(self):
        return self.pattern
