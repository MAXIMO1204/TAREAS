import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, eliminar_tarea, listar_tareas, Tarea

@pytest.fixture
def tareas_vacias():
    """Crea un diccionario de tareas vacío para usar en las pruebas."""
    return {}

@pytest.fixture
def tareas_de_ejemplo():
    """Crea un diccionario de tareas con algunos datos de ejemplo."""
    tareas = {}
    agregar_tarea(tareas, '1', 'Tarea 1', 'Alta')
    agregar_tarea(tareas, '2', 'Tarea 2', 'Media')
    return tareas

def test_agregar_tarea_exitoso(tareas_vacias):
    """Prueba agregar una tarea exitosamente."""
    agregar_tarea(tareas_vacias, '1', 'Tarea de prueba', 'Alta')
    assert '1' in tareas_vacias
    assert tareas_vacias['1'].descripcion == 'Tarea de prueba'
    assert tareas_vacias['1'].prioridad == 'Alta'
    assert not tareas_vacias['1'].completada

def test_agregar_tarea_id_duplicado(tareas_de_ejemplo):
    """Prueba que agregar una tarea con ID duplicado lanza un ValueError."""
    with pytest.raises(ValueError):
        agregar_tarea(tareas_de_ejemplo, '1', 'Otra tarea', 'Baja')

def test_actualizar_tarea_exitoso(tareas_de_ejemplo):
    """Prueba actualizar una tarea exitosamente."""
    actualizar_tarea(tareas_de_ejemplo, '1', 'Tarea actualizada', 'Baja')
    assert tareas_de_ejemplo['1'].descripcion == 'Tarea actualizada'
    assert tareas_de_ejemplo['1'].prioridad == 'Baja'

def test_actualizar_tarea_no_existente(tareas_de_ejemplo):
    """Prueba que actualizar una tarea inexistente lanza un KeyError."""
    with pytest.raises(KeyError):
        actualizar_tarea(tareas_de_ejemplo, '3', 'Tarea nueva', 'Alta')

def test_marcar_completada_exitoso(tareas_de_ejemplo):
    """Prueba marcar una tarea como completada exitosamente."""
    marcar_completada(tareas_de_ejemplo, '1')
    assert tareas_de_ejemplo['1'].completada

def test_marcar_completada_no_existente(tareas_de_ejemplo):
    """Prueba que marcar una tarea inexistente lanza un KeyError."""
    with pytest.raises(KeyError):
        marcar_completada(tareas_de_ejemplo, '3')

def test_eliminar_tarea_exitoso(tareas_de_ejemplo):
    """Prueba eliminar una tarea exitosamente."""
    eliminar_tarea(tareas_de_ejemplo, '1')
    assert '1' not in tareas_de_ejemplo

def test_eliminar_tarea_no_existente(tareas_de_ejemplo):
    """Prueba que eliminar una tarea inexistente lanza un KeyError."""
    with pytest.raises(KeyError):
        eliminar_tarea(tareas_de_ejemplo, '3')

def test_listar_tareas_pendientes(tareas_de_ejemplo, capsys):
    """Prueba listar tareas pendientes."""
    listar_tareas(tareas_de_ejemplo, completadas=False)
    captured = capsys.readouterr()
    assert "Tarea 1" in captured.out
    assert "Tarea 2" in captured.out

def test_listar_tareas_completadas(tareas_de_ejemplo, capsys):
    """Prueba listar tareas completadas."""
    marcar_completada(tareas_de_ejemplo, '1')
    listar_tareas(tareas_de_ejemplo, completadas=True)
    captured = capsys.readouterr()
    assert "Tarea 1" in captured.out
    assert "Tarea 2" not in captured.out
