# task1_engagement.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Sample data (replace with pd.read_csv("yourfile.csv")) ---
np.random.seed(42)
domains = ["youtube.com", "github.com", "stackoverflow.com",
           "wikipedia.org", "reddit.com", "medium.com", "twitter.com"]
n = 500
df = pd.DataFrame({
    "user_id":   np.random.randint(1, 80, n),
    "domain":    np.random.choice(domains, n, p=[.25,.15,.12,.10,.15,.10,.13]),
    "time_spent_min": np.random.gamma(2, 5, n).round(2),
    "visits":    np.random.randint(1, 10, n),
    "date":      pd.date_range("2025-01-01", periods=n, freq="3h")
})

print("=== Data preview ===")
print(df.head(), "\n")
print("Shape:", df.shape)

# --- 1. Popular domains (by total visits) ---
pop = df.groupby("domain")["visits"].sum().sort_values(ascending=False)
print("\n=== Visits per domain ===\n", pop)

# --- 2. Avg time spent per domain ---
avg_time = df.groupby("domain")["time_spent_min"].mean().sort_values(ascending=False)
print("\n=== Avg time spent (min) per domain ===\n", avg_time.round(2))

# --- 3. Engagement trend over time (daily total minutes) ---
df["day"] = df["date"].dt.date
trend = df.groupby("day")["time_spent_min"].sum()

# --- Visualizations ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

pop.plot(kind="bar", ax=axes[0], color="steelblue", edgecolor="black")
axes[0].set_title("Popular Domains (Total Visits)")
axes[0].set_ylabel("Visits"); axes[0].tick_params(axis="x", rotation=45)

avg_time.plot(kind="barh", ax=axes[1], color="coral", edgecolor="black")
axes[1].set_title("Avg Time Spent per Domain (min)")
axes[1].set_xlabel("Minutes")

trend.plot(ax=axes[2], marker="o", color="green")
axes[2].set_title("Daily Engagement Trend")
axes[2].set_ylabel("Total Minutes"); axes[2].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
