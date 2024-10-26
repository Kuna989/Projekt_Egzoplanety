import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from dataprocessor import load_planet_data, calculate_travel_times


class App:
    def __init__(self, master):
        self.master = master
        self.file_path = "../data/data.csv"  # Zakładamy, że plik jest już dołączony do aplikacji
        self.planet_data = load_planet_data(self.file_path)

        self.create_widgets()

    def create_widgets(self):
        # Etykieta tytułowa
        self.title_label = tk.Label(self.master, text="Analiza Danych - Czas Podróży", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Lista rozwijana do wyboru planety
        self.planet_label = tk.Label(self.master, text="Wybierz planetę:")
        self.planet_label.pack(pady=5)

        self.planet_combobox = ttk.Combobox(self.master, values=self.get_planet_names())
        self.planet_combobox.pack(pady=5)

        # Przycisk wyświetlania wykresu
        self.show_graph_button = tk.Button(self.master, text="Pokaż Wykres", command=self.show_graph)
        self.show_graph_button.pack(pady=20)

    def get_planet_names(self):
        # Zwraca listę nazw planet z wczytanych danych
        return self.planet_data['planet_name'].tolist()

    def show_graph(self):
        # Pobieramy wybraną planetę
        selected_planet = self.planet_combobox.get()

        if not selected_planet:
            messagebox.showwarning("Brak wyboru", "Proszę wybrać planetę z listy.")
            return

        # Pobieramy dane dystansu do wybranej planety
        planet_row = self.planet_data[self.planet_data['planet_name'] == selected_planet]

        if planet_row.empty:
            messagebox.showerror("Błąd", "Nie znaleziono danych dla wybranej planety.")
            return

        distance_parsec = planet_row['distance'].values[0]

        # Obliczamy czas podróży dla różnych rakiet
        travel_times = calculate_travel_times(distance_parsec)

        # Tworzymy wykres
        self.create_bar_chart(travel_times, selected_planet)

    def create_bar_chart(self, travel_times, planet_name):
        # Tworzymy wykres kolumnowy
        names = list(travel_times.keys())
        times = list(travel_times.values())

        plt.figure(figsize=(8, 6))
        plt.bar(names, times, color=['blue', 'orange', 'green'])
        plt.xlabel("Typ Rakiety")
        plt.ylabel("Czas Podróży (lata)")
        plt.title(f"Czas Podróży do {planet_name}")
        plt.show()