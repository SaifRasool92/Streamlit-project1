import streamlit as st
import matplotlib.pyplot as plt

# Title and description
st.title("Quadrant Finder")
st.write("Enter the x and y coordinates to find out which quadrant the point lies in.")

# Input fields for coordinates
x = st.number_input("Enter the x-axis value:", value=0)
y = st.number_input("Enter the y-axis value:", value=0)

# Determine the quadrant
if x > 0 and y > 0:
    quadrant = "1st Quadrant"
elif x < 0 and y > 0:
    quadrant = "2nd Quadrant"
elif x < 0 and y < 0:
    quadrant = "3rd Quadrant"
elif x > 0 and y < 0:
    quadrant = "4th Quadrant"
elif x == 0 and y > 0:
    quadrant = "On the positive Y-axis"
elif x == 0 and y < 0:
    quadrant = "On the negative Y-axis"
elif y == 0 and x > 0:
    quadrant = "On the positive X-axis"
elif y == 0 and x < 0:
    quadrant = "On the negative X-axis"
else:
    quadrant = "At the Origin"

# Display the result
st.write(f"The point ({x}, {y}) lies in the {quadrant}.")

# Plotting the point on a graph
fig, ax = plt.subplots()
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Highlight the quadrants
ax.fill_between([0, max(10, abs(x))], 0, max(10, abs(y)), color='green', alpha=0.1)
ax.fill_betweenx([0, max(10, abs(y))], -max(10, abs(x)), 0, color='blue', alpha=0.1)
ax.fill_between([0, -max(10, abs(x))], 0, -max(10, abs(y)), color='red', alpha=0.1)
ax.fill_betweenx([0, -max(10, abs(y))], 0, max(10, abs(x)), color='yellow', alpha=0.1)

# Plot the point
ax.scatter(x, y, color='red', s=100, zorder=5)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Display the graph in Streamlit
st.pyplot(fig)



