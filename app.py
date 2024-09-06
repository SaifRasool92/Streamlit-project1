import streamlit as st

st.title("Quadrant Finder")
st.write("Enter the x and y coordinates to find out which quadrant the point lies in.")

x = st.number_input("Enter the x-axis value:", value=0)
y = st.number_input("Enter the y-axis value:", value=0)

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

st.write(f"The point ({x}, {y}) lies in the {quadrant}.")


