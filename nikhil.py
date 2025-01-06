# Example dictionary
data = {"boy": 11, "girl": 12, "boy2": 30, "girl2": 35, "boy3": 45, "girl3": 29}

# Initialize counters
total_boys = 0
total_girls = 0
boys_above_15 = 0
girls_above_15 = 0

# Iterate through the dictionary
for key, age in data.items():
    if "boy" in key.lower():
        total_boys += 1
        if age > 15:
            boys_above_15 += 1
    elif "girl" in key.lower():
        total_girls += 1
        if age > 15:
            girls_above_15 += 1

# Display results
print(f"Total number of boys: {total_boys}")
print(f"Total number of girls: {total_girls}")
print(f"Number of boys above 18: {boys_above_15}")
print(f"Number of girls above 18: {girls_above_15}")