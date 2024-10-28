# cSpell: disable
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def extract_b13(file_path):
    df = pd.read_excel(f"sheets/{file_path}.xlsx", sheet_name='data')  # Replace 'Sheet1' if needed

    data = df.iloc[:, [0, 2]]

    # Process data into a nested dictionary structure
    json_data = {}
    current_key = None

    for _, row in data.iterrows():
        col_a_value = str(row.iloc[0])
        col_c_value = str(row.iloc[1]) if not pd.isna(row.iloc[1]) else None

        if col_c_value:
            # If there's a value in Column C, add it as a key-value pair under the main json_data
            if current_key:
                json_data[current_key][col_a_value] = col_c_value
            else:
                json_data[col_a_value] = col_c_value
        else:
            # If no value in Column C, create a new nested dictionary under col_a_value key
            current_key = col_a_value
            json_data[current_key] = {}

    # Save json_data to json file
    json_file_path = f"{file_path}.json"
    with open(json_file_path, 'w') as json_file:
        import json
        json.dump(json_data, json_file, indent=4)

def graph_type_1(file_path, title):
    data = pd.read_csv(file_path)

    plt.figure(figsize=(10, 6))
    categories = ['2003', '2012', '2018']
    num_categories = len(categories)
    x = np.arange(num_categories)
    bar_width = 0.25

    electricity = data.loc[0:2, 'Electricity']
    natural_gas = data.loc[0:2, 'Natural Gas']
    propane = data.loc[0:2, 'Propane']

    plt.bar(x - bar_width, electricity, width=bar_width, label='Electricity', color='orange')
    plt.bar(x, natural_gas, width=bar_width, label='Natural Gas', color='brown')
    plt.bar(x + bar_width, propane, width=bar_width, label='Propane', color='blue')

    # Add labels and title
    plt.xlabel('Years', fontweight='bold')
    plt.ylabel('Proportion', fontweight='bold')
    plt.title(title)

    # Add the category names to the x-axis
    plt.xticks(x, categories)
    plt.legend()
    plt.show()

def graph_type_2(file_path, title):
    data = pd.read_csv(file_path)

    plt.figure(figsize=(10, 6))
    categories = ['2009', '2015', '2020']
    num_categories = len(categories)
    x = np.arange(num_categories)
    bar_width = 0.2  # Adjusted for 4 bars per group

    # Extract data for each fuel type
    electricity = data.loc[0:2, 'Electricity']
    natural_gas = data.loc[0:2, 'Natural Gas']
    propane = data.loc[0:2, 'Propane']
    dual_fuel = data.loc[0:2, 'Dual Fuel']

    # Plot the bars with adjusted positions for 4 bars per group
    plt.bar(x - 1.5*bar_width, electricity, width=bar_width, label='Electricity', color='orange')
    plt.bar(x - 0.5*bar_width, natural_gas, width=bar_width, label='Natural Gas', color='brown')
    plt.bar(x + 0.5*bar_width, propane, width=bar_width, label='Propane', color='blue')
    plt.bar(x + 1.5*bar_width, dual_fuel, width=bar_width, label='Dual Fuel', color='green')

    # Add labels and title
    plt.xlabel('Years', fontweight='bold')
    plt.ylabel('Proportion', fontweight='bold')
    plt.title(title)

    # Add the category names to the x-axis
    plt.xticks(x, categories)
    plt.legend()
    plt.show()


def main():
    # extract_b13('b13_2018')
    # extract_b13('b13_2012')
    # graph_type_1('csvs/ResidentialV1', 'Proportions of Energy Sources for Residential Household Cooking')
    graph_type_1('csvs/Commercial.csv', 'Proportions of Energy Sources for Commercial Cooking by Total Floorspace')
    graph_type_2('csvs/ResidentialV2.csv', 'Most Used Stove-Top Fuels in Residential Cooking by Household')
    pass

if __name__ == "__main__":
    main()