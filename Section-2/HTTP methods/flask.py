from flask import Flask, request

app = Flask(__name__)

@app.route('/get-item', methods=['GET'])
def get_item():
    return "You sent a GET request"

@app.route('/add-item', methods=['POST'])
def add_item():
    name = request.form.get('name')
    qty = request.form.get('qty')
    return f"Added {qty} of {name}"

@app.route('/delete-item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    return f"Deleted item with ID {item_id}"

if __name__ == '__main__':
    app.run()
