import json
from flask import request, Response
from src.core.uses_cases.admin_coordinator import AdminCoordinator

def store(admin_coordinator: AdminCoordinator):
  request_data = request.json
  admin_coordinator.create_author(request_data["name"])
  response = {
    "message": "Author created"
  }
  return Response(
    json.dumps(response),
    status=200, 
    mimetype='application/json')



