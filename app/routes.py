from app.utils.firebase import FIRE
from app.utils.trainGpt.JORDAN_GPT import JORDAN_GPT
from flask import Blueprint, jsonify
from datetime import datetime
from flask import request
import json


app_blueprint = Blueprint('app', __name__)


# Load resume data from JSON file
with open('app/utils/data/resume.json') as f:
    resume_data = json.load(f)

# Load resume data from JSON file
with open('app/utils/data/roleDescriptions.json') as f:
    role_data = json.load(f)

# Route for root URL


@app_blueprint.route('/')
def index():
    # logger.info('Home route accessed')
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Home route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify({'message': 'Welcome! With this API, you can access my resume data. Please see the documentation for more details.'})

# Route for skills section


@app_blueprint.route('/resume/skills')
def get_skills():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Skills route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['skills'])

# Route for work experience section


@app_blueprint.route('/resume/work_experience')
def get_work_experience():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Work experience route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['work_experience'])

# Route for individual internships


@app_blueprint.route('/resume/internships')
def get_internship():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Internships route accessed',
    }
    FIRE.load_dict(data, path='/logs')
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
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Projects route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['projects'])

# Route for education section


@app_blueprint.route('/resume/education')
def get_education():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Education route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['education'])

# Route for DataShapes internship


@app_blueprint.route('/roleDescriptions/datashapes')
def get_datashapes():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'DataShapes route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['datashapes'])

# Route for Tesla internship


@app_blueprint.route('/roleDescriptions/tesla')
def get_tesla():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Tesla route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['tesla'])

# Route for Cats Stats internship


@app_blueprint.route('/roleDescriptions/data_cats')
def get_data_cats():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Data Cats route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['data_cats'])

# Route for Q2 internship


@app_blueprint.route('/roleDescriptions/q2')
def get_q2():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Q2 route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['Q2'])

# Route for Esme internship


@app_blueprint.route('/roleDescriptions/esme')
def get_esme():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Esme route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['esme'])

# Route for C2i internship


@app_blueprint.route('/roleDescriptions/c2i')
def get_c2i():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'C2i route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['c2i'])

# Route for contact information


@app_blueprint.route('/contact')
def get_contact_info():
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Contact route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    contact_info = {
        'name': 'Jordan Eisenman',
        'email': 'jordaneisenman@gmail.com',
        'phone': '802-733-7703'
    }
    return jsonify(contact_info)

# Route for Jordan GPT


@app_blueprint.route('/jordan_gpt', methods=['GET'])
def jordan_gpt():
    try:
        # Query the JORDAN_GPT model
        question = request.json['question']
        response = JORDAN_GPT.respond(question)
        jordan_gpt = {
            'question': question,
            'response': response,
        }
        # Return the response and response instruction as a JSON object
        return jordan_gpt, 200
    except Exception as e:
        logs = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'loglevel': 'ERROR',
            'log': e,
        }
        FIRE.load_dict(logs, path='/logs')
        return "Error: {}".format(e), 400
