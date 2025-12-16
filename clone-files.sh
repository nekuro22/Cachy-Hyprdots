#!/bin/sh
# oder
#!/bin/bash
sudo pacman -S --noconfirm git
git clone https://github.com/Junior-RoboAG-GHG/Cachy-Hyprdots.git "$HOME/Cachy-Hyprdots"
cd "$HOME/Cachy-Hyprdots"
chmod +x install-arch.sh  # Stelle sicher, dass das Skript ausführbar ist
./install-arch.sh