#!/bin/sh
# oder
#!/bin/bash
echo "Starte Installation der Hyprdots-Konfiguration..."
sudo pacman -S hyprland
sudo pacman -S yay
sudo pacman -S git

cd ~/Cachy-Hyprdots
git fetch origin
git pull origin main

sudo cp ~/Cachy-Hyprdots/hyprdots/hyprland.conf ~/.config/hypr/hyprland.conf
#usw