# Sistema de Gestión de Tareas

## Descripción

El **Sistema de Gestión de Tareas** 
es una aplicación diseñada para ayudar a los usuarios a organizar y gestionar sus tareas de manera eficiente. 
El sistema permite realizar operaciones básicas sobre tareas, tales como agregar nuevas tareas, actualizar su descripción y prioridad, 
marcar tareas como completadas, eliminar tareas y listar tanto tareas pendientes como completadas. Está implementado en Python 
y utiliza un enfoque basado en funciones para manejar las operaciones de las tareas.

## Funcionalidades

- **Agregar Tarea:** Permite añadir una nueva tarea al sistema con un identificador único, descripción y prioridad. Lanza un error si la tarea ya existe.
  
- **Actualizar Tarea:** Modifica la descripción y prioridad de una tarea existente. Lanza un error si la tarea no se encuentra en el sistema.

- **Marcar Completada:** Cambia el estado de una tarea a completada. Lanza un error si la tarea no existe.

- **Eliminar Tarea:** Elimina una tarea del sistema. Lanza un error si la tarea no se encuentra en el sistema.

- **Listar Tareas:** Lista todas las tareas pendientes o completadas, según se requiera.

## Manejo de Errores

- Intentar agregar una tarea que ya existe lanza una excepción `ValueError`.
- Intentar actualizar, marcar como completada o eliminar una tarea que no existe lanza una excepción `KeyError`.

## Pruebas Unitarias

El sistema incluye un conjunto de pruebas unitarias escritas con `pytest`, que cubren los siguientes casos:

- Agregar nuevas tareas.
- Actualizar tareas existentes.
- Marcar tareas como completadas.
- Eliminar tareas del sistema.
- Listar tareas según su estado de completitud.
- Verificación del manejo de errores al intentar operar con tareas inexistentes o duplicadas.

## Requisitos del Sistema

- Python 3.x
- `pytest` para ejecutar pruebas unitarias

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tareas.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd tareas
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el sistema de gestión de tareas, ejecuta el script principal:

```bash
python tareas.py
```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
pytest test_tareas.py
```

## Contribución

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request en GitHub. Todas las contribuciones son bienvenidas.
