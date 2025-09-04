import re


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
    regex = input("Ingresa una expresión regular: ")
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
== == == =

class RegEx:
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, string):
        return string == self.pattern

    def patern(self):
        return self.pattern
