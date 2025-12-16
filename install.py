import platform
import distro
import subprocess
import sys
from pathlib import Path
import os

if platform.system() != "Linux":
    print("Error: This Hyprdots setup is only for Linux.")
    sys.exit(1)

dist_name = distro.name(pretty=True)
print(f"Detected distribution: {dist_name}")

if "Arch" not in dist_name and "CachyOS" not in dist_name:
    print("Error: This Hyprdots setup is only for Arch-based distros (e.g., Arch Linux or CachyOS).")
    sys.exit(1)

hyprdots_dir = Path.home() / "Cachy-Hyprdots"

# Pfade zu den Skripten (angenommen: sie liegen im selben Verzeichnis wie install.py)
current_dir = Path(__file__).parent.resolve()
clone_script = current_dir / "clone-files.sh"
install_script = current_dir / "install-arch.sh"

if hyprdots_dir.exists() and hyprdots_dir.is_dir():
    print("Cachy-Hyprdots directory found. Running install-arch.sh...")
    os.chmod(install_script, 0o755)  # Ausführbar machen
    subprocess.run([str(install_script)], check=True)
else:
    print("Cachy-Hyprdots directory not found. Running clone-files.sh...")
    os.chmod(clone_script, 0o755)   # Ausführbar machen
    subprocess.run([str(clone_script)], check=True)