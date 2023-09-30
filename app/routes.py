from app.utils.model import JORDAN_GPT
from flask import Blueprint, jsonify
import json
from requests import request
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# Set the logging level (optional)
logger.setLevel(logging.INFO)

# Create a file handler for logging to a file (optional)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a stream handler for logging to the console (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Set the formatter for the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


app_blueprint = Blueprint('app', __name__)

# Load resume data from JSON file
with open('app/utils/data/resume.json') as f:
    resume_data = json.load(f)

# Load resume data from JSON file
with open('app/utils/data/roleDescription.json') as f:
    role_data = json.load(f)

# Route for root URL


@app_blueprint.route('/')
def index():
    logger.info('Home route accessed')
    return jsonify({'message': 'Welcome! With this API, you can access my resume data. Please see the documentation for more details.'})

# Route for skills section


@app_blueprint.route('/resume/skills')
def get_skills():
    return jsonify(resume_data['skills'])

# Route for work experience section


@app_blueprint.route('/resume/work_experience')
def get_work_experience():
    return jsonify(resume_data['work_experience'])

# Route for individual internships


@app_blueprint.route('/resume/internships')
def get_internship():
    if 'internship_name' not in request.args:
        return jsonify({'message': 'Please provide an internship name'})
    internship_name = request.args['internship_name']
    for internship in resume_data['internships']:
        if internship['name'].lower() == internship_name.lower():
            return jsonify(internship)
    return jsonify({'error': 'Internship not found'})

# Route for projects section


@app_blueprint.route('/resume/projects')
def get_projects():
    return jsonify(resume_data['projects'])

# Route for education section


@app_blueprint.route('/resume/education')
def get_education():
    return jsonify(resume_data['education'])

# Route for DataShapes internship


@app_blueprint.route('/roleDescriptions/datashapes')
def get_datashapes():
    return jsonify(role_data['DataShapes'])

# Route for Tesla internship


@app_blueprint.route('/roleDescriptions/tesla')
def get_tesla():
    return jsonify(role_data['tesla'])

# Route for Cats Stats internship


@app_blueprint.route('/roleDescriptions/data_cats')
def get_data_cats():
    return jsonify(role_data['data_cats'])

# Route for Q2 internship


@app_blueprint.route('/roleDescriptions/Q2')
def get_q2():
    return jsonify(role_data['Q2'])

# Route for Esme internship


@app_blueprint.route('/roleDescriptions/esme')
def get_esme():
    return jsonify(role_data['esme'])

# Route for C2i internship


@app_blueprint.route('/roleDescriptions/C2i')
def get_c2i():
    return jsonify(role_data['c2i'])

# Route for contact information


@app_blueprint.route('/contact')
def get_contact_info():
    contact_info = {
        'name': 'Jordan Eisenman',
        'email': 'jordaneisenman@gmail.com',
        'phone': '802-733-7703'
    }
    return jsonify(contact_info)


@app_blueprint.route('/jordan_gpt', methods=['POST'])
def jordan_gpt():
    try:
        # Query the JORDAN_GPT model
        question = request.json['question']
        response = JORDAN_GPT.query(question)
        logger.info('Jordan GPT accessed')
        logger.info('Question: ' + question)
        logger.info('Response: ' + response)
        # Return the response and response instruction as a JSON object
        return response
    except Exception as e:
        logger.error(e)
        return "Error: {}".format(e), 400
