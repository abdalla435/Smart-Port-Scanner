import socket
import requests
import threading

thread_count = 0
max_threads = 1000  # All Rights Going To Abdalla Gaming. 
def port_scanner(host, port):
    global thread_count
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            try:
                response = requests.get(f"http://{host}:{port}", timeout=0.5)
                if "Apache" in response.headers.get("Server", ""):
                    print(f"{port} Port: Apache2 detected")
                elif "XMPP" in response.headers.get("Server", ""):
                    print(f"{port} Port: XMPP detected")
                else:
                    print(f"{port} Port: Unknown port detected")
            except:
                pass
    except socket.timeout:
        print("Connection timed out")
    except socket.error:
        print("Host could not be reached")
    s.close()
    thread_count -= 1

def port_scanner_thread(host, port):
    global thread_count
    while thread_count >= max_threads:
        pass
    thread_count += 1
    thread = threading.Thread(target=port_scanner, args=(host, port))
    thread.start()

host = input("Enter the host to scan: ")

for port in range(1, 65536):
    port_scanner_thread(host, port)
