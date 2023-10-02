# API Documentation

## Root URL

- **URL:** `/`
- **Method:** GET
- **Description:** This route welcomes users to the API and provides a brief overview of its functionality.
- **Response:** JSON response with a welcome message.

## Skills Section

- **URL:** `/resume/skills`
- **Method:** GET
- **Description:** Retrieves the skills section of the resume data.
- **Response:** JSON response containing a list of skills.

## Work Experience Section

- **URL:** `/resume/work_experience`
- **Method:** GET
- **Description:** Retrieves the work experience section of the resume data.
- **Response:** JSON response containing a list of work experience entries.

## Individual Internships

- **URL:** `/resume/internships`
- **Method:** GET
- **Description:** Retrieves information about a specific internship.
- **Parameters:**
  - `internship_name` (Query Parameter): The name of the internship to retrieve.
- **Response:** JSON response containing details of the requested internship or an error message if not found.

## Projects Section

- **URL:** `/resume/projects`
- **Method:** GET
- **Description:** Retrieves the projects section of the resume data.
- **Response:** JSON response containing a list of projects.

## Education Section

- **URL:** `/resume/education`
- **Method:** GET
- **Description:** Retrieves the education section of the resume data.
- **Response:** JSON response containing a list of education entries.

## Role Descriptions

- **URL:** `/roleDescriptions/datashapes`, `/roleDescriptions/tesla`, `/roleDescriptions/data_cats`, `/roleDescriptions/q2`, `/roleDescriptions/esme`, `/roleDescriptions/c2i`
- **Method:** GET
- **Description:** Retrieves role descriptions for specific internships.
- **Response:** JSON response containing the description of the requested internship role.

## Contact Information

- **URL:** `/contact`
- **Method:** GET
- **Description:** Retrieves contact information for Jordan Eisenman.
- **Response:** JSON response containing contact details.

## Jordan GPT

- **URL:** `/jordan_gpt`
- **Method:** GET
- **Description:** Queries the JORDAN_GPT model with a question and returns a response.
- **Request Body:** JSON object with a `question` field.
- **Response:** JSON response containing the question, response, and a corrected version (if applicable).

Please note that this documentation provides a high-level overview of your API routes. You may want to include more detailed information on request/response formats, error handling, and any additional functionality if needed.
