# 🚀 Quick Installation Guide

## For Windows Users

### Method 1: Using the Start Script (Easiest)
1. Double-click `start.bat`
2. Wait for dependencies to install
3. Application will launch automatically!

### Method 2: Manual Installation
1. Open Command Prompt in this folder
2. Run: `npm install`
3. Run: `npm start`

### Method 3: Build Installer
1. Open Command Prompt in this folder
2. Run: `npm install`
3. Run: `npm run build:win`
4. Find the installer in `dist/` folder
5. Install and run!

---

## For macOS Users

### Method 1: Using the Start Script (Easiest)
1. Open Terminal in this folder
2. Run: `./start.sh`
3. Application will launch automatically!

### Method 2: Manual Installation
1. Open Terminal in this folder
2. Run: `npm install`
3. Run: `npm start`

### Method 3: Build Installer
1. Open Terminal in this folder
2. Run: `npm install`
3. Run: `npm run build:mac`
4. Find the .dmg in `dist/` folder
5. Install and run!

---

## For Linux Users

### Method 1: Using the Start Script (Easiest)
1. Open Terminal in this folder
2. Run: `./start.sh`
3. Application will launch automatically!

### Method 2: Manual Installation
1. Open Terminal in this folder
2. Run: `npm install`
3. Run: `npm start`

### Method 3: Build Installer
1. Open Terminal in this folder
2. Run: `npm install`
3. Run: `npm run build:linux`
4. Find .AppImage, .deb, or .rpm in `dist/` folder
5. Install and run!

---

## Prerequisites

Before installation, make sure you have:
- **Node.js** (version 16 or higher)
  - Download from: https://nodejs.org/
  - Verify: Run `node --version` in terminal

- **npm** (comes with Node.js)
  - Verify: Run `npm --version` in terminal

---

## First Time Setup

After installation:
1. The app will load Python runtime (takes ~10 seconds)
2. Green status dot means Python is ready
3. Try running the default example code
4. Explore code samples in the sidebar
5. Enjoy coding! 🎉

---

## Troubleshooting

### "npm: command not found"
- Install Node.js from https://nodejs.org/

### Permission denied (Linux/macOS)
- Run: `chmod +x start.sh`
- Or use sudo: `sudo ./start.sh`

### App won't start
1. Delete `node_modules/` folder
2. Run `npm install` again
3. Try `npm start`

### Python won't initialize
- Check internet connection (Pyodide downloads on first run)
- Restart the application
- Clear cache and try again

---

## Need Help?

Check the main README.md for detailed documentation!

Happy coding! 🚀
