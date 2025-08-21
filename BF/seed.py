# File: BF/seed.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import time

print("Script di seeding avviato.")

# --- Configurazione dell'App Flask (necessaria per il contesto) ---
app = Flask(__name__)

# Leggiamo la configurazione del database dalle variabili d'ambiente
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
database_uri = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Definizione dei Modelli (copiati da main.py) ---
# Dobbiamo ridefinirli qui perché questo script è indipendente da main.py
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))  # Nome dell'utente
    email = db.Column(db.String(100), unique=True)  # Email unica
    password = db.Column(db.String(255))  # Password (in chiaro, da hashare in produzione)
    break_duration = db.Column(db.Integer)  # Durata della pausa (5 o 10 minuti)
    morning_time = db.Column(db.String(5))   # Orario della notifica mattutina
    afternoon_time = db.Column(db.String(5)) # Orario della notifica pomeridiana
    evening_time = db.Column(db.String(5))   # Orario della notifica serale
    timezone = db.Column(db.String(64), default='UTC')
#tabella per progressi
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    date = db.Column(db.String(10))  # Formato "YYYY-MM-DD"
    completed = db.Column(db.Boolean)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    type = db.Column(db.String(50))
    image_url = db.Column(db.String(200))


# --- Dati da Inserire ---
users_data = [
    { 'name': 'marco', 'email': 'marco@gmail.com', 'password': '123456', 'break_duration': 5, 'morning_time': '18:14', 'afternoon_time': '15:24', 'evening_time': '18:44', 'timezone': 'Europe/Rome'},
    { 'name': 'Mourad', 'email': 'mourad@gmail.com', 'password': '123456', 'break_duration': 5, 'morning_time': '09:00', 'afternoon_time': '14:00', 'evening_time': '18:00', 'timezone': 'Europe/Rome'}
]

exercises_data = [
    {'name': 'Allungamento della schiena', 'description': 'Allunga la schiena.', 'duration': 5, 'type': 'stretching', 'image_url': 'static/img/stretchingshiena.jpg'},
    {'name': 'Camminata sul posto', 'description': 'Cammina sul posto.', 'duration': 5, 'type': 'walk', 'image_url': 'static/img/run.gif'},
    {'name': 'Jumping jacks', 'description': 'Esegui 3 serie da 10 jumping jacks.', 'duration': 5, 'type': 'corpo_libero', 'image_url': 'static/img/jumping-jacks.gif'},
    {'name': 'Crunch', 'description': 'Esegui 3 serie da 3-6 ripetizioni con 1 min di pausa tra un serie e l\'altra', 'duration': 5, 'type': 'corpo_libero', 'image_url': 'static/img/Crunch.gif'},
    {'name': 'Push up', 'description': 'Esegui 3 serie da 3-6 ripetizioni con 2 min di pausa tra un serie e l\'altra se non c\'e la si fa usare le ginocchia per falicitare l\'esecuzione.', 'duration': 5, 'type': 'corpo_libero', 'image_url': 'static/img/push_up.gif'},
    {'name': 'Decopression-Circuit', 'description': 'Esercizio importante per spalle e cervicale 1 min per ogni posizione', 'duration': 5, 'type': 'stretching', 'image_url': 'static/img/decopression.jpg'},
    {'name': 'Cossack Squat', 'description': 'Esercizio importante per sviluppare forza nelle gambe e mobilità del bacino 2 min per lato', 'duration': 5, 'type': 'stretching', 'image_url': 'static/img/Cossack.jpg'}
]


# --- Logica di Seeding ---
def seed():
    with app.app_context():
        # Attendi che il database sia pronto
        db_ready = False
        for _ in range(10):
            try:
                db.session.execute('SELECT 1')
                db_ready = True
                print("Database è pronto.")
                break
            except Exception as e:
                print(f"In attesa del database... ({e})")
                time.sleep(2)
        
        if not db_ready:
            print("Database non disponibile. Seeding fallito.")
            return
        
        print("Creazione di tutte le tabelle (se non esistono)...")
        db.create_all()

        # Svuota le tabelle per evitare duplicati
        print("Svuotamento tabelle...")
        db.session.query(Progress).delete()
        db.session.query(Exercise).delete()
        db.session.query(User).delete()
        
        # Inserisci utenti
        print("Inserimento utenti...")
        db_users = []
        for user_info in users_data:
            #user_info['password'] = generate_password_hash(user_info['password'], method='pbkdf2:sha256')
            new_user = User(**user_info)
            db.session.add(new_user)
            db_users.append(new_user)
        db.session.commit()

        # Inserisci esercizi
        print("Inserimento esercizi...")
        for exercise_info in exercises_data:
            new_exercise = Exercise(**exercise_info)
            db.session.add(new_exercise)
        
        db.session.commit()
        print("Seeding del database completato con successo.")

if __name__ == '__main__':
    seed()