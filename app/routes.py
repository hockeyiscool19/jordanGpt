from app.utils.firebase import FIRE
from app.utils.trainGpt.JORDAN_GPT import JORDAN_GPT
from flask import Blueprint, jsonify
from datetime import datetime
from flask import request, render_template, session
import json
import time
import secrets


app_blueprint = Blueprint('app', __name__)
app_blueprint.secret_key = secrets.token_hex(32)


# Load resume data from JSON file
with open('app/utils/data/resume.json') as f:
    resume_data = json.load(f)

# Load resume data from JSON file
with open('app/utils/data/roleDescriptions.json') as f:
    role_data = json.load(f)


# # Loads static page
@app_blueprint.route('/')
def index():
    return render_template('index.html')


@app_blueprint.route('/home')
def home():
    """
    Home Route
    ---
    tags:
      - Home
    responses:
      200:
        description: Welcome message and general information about the API.
    """
    # logger.info('Home route accessed')
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Home route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify({'message': 'Welcome! With this API, you can access my resume data. Please see the documentation for more details.'})

@app_blueprint.route('/resume/skills')
def get_skills():
    """
    Get Skills
    ---
    tags:
      - Resume
    responses:
      200:
        description: Returns the skills section of the resume.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Skills route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['skills'])


# Route for work experience section


@app_blueprint.route('/resume/work_experience')
def get_work_experience():
    """
    Get Work Experience
    ---
    tags:
      - Resume
    responses:
      200:
        description: Returns the work experience section of the resume.
    """

    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Work experience route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['work_experience'])

# Route for individual internships


@app_blueprint.route('/resume/internships')
def get_internship():
    """
    Get Specific Internship
    ---
    tags:
      - Resume
    parameters:
      - name: internship_name
        in: query
        type: string
        required: true
        description: Name of the internship to retrieve.
    responses:
      200:
        description: Returns details of the specified internship.
      400:
        description: Internship not found.
    """

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
    """
    Get Projects
    ---
    tags:
      - Resume
    responses:
      200:
        description: Returns the projects section of the resume.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Projects route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['projects'])

# Route for education section


@app_blueprint.route('/resume/education')
def get_education():
    """
    Get Education
    ---
    tags:
      - Resume
    responses:
      200:
        description: Returns the education section of the resume.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Education route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(resume_data['education'])

# Route for DataShapes internship


@app_blueprint.route('/roleDescriptions/datashapes')
def get_datashapes():
    """
    Get DataShapes Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the DataShapes internship.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'DataShapes route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['datashapes'])

# Route for Tesla internship


@app_blueprint.route('/roleDescriptions/tesla')
def get_tesla():
    """
    Get Tesla Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the Tesla internship.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Tesla route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['tesla'])

# Route for Cats Stats internship


@app_blueprint.route('/roleDescriptions/data_cats')
def get_data_cats():
    """
    Get Data Cats Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the Data Cats internship.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Data Cats route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['data_cats'])

# Route for Q2 internship


@app_blueprint.route('/roleDescriptions/q2')
def get_q2():
    """
    Get Q2 Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the Q2 internship.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Q2 route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['Q2'])

# Route for Esme internship


@app_blueprint.route('/roleDescriptions/esme')
def get_esme():
    """
    Get Esme Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the Esme internship.
    """
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'log': 'Esme route accessed',
    }
    FIRE.load_dict(data, path='/logs')
    return jsonify(role_data['esme'])

# Route for C2i internship


@app_blueprint.route('/roleDescriptions/c2i')
def get_c2i():
    """
    Get C2i Internship Description
    ---
    tags:
      - Internship Descriptions
    responses:
      200:
        description: Returns the description for the C2i internship.
    """
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

@app_blueprint.route('/jordan_gpt', methods=['POST'])
def jordan_gpt():
    """
    Query the JORDAN_GPT Model
    ---
    tags:
      - GPT
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - question
          properties:
            question:
              type: string
              description: Question to ask the JORDAN_GPT model.
    responses:
      200:
        description: Returns the response from the JORDAN_GPT model.
      400:
        description: Error querying the model.
    """
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


################################################################################################################################################
from firebase_admin import auth
from flasgger.utils import swag_from

@app_blueprint.route('/signup', methods=['POST'])
def signup():
    """
    Signup a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              description: Email address of the user.
            password:
              type: string
              description: Password for the user.
    responses:
      200:
        description: Successfully created user
        schema:
          type: object
          properties:
            message:
              type: string
            uid:
              type: string
      400:
        description: Error creating user
    """

    try:
        data = request.json
        email = data['email']
        password = data['password']

        # Create a user in Firebase
        user = auth.create_user(email=email, password=password)

        # The user's ID (uid) can be accessed from the user object
        uid = user.uid

        # Optionally, store the uid or any other details in your database

        return jsonify({"message": "Successfully created user", "uid": uid}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
