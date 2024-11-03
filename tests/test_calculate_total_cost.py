import pytest
from gms import GymMembership

@pytest.fixture
def gym_instance():
    """Fixture para crear una instancia de GymMembership"""
    return GymMembership()

def test_calculate_total_cost_basic_plan(gym_instance):
    """Prueba para el cálculo del costo de la membresía 'Basic' sin características adicionales"""
    result = gym_instance.calculate_total_cost('Basic', [], 1)
    assert result == 50

def test_calculate_total_cost_premium_with_features(gym_instance):
    """Prueba para el cálculo del costo de la membresía 'Premium' con características adicionales"""
    result = gym_instance.calculate_total_cost('Premium', ['Personal Training', 'Group Classes'], 1)
    expected_cost = 100 + 30 + 20  # Base cost + features
    expected_cost += expected_cost * 0.15  # Apply 15% premium surcharge
    assert result == pytest.approx(expected_cost)

def test_group_discount_applied(gym_instance):
    """Prueba para verificar si se aplica el descuento de grupo del 10%"""
    result = gym_instance.calculate_total_cost('Family', [], 3)
    assert result == pytest.approx(150 * 0.9)  # 10% de descuento en 150

def test_special_offer_discount_over_400(gym_instance):
    """Prueba para el descuento de $50 por un costo total superior a $400"""
    result = gym_instance.calculate_total_cost('Premium', ['Personal Training', 'Group Classes', 'Nutrition Plan'], 2)
    expected_cost = 100 + 30 + 20 + 25  # Base + características
    expected_cost += expected_cost * 0.15  # Recargo de Premium
    expected_cost *= 0.9  # Descuento de grupo
    expected_cost -= 50  # Descuento de $50
    assert result == pytest.approx(expected_cost)

def test_special_offer_discount_over_200(gym_instance):
    """Prueba para el descuento de $20 por un costo total superior a $200"""
    result = gym_instance.calculate_total_cost('Family', ['Personal Training', 'Nutrition Plan'], 1)
    assert result == pytest.approx(150 + 30 + 25 - 20)
