while True:
    print("\nIT-Support und Systemadmin Diagnose-Tool")
    print("===========================================")
    print("1 Neues Ticket erstellen")
    print("2 Bestehende Tickets anzeigen")
    print("3 Benutzerliste anzeigen")
    print("4 Inventarliste anzeigen")
    print("5 Logdatei durchsuchen")
    print("6 Ordner analysieren")
    print("7 Systemreport erstellen")
    print("8 Programm beenden")
    print("===========================================")

    auswahl = input("Auswahl eingeben: ")
    
    print("===========================================")


    
    if auswahl == "1":
        import csv

        print("\nNeues Ticket erstellen")

        name = input("Name: ")
        abteilung = input("Abteilung: ")
        problem = input("Problem: ")
        prioritaet = input("Priorität: ")
        status = input("Status: ")

        with open("data/tickets.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "9999",
                name,
                abteilung,
                problem,
                prioritaet,
                status
            ])

        print("Ticket wurde gespeichert.")

    
    elif auswahl == "2":
        import csv

        print("\nBestehende Tickets anzeigen")

        try:
            with open("data/tickets.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for ticket in reader:
                    print(
                        ticket["ticket_id"],
                        ticket["name"],
                        ticket["abteilung"],
                        ticket["problem"],
                        ticket["prioritaet"],
                        ticket["status"]
                    )

        except Exception as fehler:
            print("Fehler beim Lesen der Tickets:", fehler)

    
    elif auswahl == "3":
        import csv

        print("\nBenutzerliste anzeigen")

        try:
            with open("data/benutzer.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for benutzer in reader:
                    print(
                        benutzer["username"],
                        benutzer["name"],
                        benutzer["abteilung"],
                        benutzer["rolle"],
                        benutzer["status"]
                    )

                    if benutzer["status"] != "aktiv":
                        print("Achtung: Dieser Benutzer ist nicht aktiv")

        except Exception as fehler:
            print("Fehler beim Lesen der Benutzerliste:", fehler)

    
    elif auswahl == "4":
        import csv

        print("\nInventarliste anzeigen")

        try:
            with open("data/inventar.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for geraet in reader:
                    print(
                        geraet["geraete_id"],
                        geraet["geraet"],
                        geraet["benutzer"],
                        geraet["abteilung"],
                        geraet["standort"],
                        geraet["status"]
                    )

                    if geraet["status"] == "defekt" or geraet["status"] == "wartung" or geraet["status"] == "verloren":
                        print("Warnung: Dieses Gerät hat einen kritischen Status")

        except Exception as fehler:
            print("Fehler beim Lesen der Inventarliste:", fehler)

    
    elif auswahl == "5":
        print("\nLogdatei durchsuchen")

        suchwort = input("Suchwort eingeben: ")

        try:
            with open("logs/server.log", "r", encoding="utf-8") as file:
                gefunden = False

                for zeile in file:
                    if suchwort.lower() in zeile.lower():
                        print(zeile.strip())
                        gefunden = True

                if gefunden == False:
                    print("Keine passenden Zeilen gefunden.")

        except Exception as fehler:
            print("Fehler beim Lesen der Logdatei:", fehler)

    
    elif auswahl == "6":
        from pathlib import Path

        print("\nOrdner analysieren")

        try:
            pfad = Path(input("Ordnerpfad eingeben: "))

            if pfad.exists() and pfad.is_dir():
                dateien = 0
                ordner = 0

                for eintrag in pfad.iterdir():
                    if eintrag.is_file():
                        dateien = dateien + 1
                    elif eintrag.is_dir():
                        ordner = ordner + 1

                print("Dateien:", dateien)
                print("Ordner:", ordner)

            else:
                print("Der Ordner wurde nicht gefunden.")

        except Exception as fehler:
            print("Fehler bei der Ordneranalyse:", fehler)

    
    elif auswahl == "7":
        from datetime import datetime
        from pathlib import Path
        import subprocess

        print("\nSystemreport erstellen")

        try:
            Path("reports").mkdir(exist_ok=True)

            projektordner = Path.cwd()
            anzahl_dateien = 0

            for eintrag in projektordner.iterdir():
                if eintrag.is_file():
                    anzahl_dateien = anzahl_dateien + 1

            result = subprocess.run(
                ["whoami"],
                capture_output=True,
                text=True
            )

            warnungen = 0
            fehler_anzahl = 0

            with open("logs/server.log", "r", encoding="utf-8") as file:
                for zeile in file:
                    if "WARN" in zeile:
                        warnungen = warnungen + 1
                    if "ERROR" in zeile or "FAILED" in zeile:
                        fehler_anzahl = fehler_anzahl + 1

            with open("reports/system_report.txt", "w", encoding="utf-8") as report:
                report.write("Systemreport\n")
                report.write("====================\n\n")

                report.write("Datum und Uhrzeit:\n")
                report.write(str(datetime.now()) + "\n\n")

                report.write("Aktuelles Arbeitsverzeichnis:\n")
                report.write(str(Path.cwd()) + "\n\n")

                report.write("Anzahl Dateien im Projektordner:\n")
                report.write(str(anzahl_dateien) + "\n\n")

                report.write("Ergebnis eines einfachen Systembefehls:\n")
                report.write(result.stdout + "\n")

                report.write("Zusammenfassung Logdatei:\n")
                report.write("WARN gefunden: " + str(warnungen) + "\n")
                report.write("ERROR oder FAILED gefunden: " + str(fehler_anzahl) + "\n")

            print("Systemreport wurde erstellt.")

        except Exception as fehler:
            print("Fehler beim Erstellen des Systemreports:", fehler)

    
    elif auswahl == "8":
        print("Programm beendet")
        break

    else:
        print("Ungueltige Auswahl. Bitte eine Zahl von 1 bis 8 eingeben.")