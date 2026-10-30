# Tema 1 - Chuleta de entorno

## 1. Crear y ejecutar un .py (ejercicio "Hola, Mundo" del profesor)
1. En VS Code: Archivo > Nuevo archivo > guárdalo como `hola_mundo.py` (la extensión `.py` es obligatoria).
2. Escribe: `print("¡Hola, Mundo!")`
3. Abre la terminal integrada: **Ctrl + ñ** (o menú Terminal > Nuevo terminal).
4. Ejecuta, situada en la carpeta del archivo:

| Sistema | Orden |
|---|---|
| Windows / macOS | `python hola_mundo.py` |
| Linux / Ubuntu / WSL / Docker | `python3 hola_mundo.py`  (el profesor lo EXIGE en Linux) |

- `python --version` / `python3 --version` -> comprueba qué versión tienes (match-case necesita 3.10+).
- `python` sin archivo abre el intérprete interactivo (REPL, prompt `>>>`). Sal con `exit()`.
- Si dice "No such file": no estás en la carpeta. Muévete con `cd carpeta`, mira dónde estás con `pwd` (Linux) o `cd` (Windows), lista con `ls` (o `dir` en cmd).

## 2. pip y uv (instalar librerías)
- `pip install requests` (en Linux `pip3`, o mejor `python3 -m pip install requests`).
- `pip list` -> qué hay instalado. `pip freeze > requirements.txt` -> guardar dependencias. `pip install -r requirements.txt` -> instalarlas.
- `uv` es un gestor moderno y muy rápido: `uv venv`, `uv pip install requests`, `uv run archivo.py`.
- En el examen NO hay internet: usa solo la biblioteca estándar.

## 3. Entorno virtual (venv)
```bash
python -m venv .venv              # crear (Linux: python3 -m venv .venv)
.venv\Scripts\activate            # activar en Windows
source .venv/bin/activate         # activar en Linux / macOS / WSL
deactivate                        # salir
```
Sirve para que cada proyecto tenga sus propias librerías sin mezclarse. Al activarlo, el prompt muestra `(.venv)`.

## 4. Docker y WSL (básico)
- **WSL** = Linux (Ubuntu) dentro de Windows. Abrir: `wsl` en la terminal. Ahí se usa `python3`.
- **Regla de oro del profesor**: guarda los proyectos SIEMPRE en el home de Linux (`~/` o `~/proyectos_clase`) y NUNCA en `/mnt/c/Users/...` (Escritorio, Documentos), porque con Docker/WSL2 el rendimiento cae muchísimo.
- **Docker**: `docker ps` (contenedores en marcha), `docker run -it python:3.12 bash` (contenedor con Python), `docker compose up -d` (levantar el proyecto), `docker exec -it nombre bash` (entrar en un contenedor).
- **Prompt con la ruta (PS1)**: para ver el directorio actual en la terminal de Ubuntu se modifica la variable de entorno `PS1` dentro de `~/.bashrc`. Ejemplo: añadir al final `export PS1='\u@\h:\w\$ '` (`\w` = ruta actual) y recargar con `source ~/.bashrc`.

## 5. `if __name__ == "__main__":`
```python
def saludar(nombre):
    """Devuelve un saludo."""
    return f"Hola, {nombre}"

if __name__ == "__main__":      # solo se ejecuta si lanzas ESTE archivo directamente
    print(saludar("Ana"))
```
- Si ejecutas `python archivo.py`, `__name__` vale `"__main__"` y se ejecuta el bloque.
- Si otro archivo hace `import archivo`, `__name__` vale `"archivo"` y el bloque NO se ejecuta (así las pruebas no se disparan al importar).
- Equivale al `public static void main(String[] args)` de Java.
- Funciones y clases: pon las pruebas siempre dentro de este bloque.

## 6. Diferencias rápidas con Java
- Sin `;` ni llaves: los bloques se marcan con `:` y **4 espacios** de sangría.
- Sin tipos al declarar: `edad = 18`. `input()` devuelve SIEMPRE `str` -> convierte con `int()` / `float()`.
- `&&`, `||`, `!` -> `and`, `or`, `not`. `true/false/null` -> `True/False/None`.
