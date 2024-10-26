import pandas as pd

PARSEC_TO_KM = 3.086e13
Light_speed = 300000

SPACE_X_STARSHIP_SPEED = 27000  # Realistyczna prędkość Starship (27,000 km/h)
ROCKET_50_PERCENT_LIGHT_SPEED = 0.5 * Light_speed
ROCKET_99_PERCENT_LIGHT_SPEED = 0.99 * Light_speed

def load_planet_data(file_path):

    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise RuntimeError(f"Błąd podczas wczytywania danych: {str(e)}")

def calculate_travel_times(distance_parsec):

    distance_km = distance_parsec * PARSEC_TO_KM

    travel_times = {
        "Starship (SpaceX)": distance_km / SPACE_X_STARSHIP_SPEED,
        "50% Prędkości Światła": distance_km / ROCKET_50_PERCENT_LIGHT_SPEED,
        "99% Prędkości Światła": distance_km / ROCKET_99_PERCENT_LIGHT_SPEED,
    }

    return travel_times
