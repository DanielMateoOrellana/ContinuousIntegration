import pytest
from gms import GymMembership

@pytest.fixture
def gym_instance():
    """Fixture para crear una instancia de GymMembership"""
    return GymMembership()

def test_invalid_plan(gym_instance):
    """Prueba para un plan de membresía no válido"""
    result = gym_instance.calculate_total_cost('InvalidPlan', [], 1)
    assert result == 0  # Debe devolver 0 para un plan no válido

def test_invalid_feature_selection(gym_instance):
    """Prueba para la selección de una característica adicional no válida"""
    with pytest.raises(KeyError):
        gym_instance.additional_features['InvalidFeature']
