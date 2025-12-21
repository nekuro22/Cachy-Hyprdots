#!/bin/bash
echo "Starting Installation of Cachy-HyprDots"

sudo pacman -S --needed hyprland yay git

cd ~/Cachy-Hyprdots || exit 1
git fetch origin
git pull origin main

mkdir -p ~/.config/hypr
cp ~/Cachy-Hyprdots/hyprdots/hyprland.conf ~/.config/hypr/hyprland.conf

echo "Installation finished, you may reboot your device and boot into Hyprland now."
