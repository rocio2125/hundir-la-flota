⚓ Hundir la Flota (Battleship)

📋 Descripción del Proyecto
Este proyecto consiste en el desarrollo del clásico juego Hundir la Flota ejecutado en entorno de terminal. Se ha diseñado poniendo especial énfasis en la programación básica de python, la gestión de errores y mediante consola.

El juego enfrenta a un jugador humano contra la máquina con lógica de disparo aleatoria, en un tablero de 10x10 donde la estrategia y la gestión de coordenadas son clave.

🚀 Funcionalidades Principales
Generación Procedural: Colocación aleatoria de barcos asegurando que no se solapen ni se salgan de los límites del tablero.

Motor de Juego: Gestión de turnos dinámicos entre el Usuario y la Máquina.

Sistema de Coordenadas: Validación de inputs para evitar disparos duplicados o fuera de rango.

Interfaz Limpia: Visualización de tableros (propio y de ataque) con actualización en tiempo real de impactos (X) y agua (-).

🛠️ Stack Tecnológico

Lenguaje: Python 3.x.


Librerías utilizadas: random (para la lógica de la máquina), numpy (para la gestión de matrices del tablero).

🏗️ Arquitectura de Código
El proyecto sigue una estructura modular para facilitar su mantenimiento:

Clase Tablero: Gestiona la creación de la malla, la posición de los barcos y el registro de disparos.

Lógica de Barcos: Define las dimensiones y la vida de la flota (Portaviones, Acorazados, Destructores y Fragatas).

Bucle de Juego (Main): Orquesta la lógica de victoria/derrota y el flujo de la partida.

🔧 Instalación y Ejecución
Clona el repositorio:

Bash

git clone https://github.com/rocio2125/hundir-la-flota.git
Navega al directorio:

Bash

cd hundir-la-flota
Ejecuta el juego:

Bash

python main.py
🧠 Desafíos Técnicos y Aprendizaje
Recursividad: Implementación de funciones recursivas para la colocación de barcos hasta encontrar una posición válida.

Manejo de Excepciones: Control de errores de entrada para garantizar que el programa no se detenga ante un input inválido del usuario.

👤 Autora
Rocío Ortiz Gutiérrez

LinkedIn: https://www.linkedin.com/in/rocioortizg/ 
Portfolio/GitHub: https://github.com/rocio2125
