# Login Form Validation - DevOps Project

This beginner-friendly project demonstrates:
- HTML and CSS login form
- JavaScript username/password validation
- Git source-code management
- Docker image creation using Nginx
- Selenium browser automation tests with pytest

## Demo credentials

- Username: `admin`
- Password: `admin123`

> This is a client-side demonstration only. It is not secure authentication for a real application.

## 1. Run locally

Open `index.html` in a browser, or use VS Code Live Server.

## 2. Git commands

Run these commands in the project folder:

```bash
git init
git add .
git status
git commit -m "Initial login form project"
git branch -M main
```

Create an empty GitHub repository named `Login-Form-Validation`, then connect it:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Useful commands:

```bash
git log
git status
git add .
git commit -m "Update login validation"
git push
git pull
```

## 3. Build and run with Docker

Make sure Docker Desktop is running. From this folder:

```bash
docker build -t login-app .
docker run -d -p 8082:80 --name login-container login-app
```

Open: http://localhost:8082

Useful Docker commands:

```bash
docker images
docker ps
docker logs login-container
docker stop login-container
docker start login-container
```

If the container name is already in use, remove the old container first:

```bash
docker rm -f login-container
```

Then run the `docker run` command again.

## 4. Run Selenium tests

Keep the Docker container running. Install Python packages:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v test_login.py
```

Selenium 4 uses Selenium Manager to help obtain a compatible browser driver. Google Chrome must be installed.

The test checks:
1. Empty username and password
2. Invalid credentials
3. Valid demo credentials

## Project workflow

HTML/CSS/JavaScript -> Git/GitHub -> Docker image/container -> Selenium tests
