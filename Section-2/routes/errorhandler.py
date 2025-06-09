@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404

# You can register a global error handler in Flask for any unhandled exceptions by using:
@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
  
