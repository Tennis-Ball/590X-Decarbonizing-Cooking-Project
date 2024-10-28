import matplotlib.pyplot as plt

# Define the power ratings for stove and microwave
stove_power = 2400  # in watts
microwave_power = 1000  # in watts

# Cooking details in a dictionary for each food item
# Each item contains: [time in minutes, time in seconds, heat level, appliance]
cooking_data = {
    "Bacon": [7, 6, 0.6, stove_power],
    "Eggs": [3, 9, 0.5, stove_power],
    "Eggos": [1, 0, 1.0, microwave_power],
    "Steak": [7, 5, 0.7, stove_power],
    "Pasta+Veggies": [37, 12, 0.8, stove_power],
    "Tomato Sauce": [1, 0, 1.0, microwave_power],
}

# Calculate the energy used (in kWh) for each item
energy_usage = {}

for item, (minutes, seconds, heat_fraction, power_rating) in cooking_data.items():
    # Convert cooking time to hours
    time_hours = (minutes + seconds / 60) / 60
    # Calculate effective power usage considering the heat level
    effective_power = power_rating * heat_fraction
    # Calculate energy consumption in kWh
    energy_kwh = effective_power * time_hours
    energy_usage[item] = energy_kwh

# Sum total energy usage
total_energy_usage = sum(energy_usage.values())

# Additional power consumption assumptions
gas_power_per_minute = 0.18 * 60  # Convert to watts (0.18 kWh per minute)
induction_efficiency = 0.85  # Induction efficiency factor

# Calculate energy usage for Gas and Induction stoves
energy_usage_gas = {}
energy_usage_induction = {}

for item, (minutes, seconds, heat_fraction, power_rating) in cooking_data.items():
    # Convert time to hours
    time_hours = (minutes + seconds / 60) / 60
    # Calculate effective power for gas and induction stoves
    # Gas: based on average energy per minute
    gas_energy = gas_power_per_minute * (minutes + seconds / 60) * heat_fraction  # in watt-hours
    # Induction: use efficiency adjustment on electric stove power
    induction_energy = (power_rating * heat_fraction * induction_efficiency) * time_hours  # in watt-hours
    energy_usage_gas[item] = gas_energy
    energy_usage_induction[item] = induction_energy

# Calculate total energy usage for Gas and Induction scenarios
total_energy_gas = sum(energy_usage_gas.values())
total_energy_induction = sum(energy_usage_induction.values())

# Data for bar graph
energy_totals = {
    "Electric Stove": total_energy_usage,
    "Gas Stove": total_energy_gas,
    "Induction Stove": total_energy_induction
}

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(energy_totals.keys(), energy_totals.values(), color=['blue', 'green', 'orange'])
plt.xlabel("Cooking Method")
plt.ylabel("Total Energy Usage (Wh)")
plt.title("Comparison of Energy Usage by Cooking Method")
plt.show()
