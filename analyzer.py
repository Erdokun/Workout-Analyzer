import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data (Yapay zeka veriyi yutuyor)
# We add column names because our CSV doesn't have headers yet
column_names = ["date", "workout_type", "weight"]
data = pd.read_csv("workout_log.csv", names=column_names)

# Convert weight column to numbers so we can calculate math
data["weight"] = pd.to_numeric(data["weight"])

# 2. Analyze the data (Matematiksel analiz)
print("--- AI Data Analysis Report ---")
print(data) # Show the table on screen
print("--------------------------------")

max_weight = data["weight"].max()
average_weight = data["weight"].mean()

print(f"Your Personal Record (Max Weight): {max_weight} kg")
print(f"Your Training Average Weight: {average_weight:.2f} kg")
print("--------------------------------")

# 3. Visualize the data (Görsel zeka - Grafik çizdirme)
plt.plot(data["date"], data["weight"], marker="o", color="red", linewidth=2)

# Style the chart (Grafiği süsleyelim)
plt.title("Workout Progress Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Weight (kg)", fontsize=12)
plt.grid(True)

# Save the chart as an image
plt.savefig("progress_chart.png")
print("Boom! Progress chart created and saved as progress_chart.png successfully.")