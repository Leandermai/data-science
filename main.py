import numpy as np

def main():
    werte = np.array([2.1, 3.4, 1.9, 4.2, 3.3])
    print(f"Mittelwert: {werte.mean():.2f}")
    print(f"Standardabweichung: {werte.std(ddof=1):.2f}")

if __name__ == "__main__":
    main()
