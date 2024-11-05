"""Gym Membership System for managing plans, features, and total cost calculations."""

class GymMembership:
    """Class for managing membership plans and costs in a gym."""

    def __init__(self):
        """Initializes membership plans and additional features."""
        self.membership_plans = {
            'Basic': 50,
            'Premium': 100,
            'Family': 150
        }
        self.additional_features = {
            'Personal Training': 30,
            'Group Classes': 20,
            'Nutrition Plan': 25
        }
        self.premium_surcharge = 0.15

    def display_membership_plans(self):
        """Displays all available membership plans and their costs."""
        print("Available Membership Plans:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")

    def display_additional_features(self):
        """Displays all available additional features and their costs."""
        print("\nAvailable Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")

    def calculate_total_cost(self, base_plan, features, num_members):
        """Calculates the total cost of membership, including plans, features, and discounts."""
        base_cost = self.membership_plans.get(base_plan, 0)
        features_cost = sum(self.additional_features.get(feature, 0) for feature in features)
        total_cost = base_cost + features_cost

        if base_plan == 'Premium':
            total_cost += total_cost * self.premium_surcharge

        if num_members >= 2:
            total_cost *= 0.9  # Apply 10% group discount
            print("\nGroup discount of 10% applied.")

        if total_cost > 400:
            total_cost -= 50
            print("$50 discount applied for total cost over $400.")
        elif total_cost > 200:
            total_cost -= 20
            print("$20 discount applied for total cost over $200.")

        return round(total_cost, 3)

    def confirm_membership(self, base_plan, features, num_members):
        """Confirms the membership after calculating the total cost."""
        total_cost = self.calculate_total_cost(base_plan, features, num_members)
        print("\nSummary of your selection:")
        print(f"Selected Plan: {base_plan}")
        print(f"Additional Features: {', '.join(features) if features else 'None'}")
        print(f"Number of Members: {num_members}")
        print(f"Total Cost: ${total_cost}")

        confirmation = input(
            "\nDo you want to confirm this membership? (yes/no): "
        ).strip().lower()
        if confirmation == 'yes':
            return total_cost
        print("\nMembership selection canceled.")
        return -1  # Return -1 for consistency

    def run_program(self):
        """Runs the membership management program,
        interacting with the user to select plans and features."""
        self.display_membership_plans()
        base_plan = input("\nSelect a membership plan: ").strip()
        if base_plan not in self.membership_plans:
            print("Invalid membership plan selected.")
            return -1

        self.display_additional_features()
        features_input = input(
            "\nSelect additional features (comma-separated, or press Enter to skip): "
        ).strip()
        features = [feature.strip() for feature in features_input.split(',')
                    ] if features_input else []

        for feature in features:
            if feature and feature not in self.additional_features:
                print(f"Invalid feature selected: {feature}")
                return -1

        try:
            num_members = int(input("\nEnter the number of members: ").strip())
            if num_members < 1:
                raise ValueError("Number of members must be at least 1.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return -1

        total_cost = self.confirm_membership(base_plan, features, num_members)
        if total_cost != -1:
            print(f"\nMembership confirmed. Final total cost: ${total_cost}")
            return total_cost  # Return total cost for successful confirmation

        print("\nMembership process was not completed.")
        return -1  # Return -1 for consistency in all paths


if __name__ == "__main__":
    # Create an instance of GymMembership and run the program
    gym_membership = GymMembership()
    gym_membership.run_program()
