from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None
    estado = None
    
    if request.method == 'POST':
        try:
            nota1 = float(request.form.get('nota1'))
            nota2 = float(request.form.get('nota2'))
            nota3 = float(request.form.get('nota3'))
            asistencia = float(request.form.get('asistencia'))
            
            # Validar rangos
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                resultado = "Error: Las notas deben estar entre 10 y 70"
            elif not (0 <= asistencia <= 100):
                resultado = "Error: La asistencia debe estar entre 0 y 100"
            else:
                # Calcular promedio
                promedio = (nota1 + nota2 + nota3) / 3
                
                # Determinar estado
                if promedio >= 40 and asistencia >= 75:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"
                
                resultado = f"Promedio: {promedio:.2f}"
        except (ValueError, TypeError):
            resultado = "Error: Por favor ingrese valores numéricos válidos"
    
    return render_template('ejercicio1.html', resultado=resultado, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    nombre_largo = None
    cantidad_caracteres = None
    
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()
        
        if not nombre1 or not nombre2 or not nombre3:
            resultado = "Error: Por favor complete todos los nombres"
        else:
            # Encontrar el nombre más largo
            nombres = [
                (nombre1, len(nombre1)),
                (nombre2, len(nombre2)),
                (nombre3, len(nombre3))
            ]
            
            nombre_mas_largo = max(nombres, key=lambda x: x[1])
            nombre_largo = nombre_mas_largo[0]
            cantidad_caracteres = nombre_mas_largo[1]
    
    return render_template('ejercicio2.html', 
                         nombre_largo=nombre_largo, 
                         cantidad_caracteres=cantidad_caracteres,
                         resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
