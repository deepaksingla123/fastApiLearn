
from fastapi import FastAPI
import uvicorn

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b    

def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        return "Error: Division by zero"
    return a / b    

app = FastAPI()

@app.get("/add")
def add_endpoint(x: float, y: float):
    result = add(x, y)
    print(f"add_endpoint: {x} + {y} = {result}")

    return {"operation": "add", "a": x, "b": y, "result": result}

@app.get("/subtract")
def subtract_endpoint(a: float, b: float):
    result = subtract(a, b)
    return {"operation": "subtract", "a": a, "b": b, "result": result}

@app.get("/multiply")
def multiply_endpoint(a: float, b: float):
    result = multiply(a, b)
    return {"operation": "multiply", "a": a, "b": b, "result": result}  

@app.get("/divide")
def divide_endpoint(a: float, b: float):
    result = divide(a, b)
    return {"operation": "divide", "a": a, "b": b, "result": result}    

@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add, /subtract, /multiply or /divide endpoints."}

# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)

