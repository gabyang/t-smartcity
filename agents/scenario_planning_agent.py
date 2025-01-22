import numpy as np
import logging

class DeepScenarioPlanning:
    def __init__(self, base_scenario):
        self.base_scenario = base_scenario
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def generate_random_scenarios(self, num_scenarios=5):
        """
        Generate random scenarios by tweaking the base values.
        """
        scenarios = []
        logging.info(f"Generating {num_scenarios} random scenarios.")
        for _ in range(num_scenarios):
            scenario = {key: value * (1 + np.random.uniform(-0.2, 0.2)) for key, value in self.base_scenario.items()}
            scenarios.append(scenario)
        return scenarios

    def run_scenario(self, scenario, factors):
        """
        Simulate the outcome based on multiple factors.
        """
        logging.info("Running scenario with given factors.")
        outcome = sum(scenario[factor] * weight for factor, weight in factors.items())
        return outcome

if __name__ == "__main__":
    base = {"GDP": 1000, "Population": 1000000, "Transport": 500}
    planner = DeepScenarioPlanning(base)
    scenarios = planner.generate_random_scenarios()
    outcome = planner.run_scenario(scenarios[0], {"GDP": 0.5, "Population": 0.3, "Transport": 0.2})
    print("Generated Scenarios:\n", scenarios)
    print("Scenario Outcome:\n", outcome)