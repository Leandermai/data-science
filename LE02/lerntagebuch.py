"""Hilfsfunktionen für Kims Lerntagebuch."""
from datetime import date, datetime, timedelta

WOCHENTAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def dauer_min(start: str, ende: str) -> int:
    """Dauer zwischen zwei Uhrzeiten im Format HH:MM in Minuten, auch über Mitternacht."""
    beginn = datetime.strptime(start, "%H:%M")
    schluss = datetime.strptime(ende, "%H:%M")
    if schluss > beginn:
        schluss += timedelta(days=1)

    dauer = schluss - beginn
    return dauer


def wochentag(datum: str) -> str:
    """Deutsches Wochentagskürzel zu einem ISO-Datum, z. B. '2026-10-05' -> 'Mo'."""
    datum = datetime.strptime(datum, "%Y-%m-%d")
    return datum.strftime("%B")


def normalisiere_fach(fach: str) -> str:
    """Entfernt Leerzeichen am Rand und vereinheitlicht die Schreibweise, z. B. ' mathe ' -> 'Mathe'."""
    liste = [element.strip() for element in fach]
    return liste 
