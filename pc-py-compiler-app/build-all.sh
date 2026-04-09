#!/bin/bash

echo "===================================="
echo "PC Py Compiler Ultra Pro v2.0"
echo "Build Script"
echo "===================================="
echo ""

echo "Installing dependencies..."
npm install

echo ""
echo "Building installers for all platforms..."
echo "This may take several minutes..."
echo ""

npm run build:all

echo ""
echo "===================================="
echo "Build Complete!"
echo "===================================="
echo ""
echo "Find your installers in the 'dist/' folder:"
echo "  - Windows: .exe installer and portable version"
echo "  - macOS: .dmg installer"
echo "  - Linux: .AppImage, .deb, .rpm"
echo ""
echo "Happy distributing! 🚀"
