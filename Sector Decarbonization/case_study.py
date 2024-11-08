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

# Original electric stove scenario (calculated previously)
electric_stove_energy = total_energy_usage / 1000  # in kWh

# Gas stove energy calculation
# Total time for all foods in hours (sum of individual times from earlier calculation)
# We assume gas stove usage is equivalent to 2.64 kWh per hour per burner
# https://www.hunker.com/13408239/typical-btus-of-a-gas-stove/
total_gas_stove_energy = 2.64 * (electric_stove_energy / 2.4)  # Scaling according to BTU vs Electric use

# Induction stove energy calculation
# Equivalent energy use assumed at 2.0 kWh per hour
total_induction_stove_energy = 2.0 * (electric_stove_energy / 2.4)  # Scaling for similar heat output as electric

# Data for plotting
stove_types = ['Electric Stove', 'Gas Stove', 'Induction Stove']
energy_usage_kwh = [electric_stove_energy, total_gas_stove_energy, total_induction_stove_energy]

# Plotting the comparison
plt.figure(figsize=(8, 6))
plt.bar(stove_types, energy_usage_kwh, color=['blue', 'orange', 'green'])
plt.title('Energy Usage Comparison for Different Stove Types')
plt.xlabel('Stove Type')
plt.ylabel('Total Energy Usage (kWh)')
plt.show()