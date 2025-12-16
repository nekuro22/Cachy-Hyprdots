import platform
import distro
import subprocess
import sys
from pathlib import Path

if platform.system() != "Linux":
    print("Error: This Hyprdots setup is only for Linux.")
    sys.exit(1)

dist_name = distro.name(pretty=True)
print(f"Detected distribution: {dist_name}")

# Prüfen, ob die Distribution Arch-basiert ist
if "Arch" not in dist_name and "CachyOS" not in dist_name:
    print("Error: This Hyprdots setup is only for Arch-based distros (e.g., Arch Linux or CachyOS).")
    sys.exit(1)

# Pfad zum Cachy-Hyprdots-Verzeichnis im Home-Ordner
hyprdots_dir = Path.home() / "Cachy-Hyprdots"

# Entscheiden, welches Skript ausgeführt werden soll
if hyprdots_dir.exists() and hyprdots_dir.is_dir():
    print("Cachy-Hyprdots directory found. Running install-arch.sh...")
    subprocess.run(["./install-arch.sh"], check=True)
else:
    print("Cachy-Hyprdots directory not found. Running clone-files.sh...")
    subprocess.run(["./clone-files.sh"], check=True)