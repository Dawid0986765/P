import bluetooth

def scan_devices():
    print("Skanowanie urządzeń Bluetooth...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    print("Znalezione urządzenia Bluetooth:")
    for addr, name in nearby_devices:
        print(f"Adres: {addr}, Nazwa: {name}")
    return nearby_devices

def select_target(nearby_devices):
    target_name = input("Podaj nazwę słuchawek, które chcesz zaatakować: ")
    target_address = None
    for addr, name in nearby_devices:
        if name == target_name:
            target_address = addr
            break
    return target_address

def bluetooth_attack(target_address):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        sock.connect((target_address, 1))
        print("Połączono pomyślnie! Teraz wysyłaj jakieś złośliwe dane...")
        # Tutaj możesz wysłać swoje złośliwe dane
        sock.close()
        print("Atak udany! Słuchawki twojego kumpla będą teraz wariować!")
    except Exception as e:
        print("Błąd:", e)

def main_menu():
    print("Wybierz opcję:")
    print("1. Zeskanuj urządzenia Bluetooth")
    print("2. Wybierz słuchawki do ataku")
    print("3. Wyjdź")

def main():
    while True:
        main_menu()
        choice = input("Podaj numer opcji: ")
        if choice == '1':
            nearby_devices = scan_devices()
        elif choice == '2':
            if nearby_devices:
                target_address = select_target(nearby_devices)
                if target_address:
                    bluetooth_attack(target_address)
                else:
                    print("Nie znaleziono słuchawek o podanej nazwie.")
            else:
                print("Najpierw wykonaj skanowanie urządzeń Bluetooth.")
        elif choice == '3':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
