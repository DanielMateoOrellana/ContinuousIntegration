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
    
    # Base Cost
    base_cost = 100  # Premium plan
    
    # Features Cost
    features_cost = 30 + 20 + 25  # Personal Training + Group Classes + Nutrition Plan
    
    # Total before any discounts or surcharges
    initial_total = base_cost + features_cost
    
    # Premium Surcharge
    premium_surcharge = initial_total * 0.15
    pre_group_discount_total = initial_total + premium_surcharge
    
    # Group Discount
    group_discount = 0.10  # 10%
    after_group_discount = pre_group_discount_total * (1 - group_discount)
    
    # Special Offer Discount
    special_offer_discount = 50 if after_group_discount > 400 else 0
    
    # Expected cost after all discounts and surcharges
    expected_cost = after_group_discount - special_offer_discount
    
    assert result == pytest.approx(expected_cost, abs=0.01)  # Allow for small float comparison error

def test_special_offer_discount_over_200(gym_instance):
    """Prueba para el descuento de $20 por un costo total superior a $200"""
    result = gym_instance.calculate_total_cost('Family', ['Personal Training', 'Nutrition Plan'], 1)
    assert result == pytest.approx(150 + 30 + 25 - 20)
