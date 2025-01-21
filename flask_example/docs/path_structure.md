Here's the proper directory structure for your Flask application, with separation of concerns for templates, views, WASPAS logic, and the database model. This structure ensures maintainability and scalability.

### Directory Structure
```
project_root/
│
├── app/
│   ├── __init__.py          # App initialization and configuration
│   ├── models.py            # Database models (Player class and DB setup)
│   ├── views.py             # Flask routes and view functions
│   ├── waspas.py            # WASPAS algorithm implementation
│   ├── templates/           # HTML templates
│   │   └── index.html       # Main template for displaying top players
│   ├── static/              # Static files (CSS, JS, images)
│   └── utils/               # Utility functions (optional, e.g., helpers)
│
├── migrations/              # Database migration files (if using Flask-Migrate)
│
├── config.py                # Configuration file for the app (e.g., DB URI)
├── requirements.txt         # Python dependencies
├── run.py                   # Entry point for running the Flask app
└── README.md                # Project documentation
```

---

### File Details

#### `__init__.py` (App Initialization)
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import routes and models
        from . import views, models
        db.create_all()

    return app
```

---

#### `models.py` (Database Models)
```python
from . import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skill = db.Column(db.Float, nullable=False)
    pace = db.Column(db.Float, nullable=False)
    strength = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
```

---

#### `waspas.py` (WASPAS Logic)
```python
import pandas as pd

def WASPAS(data, weights, lambda_):
    """
    WASPAS method for decision-making.
    """
    numeric_cols = data.select_dtypes(include=['number']).columns
    df_numeric = data[numeric_cols]
    normalized_data = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())

    ws = normalized_data.mul(weights, axis=1).sum(axis=1)
    wp = normalized_data.pow(weights, axis=1).prod(axis=1)

    waspas_score = lambda_ * ws + (1 - lambda_) * wp

    ranked_data = data.copy()
    ranked_data['WASPAS_Score'] = waspas_score
    ranked_data = ranked_data.sort_values(by='WASPAS_Score', ascending=False)

    return ranked_data
```

---

#### `views.py` (Flask Routes)
```python
from flask import render_template
from . import db
from .models import Player
from .waspas import WASPAS
import pandas as pd

def get_top_five():
    players = Player.query.all()
    player_data = [
        (player.name, player.skill, player.pace, player.strength, player.age, player.cost)
        for player in players
    ]

    data = pd.DataFrame(player_data, columns=['Name', 'Skill', 'Pace', 'Strength', 'Age', 'Cost'])
    weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15, 'Cost': 0.2}
    lambda_ = 0.5

    return WASPAS(data, weights, lambda_).head(5)

def register_routes(app):
    @app.route('/')
    def index():
        top_players = get_top_five()
        return render_template('index.html', players=top_players)

# Register routes in the app
from flask import Blueprint
views_bp = Blueprint('views', __name__)
register_routes(views_bp)
```

---

#### `templates/index.html` (HTML Template)
Same as provided earlier in the previous response.

---

#### `config.py` (App Configuration)
```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///players.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

#### `run.py` (Entry Point)
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Instructions to Run
1. **Install Dependencies**:
   ```bash
   pip install flask flask-sqlalchemy
   ```
2. **Set Up Database**:
   - Run the app once to create the `players.db` database:
     ```bash
     python run.py
     ```
   - Use Flask-SQLAlchemy to insert sample data into the `Player` table.

3. **Run the App**:
   ```bash
   python run.py
   ```

4. **Access the App**:
   Open `http://127.0.0.1:5000/` in your browser.

---

Let me know if you'd like guidance on database seeding, Dockerizing the app, or adding CSS for styling!