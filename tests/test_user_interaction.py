import pytest
from gms import GymMembership
import unittest.mock as mock

@pytest.fixture
def gym_instance():
    """Fixture para crear una instancia de GymMembership"""
    return GymMembership()

def test_confirm_membership_no_confirmation(gym_instance):
    """Prueba de confirmación de membresía cuando el usuario cancela"""
    gym_instance.calculate_total_cost = lambda *args: 100  # Mock del cálculo
    with mock.patch('builtins.input', return_value='no'):
        result = gym_instance.confirm_membership('Basic', [], 1)
        assert result == -1

def test_confirm_membership_yes_confirmation(gym_instance):
    """Prueba de confirmación de membresía cuando el usuario confirma"""
    gym_instance.calculate_total_cost = lambda *args: 100  # Mock del cálculo
    with mock.patch('builtins.input', return_value='yes'):
        result = gym_instance.confirm_membership('Basic', [], 1)
        assert result == 100
