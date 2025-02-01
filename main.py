import time
import os
import random
import datetime
import subprocess
from colorama import Fore, init

# Inisialisasi warna terminal
init(autoreset=True)
YELLOW = Fore.YELLOW
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Fore.RESET


def get_next_run_time():
    """Menghitung waktu sleep hingga besok antara jam 10:00 - 14:00."""
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    next_run_hour = random.randint(10, 14)
    next_run_time = datetime.datetime(
        tomorrow.year, tomorrow.month, tomorrow.day, next_run_hour, 0, 0
    )

    sleep_seconds = (next_run_time - now).total_seconds()
    return sleep_seconds, next_run_time.strftime("%H:%M")


def do_all_task(script_path, message):
    """Menjalankan script secara aman menggunakan subprocess."""
    try:
        print(f"{YELLOW}========== {message} =========={RESET}")
        if script_path.endswith('.py'):
            subprocess.run(["python", script_path], check=True)
        else:
            print(f"{RED}[ERROR] {script_path} bukan file Python.{RESET}")
            return
        print(f"{GREEN}========== {message} COMPLETED =========={RESET}")
    except FileNotFoundError:
        print(f"{RED}[ERROR] File not found: {script_path}{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}[EXCEPTION] Error saat menjalankan script: {str(e)}{RESET}")

scripts = [
    ('skrip/Fn.py', 'Inisiasi task Faucet native'),
    ('skrip/V_fn.py', 'Inisiasi Claim reward Faucet native'),
    ('skrip/F-eDeai.py', 'Inisiasi task Faucet Adeai'),
    ('skrip/V-f-edai.py', 'Inisiasi Claim reward Faucet Adeai'),
    ('skrip/s.py', 'Inisiasi Task send token Dan klaim rewards'),
    ('skrip/d.py', 'Inisiasi Task deploy token Dan klaim rewards')
]

while True:
    all_scripts_completed = True
    
    for script, message in scripts:
        if os.path.exists(script):
            do_all_task(script, message)
        else:
            print(f"{RED}[ERROR] {script} does not exist.{RESET}")
            all_scripts_completed = False

    if all_scripts_completed:
        ap_script = 'skrip/ap.py'
        if os.path.exists(ap_script):
            print(f"{YELLOW}========== FIXING DELAY POINTS {ap_script} =========={RESET}")
            do_all_task(ap_script, "Inisiasi FIXING DELAY POINTS")
        else:
            print(f"{RED}[ERROR] {ap_script} does not exist.{RESET}")

    print(Fore.GREEN + "Semua transaksi telah selesai!")
    
    sleep_time, next_run_str = get_next_run_time()
    print(Fore.YELLOW + f"Menunggu hingga besok sekitar pukul {next_run_str} sebelum mengulangi proses...")

    time.sleep(sleep_time)
    print(Fore.CYAN + "Memulai ulang proses...")
