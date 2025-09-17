from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Clase con reglas predefinidas
class RegexRules:
    rules = {
        "numero_entero": r"^[0-9]+$",
        "palabra_minuscula": r"^[a-z]+$",
        "nombre_mayuscula_inicial": r"^[A-Z][a-z]+$",
        "telefono_con_guiones": r"[0-9]{3}-[0-9]{4}-[0-9]{4}",
        "inicio_cadena": r"^",
        "fin_cadena": r"$",
        "conjunto_abc": r"[abc]",
        "digito": r"[0-9]",
        "mayuscula": r"[A-Z]",
        "minuscula": r"[a-z]",
        "no_digito": r"[^0-9]",
        "cero_o_mas": r"a*",
        "uno_o_mas": r"a+",
        "cero_o_una": r"a?",
        "exactamente_n": r"[0-9]{4}",
        "al_menos_n": r"[a-z]{3,}",
        "entre_n_m": r"[0-9]{2,4}",
        "cualquier_caracter": r".",
        "alternativa": r"(perro|gato)",
        "punto_literal": r"\.",
        "grupo_ab": r"(ab)+",
        "binario_3": r"(0|1){3}",
    }

    @classmethod
    def listar_reglas(cls):
        return list(cls.rules.keys())

    @classmethod
    def get_rule(cls, name: str):
        return cls.rules.get(name, None)

    @classmethod
    def get_rule_with_description(cls, name: str):
        descriptions = {
            "numero_entero": "Solo dígitos, sin decimales ni signos",
            "palabra_minuscula": "Solo letras minúsculas",
            "nombre_mayuscula_inicial": "Nombre con inicial mayúscula",
            "telefono_con_guiones": "Teléfono con guiones (000-0000-0000)",
            "inicio_cadena": "Inicio de cadena",
            "fin_cadena": "Fin de cadena",
            "conjunto_abc": "Solo a, b o c",
            "digito": "Cualquier dígito",
            "mayuscula": "Letra mayúscula",
            "minuscula": "Letra minúscula",
            "no_digito": "Cualquier carácter que no sea dígito",
            "cero_o_mas": "Cero o más veces 'a'",
            "uno_o_mas": "Una o más veces 'a'",
            "cero_o_una": "Cero o una vez 'a'",
            "exactamente_n": "Exactamente 4 dígitos",
            "al_menos_n": "Al menos 3 letras minúsculas",
            "entre_n_m": "Entre 2 y 4 dígitos",
            "cualquier_caracter": "Cualquier caracter excepto salto de línea",
            "alternativa": "perro o gato",
            "punto_literal": "Punto literal",
            "grupo_ab": "Repite grupo 'ab'",
            "binario_3": "Cadenas binarias de 3 símbolos",
        }
        pattern = cls.rules.get(name)
        description = descriptions.get(name, "Sin descripción")
        return pattern, description

# Validar si la regex es correcta
def validar_regex(regex):
    try:
        re.compile(regex)
        return True, ""
    except re.error as e:
        return False, str(e)

# Resaltar coincidencias usando re.MULTILINE
def resaltar_coincidencias(texto, regex):
    try:
        coincidencias = list(re.finditer(regex, texto, re.MULTILINE))
        texto_resaltado = texto
        offset = 0
        for match in coincidencias:
            inicio, fin = match.span()
            texto_resaltado = (
                texto_resaltado[:inicio + offset] +
                "<mark>" + texto_resaltado[inicio + offset:fin + offset] + "</mark>" +
                texto_resaltado[fin + offset:]
            )
            offset += 13  # longitud de <mark></mark>
        return texto_resaltado, [m.group() for m in coincidencias]
    except Exception:
        return texto, []

# Ruta principal
@app.route('/')
def index():
    reglas = []
    for nombre in RegexRules.listar_reglas():
        pattern, description = RegexRules.get_rule_with_description(nombre)
        reglas.append({
            'name': nombre,
            'pattern': pattern,
            'description': description
        })
    return render_template('index.html', reglas=reglas)

# Procesar regex
@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.get_json()
    regex = data.get('regex', '')
    texto = data.get('texto', '')

    # Validar regex
    es_valida, error = validar_regex(regex)
    if not es_valida:
        return jsonify({'valid': False, 'error': f'Error en la expresión regular: {error}'})

    # Validar mínimo de líneas
    lineas = texto.split('\n')
    if len(lineas) < 5:
        return jsonify({'valid': False, 'error': 'El texto debe tener al menos 5 líneas.'})

    # Resaltar coincidencias
    texto_resaltado, coincidencias = resaltar_coincidencias(texto, regex)

    return jsonify({
        'valid': True,
        'texto_resaltado': texto_resaltado,
        'coincidencias': coincidencias,
        'total_coincidencias': len(coincidencias)
    })

# Obtener regla por nombre
@app.route('/get_rule/<rule_name>')
def get_rule(rule_name):
    pattern = RegexRules.get_rule(rule_name)
    if pattern:
        return jsonify({'pattern': pattern})
    return jsonify({'error': 'Regla no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
