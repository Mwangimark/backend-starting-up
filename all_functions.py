import re
from flask import jsonify

def email_format(self, data):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
