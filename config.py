import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATION =False

    #postgres://brian:FNR40VNWLlH00J5IxwbMTRNvRyZrkXF4@dpg-cl34iuiuuipc7386ls7g-a.oregon-postgres.render.com/pets_data