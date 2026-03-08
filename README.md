# ACEest Gym Management System

## Project Overview

This is a simple Flask-based web application for ACEest Functional Fitness & Gym. The application displays different fitness program plans including workout schedules and nutrition information for Fat Loss, Muscle Gain, and Beginner programs. It demonstrates basic DevOps practices including version control, testing, containerization, and CI/CD.

## Technologies Used

- **Flask**: Web framework for Python
- **Python 3.10**: Programming language
- **Docker**: Containerization platform
- **pytest**: Unit testing framework
- **GitHub Actions**: Continuous Integration (planned)
- **Jenkins**: Build automation (planned)

## Features

- Interactive program selection (Fat Loss, Muscle Gain, Beginner)
- Dynamic display of workout schedules and nutrition plans
- Responsive web interface with custom styling
- Containerized deployment with Docker
- Unit tests for core functionality

## How to Run the Flask App Locally

1. Ensure Python 3.10 is installed.
2. Clone the repository.
3. Navigate to the project directory.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`
6. Open a browser and go to `http://localhost:5001`

## How to Run with Docker

1. Ensure Docker is installed and running.
2. Clone the repository.
3. Navigate to the project directory.
4. Build the Docker image: `docker build -t aceest-gym .`
5. Run the container: `docker run -p 5001:5001 aceest-gym`
6. Open a browser and go to `http://localhost:5001`

The application will be accessible at `http://localhost:5001` with the same functionality as the local setup.

## How to Run Tests Manually

1. Install dependencies: `pip install -r requirements.txt`
2. Run pytest: `pytest`
3. Tests will verify the app functionality, including:
   - Home page loads correctly
   - Program selection works for Fat Loss, Muscle Gain, and Beginner programs
   - Correct workout and diet information is displayed
   - Static CSS files are served properly

## Project Structure

```
aceest-gym
├── app.py                    # Flask application with program data
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container configuration
├── README.md                 # Project documentation
├── templates/                # HTML templates
│   └── index.html           # Main page template with program selection
├── static/                   # Static assets
│   └── style.css            # Styling for the web interface
└── tests/
    └── test_app.py          # Unit tests
```

## Explanation of GitHub Actions Pipeline

The GitHub Actions workflow (`.github/workflows/main.yml`) runs on every push and pull request. It performs the following stages:

1. **Checkout repository**: Retrieves the latest code.
2. **Setup Python**: Installs Python 3.10.
3. **Install dependencies**: Installs required packages from `requirements.txt`.
4. **Run pytest**: Executes unit tests to ensure code quality.
5. **Build Docker image**: Creates a Docker image to verify containerization works.

This ensures that code changes are automatically tested and can be containerized.

## Explanation of Jenkins Build Process

Jenkins can be configured to automate the build process:

1. **Pull the project from GitHub**: Use the Git plugin to clone the repository.
2. **Install dependencies**: Run `pip install -r requirements.txt` in a build step.
3. **Run tests**: Execute `pytest` to validate the application.
4. **Build the Docker image**: Run `docker build -t aceest-gym .` to create the container image.

Jenkins pipelines can be triggered by GitHub webhooks on pushes or pull requests, providing continuous integration.

## Explanation of Version Control Strategy

- **Version 1.0**: Initial commit with basic functionality.
- **Future versions**: Newer versions will be pushed to simulate software evolution, such as adding features or fixing bugs.
- **CI/CD Triggers**: Each push to the repository triggers the GitHub Actions pipeline, ensuring automated testing and building.
- **Branching**: Use feature branches for development, merging to main after review.