# Retrieves the values of a, b, and c from the user input.
# Performs conditional checks and calculations:
# Check if a, b, and c are numeric. If not, return an error message.
# If a is less than 1, display a message indicating that the input is too small.
# If b is equal to 0, indicate that it will not affect the result.
# If c is negative, provide a specific error message.
# If c is greater than or equal to 0, compute c^3.
# If the result of c^3 is greater than 1000:
# Multiply the square root of c^3 by 10.
# Otherwise, divide the square root by a.
# Add b to the final result.
# Generate output formatted as HTML to display the results on a web page.
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a < 1:
    print("Error: Input is too small.")

elif b == 0:
    print("Warning: b is equal to 0 and will not affect the result.")

elif c < 0:
    print("Error: c is negative.")

elif c > 0:
    result = c ** 3
    if result > 1000:
        result = (result ** 0.5) * 10
    else:
        result = (result ** 0.5) / a
    result += b
    

print(f"""
<html>
<body>
    <main 
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
    padding: 1rem;
    border-radius: 0.45rem;
    margin: auto;
    max-width: fit-content;
    ">   
    
    <h1>Assignment 4 - Felipe Franco de Camargo</h1>
    <h1>Initial Values</h1>
    
    <span style="font-size:18px; margin-bottom:0.25rem;" >x: {a}</span>
    <span style="font-size:18px; margin-bottom:0.25rem;" >y: {b}</span>
    <span style="font-size:18px; margin-bottom:0.25rem;" >z: {c}</span>

    <h4>Final Result: {result}</h2>
         </main>
</body>
</html>
""")
    
    

