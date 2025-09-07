import pandas as pd
import matplotlib.pyplot as plt


def main():
    # TODO: PART:I -> Data Cleaning
    df = pd.read_csv("OLX_Car_Data_CSV.csv", encoding='latin1')
    # Data Analysis
    # print(df.head())
    # print(df.info())
    # print(df.describe())

    # Remove Null Enteries
    df = df.dropna()
    # Remove Duplicates
    df = df.drop_duplicates()
    # Filter the Years
    df = df[(df["Year"] >= 2010) & (df["Year"] <= 2020)]
    # To sort the values by years from 2010 to 2020
    df = df.sort_values(by="Year", ascending=True)
    # print(df.head())
    df.reset_index(drop=True, inplace=True)
    # --- Clean Price (remove symbols, convert to numeric) ---
    df["Price"] = df["Price"].astype(str).str.replace(",", "").str.replace("PKR", "").astype(float)

    # --- Clean KMs Driven ---
    df["KMs Driven"] = df["KMs Driven"].astype(str).str.replace(",", "").str.replace("km", "").astype(float)

    # --- Standardize Categories (optional) ---
    df["Fuel"] = df["Fuel"].str.strip().str.title()
    df["Brand"] = df["Brand"].str.upper()

    print(df.head(3))

    # TODO: PART:II -> Data Analysis

    # TOP 5 best Performing Cities
    best_cities = df["Registered City"].value_counts().head(5)
    print(best_cities)

    # Percentage of User - New Cars

    condition_count = df["Condition"].value_counts()
    condition_percentages = ((condition_count / condition_count.sum()) * 100).round(2)
    print(f"{condition_percentages}%")

    #Percentage of Fuel Users Types

    fuel_count = df["Fuel"].value_counts()

    # Plot bar chart
    option = int(input("Enter an Option: "))
    if option == 1:
        plt.figure(figsize=(8, 6))
        plt.bar(fuel_count.index, fuel_count.values,
                color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])  # Customize colors
        plt.title("Fuel Type Distribution", fontsize=16)
        plt.xlabel("Fuel Type", fontsize=12)
        plt.ylabel("Number of Cars", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    elif option == 2:
        fuel_percentage = ((fuel_count / fuel_count.sum()) * 100).round(2)
        print(fuel_percentage)
        plt.figure(figsize=(8, 6))
        plt.pie(condition_percentages, labels=condition_percentages.index, autopct='%1.1f%%', startangle=140)
        plt.title('Percentage Distribution of Car Conditions')
        plt.axis('equal')
        plt.show()
    elif option == 3:
        plt.figure(figsize=(8,6))
        plt.bar(best_cities.index,best_cities.values)
        plt.title("Best Performing cities",fontsize=12)
        plt.xlabel("The Cities", fontsize=10)
        plt.ylabel("Sales", fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

# TO FIND THE BEST PERFORMING CAR BRANDS AND THEIR RESPECTIVE MODELS
    cars = df.groupby(["Brand", "Model"]).size().reset_index(name='Count')
    top_model = cars.sort_values(by='Count', ascending=False).head(5)
    print("Best-selling car model and brand:")
    print(top_model)

    # Plot
    labels = top_model['Brand'] + ' ' + top_model['Model']
    plt.figure(figsize=(8, 6))
    plt.bar(labels, top_model['Count'], color='skyblue')
    plt.title("Best Performing Cars")
    plt.xlabel("Cars", fontsize=10)
    plt.ylabel("Selling Value", fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    df.to_csv("Cleaned_Data.csv", index=False)
    print("Done")


if __name__ == '__main__':
    main()
