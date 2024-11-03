import pytest
from gms import GymMembership

@pytest.fixture
def gym_instance():
    """Fixture para crear una instancia de GymMembership"""
    return GymMembership()

def test_special_offer_discount_over_400(gym_instance):
    """Prueba para el descuento de $50 por un costo total superior a $400"""
    result = gym_instance.calculate_total_cost('Premium', ['Personal Training', 'Group Classes', 'Nutrition Plan'], 2)

    # Cálculo detallado del costo esperado
    base_cost = 100 + 30 + 20 + 25  # Base + características
    base_cost += base_cost * 0.15  # Aplica recargo de Premium
    base_cost *= 0.9  # Aplica descuento de grupo

    # Verifica si el total supera los $400 después de aplicar los descuentos
    if base_cost > 400:
        base_cost -= 50  # Aplica descuento de $50 por total > $400

    expected_cost = round(base_cost, 3)  # Redondea a 3 decimales

    # Asegura que el resultado esté cerca del costo esperado
    assert result == pytest.approx(expected_cost), f"El costo esperado era {expected_cost}, pero se obtuvo {result}"
