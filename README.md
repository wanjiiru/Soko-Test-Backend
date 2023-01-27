## Set-up and Installation

### Prerequiites
    - Python 3.8

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/wanjiiru/Soko-Test-Backend.git && cd Soko-Test-Backend`

### Create a Virtual Environment
Run the following commands in the same terminal:
```bash
sudo apt-get install python3.8-venv
python3.8 -m venv virtual
source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements`

### Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:8080/`