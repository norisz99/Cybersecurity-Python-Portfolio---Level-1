import socket
import time

def scan_ports(target_ip, ports):
    print(f"\n--- 🔍 PORT SCANNER: {target_ip} ---")
    print(f"[*] Keresés indítása...")
    
    start_time = time.time()
    
    for port in ports:
        try:
            # Létrehozunk egy internetes csatlakozót
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5) # Fél másodpercet vár max
            
            # Megpróbálunk bekopogni
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[+] ✅ Port {port} NYITVA!")
            else:
                pass # Zárt portokat nem írjuk ki, hogy ne szemeteljük tele a képernyőt
            
            sock.close()
        except KeyboardInterrupt:
            print("\nKilépés...")
            break
        except:
            pass
            
    print(f"--- Kész! Idő: {time.time() - start_time:.2f} mp ---")

if __name__ == "__main__":
    target = input("Adj meg egy IP címet (vagy domain-t, pl. google.com): ")
    # A leggyakoribb portokat vizsgáljuk
    common_ports = range(1, 1025)
    
    scan_ports(target, common_ports)
    input("\nNyomj Entert a kilépéshez...")
