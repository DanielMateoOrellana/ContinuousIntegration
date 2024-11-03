import unittest
import unittest.mock as mock  # Import mock for patching input

class GymMembership:
    def __init__(self):
        # Define the available membership plans and their base costs
        self.membership_plans = {
            'Basic': 50,
            'Premium': 100,
            'Family': 150
        }
        # Define additional features and their respective costs
        self.additional_features = {
            'Personal Training': 30,
            'Group Classes': 20,
            'Nutrition Plan': 25
        }
        # Surcharge percentage for premium plans
        self.premium_surcharge = 0.15

    def display_membership_plans(self):
        # Display all available membership plans and their costs
        print("Available Membership Plans:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")

    def display_additional_features(self):
        # Display all available additional features and their costs
        print("\nAvailable Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")

    def calculate_total_cost(self, base_plan, features, num_members):
        # Get the base cost of the selected membership plan
        base_cost = self.membership_plans.get(base_plan, 0)
        # Calculate the total cost of selected additional features
        features_cost = sum(self.additional_features.get(feature, 0) for feature in features)
        # Calculate the initial total cost
        total_cost = base_cost + features_cost

        # Apply the premium surcharge if the selected plan is 'Premium'
        if base_plan == 'Premium':
            total_cost += total_cost * self.premium_surcharge

        # Apply a 10% discount if there are two or more members
        if num_members >= 2:
            total_cost *= 0.9  # Apply 10% group discount
            print("\nGroup discount of 10% applied.")

        # Apply special offer discounts based on the total cost
        if total_cost > 400:
            total_cost -= 50  # Apply $50 discount for total cost over $400
            print("$50 discount applied for total cost over $400.")
        elif total_cost > 200:
            total_cost -= 20  # Apply $20 discount for total cost over $200
            print("$20 discount applied for total cost over $200.")

        return total_cost

    def confirm_membership(self, base_plan, features, num_members):
        # Calculate the total cost and display the summary
        total_cost = self.calculate_total_cost(base_plan, features, num_members)
        print("\nSummary of your selection:")
        print(f"Selected Plan: {base_plan}")
        print(f"Additional Features: {', '.join(features) if features else 'None'}")
        print(f"Number of Members: {num_members}")
        print(f"Total Cost: ${total_cost}")

        # Ask for user confirmation to proceed
        confirmation = input("\nDo you want to confirm this membership? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            return total_cost
        else:
            print("\nMembership selection canceled.")
            return -1

    def run_program(self):
        # Display membership plans and get user input for plan selection
        self.display_membership_plans()
        base_plan = input("\nSelect a membership plan: ").strip()
        if base_plan not in self.membership_plans:
            print("Invalid membership plan selected.")
            return -1

        # Display additional features and get user input for feature selection
        self.display_additional_features()
        features_input = input("\nSelect additional features (comma-separated, or press Enter to skip): ").strip()
        # Parse the input into a list of features
        features = [feature.strip() for feature in features_input.split(',')] if features_input else []

        # Validate the selected features
        for feature in features:
            if feature and feature not in self.additional_features:
                print(f"Invalid feature selected: {feature}")
                return -1

        # Get and validate the number of members
        try:
            num_members = int(input("\nEnter the number of members: ").strip())
            if num_members < 1:
                raise ValueError("Number of members must be at least 1.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return -1

        # Confirm the membership and display the final cost
        total_cost = self.confirm_membership(base_plan, features, num_members)
        if total_cost != -1:
            print(f"\nMembership confirmed. Final total cost: ${total_cost}")
        else:
            print("\nMembership process was not completed.")