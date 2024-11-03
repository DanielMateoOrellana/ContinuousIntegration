from gms import GymMembership

def test_display_membership_plans(capsys):
    """Prueba de visualización de los planes de membresía"""
    gym = GymMembership()
    gym.display_membership_plans()
    captured = capsys.readouterr()
    assert "Basic: $50" in captured.out
    assert "Premium: $100" in captured.out
    assert "Family: $150" in captured.out

def test_display_additional_features(capsys):
    """Prueba de visualización de las características adicionales"""
    gym = GymMembership()
    gym.display_additional_features()
    captured = capsys.readouterr()
    assert "Personal Training: $30" in captured.out
    assert "Group Classes: $20" in captured.out
    assert "Nutrition Plan: $25" in captured.out
