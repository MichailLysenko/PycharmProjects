import json  # Importiere die json-Bibliothek für die Arbeit mit JSON-Daten
import textwrap  # Importiere die textwrap-Bibliothek für das Formatieren von Texten

class TouristRouteGDN:
    def __init__(self, name="", baujahre="", architekt="", beschreibung=""):
        # Konstruktor der Klasse TouristRouteGDN, initialisiert Attribute
        self.name = name
        self.baujahre = baujahre
        self.architekt = architekt
        self.beschreibung = beschreibung

    def main(self):
        # Hauptmethode zur Ausführung des Programms
        data = self.read_file()  # Lese vorhandene Daten aus der JSON-Datei
        name, baujahre, architekt, beschreibung = self.get_data()  # Hole neue Daten vom Benutzer
        beschreibung = self.format_beschreibung(beschreibung)  # Formatieren der Beschreibung
        self.process_data(data, name, baujahre, architekt, beschreibung)  # Verarbeite die Daten
        self.write_file(data)  # Schreibe die aktualisierten Daten zurück in die JSON-Datei
        self.print_data(data)  # Gebe die formatierten Daten im Terminal aus

    def read_file(self):
        # Methode zum Lesen der JSON-Datei
        try:
            with open("Tourist_Route_GDN.json", mode="r", encoding="utf-8") as file_stream:
                data = json.load(file_stream)  # Lade den Inhalt der JSON-Datei in ein Python-Dictionary
        except FileNotFoundError:
            data = {}  # Falls die Datei nicht gefunden wird, initialisiere ein leeres Dictionary
        except json.JSONDecodeError:
            data = {}  # Falls die Datei nicht korrekt als JSON dekodiert werden kann, initialisiere ein leeres Dictionary
        return data  # Gebe das geladene oder das leere Dictionary zurück

    def get_data(self):
        # Methode zur Abfrage neuer Daten vom Benutzer
        name = input("Geben Sie den Namen der Sehenswürdigkeit ein: ")  # Eingabe des Namens
        baujahre = input("Geben Sie die Baujahre der Sehenswürdigkeit ein: ")  # Eingabe der Baujahre
        architekt = input("Geben Sie den Namen des Architekten der Sehenswürdigkeit ein: ")  # Eingabe des Architekten
        beschreibung = input("Geben Sie die zusätzliche Beschreibungen zum Objekt ein: ")  # Eingabe der Beschreibung
        return name, baujahre, architekt, beschreibung  # Rückgabe der eingegebenen Daten

    def format_beschreibung(self, beschreibung):
        # Methode zur Formatierung der Beschreibung
        return "\n".join(textwrap.wrap(beschreibung, width=70))  # Text auf 70 Zeichen pro Zeile begrenzen und mit Zeilenumbrüchen formatieren

    def process_data(self, data, name, baujahre, architekt, beschreibung):
        # Methode zur Verarbeitung der Daten
        if "sehenswuerdigkeiten" not in data:
            data["sehenswuerdigkeiten"] = []  # Wenn es noch keine Sehenswürdigkeiten gibt, initialisiere eine leere Liste

        # Suche nach der Sehenswürdigkeit in den vorhandenen Daten
        for sehenswuerdigkeit in data["sehenswuerdigkeiten"]:
            if sehenswuerdigkeit["name"].lower() == name.lower():
                # Wenn die Sehenswürdigkeit bereits existiert, ergänze die Beschreibung und aktualisiere andere Felder
                if beschreibung:
                    sehenswuerdigkeit["beschreibung"] += "\n" + beschreibung
                if baujahre:
                    sehenswuerdigkeit["baujahre"] = baujahre
                if architekt:
                    sehenswuerdigkeit["architekt"] = architekt
                return  # Beende die Methode nach der Aktualisierung

        # Wenn die Sehenswürdigkeit nicht gefunden wurde, füge sie hinzu
        data["sehenswuerdigkeiten"].append({
            "name": name,
            "baujahre": baujahre,
            "architekt": architekt,
            "beschreibung": beschreibung
        })

    def write_file(self, data):
        # Methode zum Schreiben der Daten in die JSON-Datei
        with open("Tourist_Route_GDN.json", mode="w", encoding="utf-8") as file_stream:
            json.dump(data, file_stream, indent=4, ensure_ascii=False)  # Schreibe die Daten mit Einrückungen und korrekter Kodierung

    def print_data(self, data):
        # Methode zur Ausgabe der formatierten Daten im Terminal
        print(json.dumps(data, indent=4, ensure_ascii=False))  # Gebe die Daten mit Einrückungen und korrekter Kodierung aus

# Initialisierung und Ausführung des Hauptteils des Codes, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    tourist_route_gdn = TouristRouteGDN()  # Erzeuge eine Instanz der Klasse TouristRouteGDN
    tourist_route_gdn.main()  # Rufe die Hauptmethode main auf