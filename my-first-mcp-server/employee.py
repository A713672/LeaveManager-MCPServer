# directory-server/server.py
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool
import json

app = FastMCP("employee-directory")

# Dummy employee data
EMPLOYEES = {
    "E001": {"name": "Alice", "email": "alice@example.com", "phone": "123-456", "manager": "E201"},
    "E002": {"name": "Bob", "email": "bob@example.com", "phone": "456-789", "manager": "E201"},
}

@app.tool("get_employee_info")
def get_employee_info(employee_id: str) -> dict:
    """
    Fetch employee information by employee ID or name.
    """
    # First, try exact ID match
    if employee_id in EMPLOYEES:
        return EMPLOYEES[employee_id]
    
    # If not found, try name match (case-insensitive)
    for emp_id, data in EMPLOYEES.items():
        if data["name"].lower() == employee_id.lower():
            return {"employee_id": emp_id, **data}
    
    return {"error": "Employee not found"}

@app.tool("update_employee_phone")
def update_employee_phone(employee_id: str, new_phone: str) -> dict:
    """Update an employee's phone number."""
    if employee_id in EMPLOYEES:
        EMPLOYEES[employee_id]["phone"] = new_phone
        return {"status": "success", "updated_record": EMPLOYEES[employee_id]}
    return {"status": "error", "message": "Employee not found"}

if __name__ == "__main__":
    app.run()
