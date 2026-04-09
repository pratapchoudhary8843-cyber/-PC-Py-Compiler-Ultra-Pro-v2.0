# 📁 PC Py Compiler Ultra Pro - File Structure

## Complete Application Package

```
pc-py-compiler-app/
│
├── 📄 main.js                  # Electron main process
├── 📄 preload.js               # IPC communication bridge
├── 📄 index.html               # Application UI (IDE interface)
├── 📄 package.json             # Dependencies & build config
│
├── 📁 assets/
│   ├── icon.png                # Application icon (512x512)
│   └── icon.svg                # Vector icon source
│
├── 📄 README.md                # Main documentation
├── 📄 INSTALL.md               # Installation guide
├── 📄 FEATURES.md              # Complete features list
├── 📄 LICENSE                  # MIT License
│
├── 🚀 start.sh                 # Linux/Mac launcher
├── 🚀 start.bat                # Windows launcher
├── 🔨 build-all.sh             # Build for all platforms
├── 🔨 build-windows.bat        # Build for Windows
│
└── 📄 .gitignore               # Git ignore rules
```

## 📦 After Installation

After running `npm install`, you'll also have:

```
├── 📁 node_modules/            # Installed dependencies (auto-generated)
└── 📄 package-lock.json        # Dependency lock file (auto-generated)
```

## 🏗️ After Building

After running build commands, you'll get:

```
├── 📁 dist/                    # Build output directory
│   ├── win-unpacked/           # Windows unpacked files
│   ├── *.exe                   # Windows installer
│   ├── *.dmg                   # macOS installer
│   ├── *.AppImage              # Linux AppImage
│   ├── *.deb                   # Debian/Ubuntu package
│   └── *.rpm                   # RedHat/Fedora package
```

## 🎯 Key Files Explained

### main.js
- Electron main process
- Creates application window
- Handles menu system
- Manages file operations
- Native dialog integration

### preload.js
- Secure IPC bridge
- Connects renderer to main process
- Exposes safe APIs to web interface
- Handles menu event routing

### index.html
- Complete IDE user interface
- Code editor
- Output panels (Console, Plots, Errors)
- Sidebar with samples
- Toolbar with controls
- Pyodide integration
- All JavaScript logic

### package.json
- Application metadata
- NPM dependencies
- Build scripts
- Electron-builder configuration
- Platform-specific settings

## 📋 File Purposes

| File | Purpose | Edit? |
|------|---------|-------|
| main.js | App window & menus | Yes, for customization |
| preload.js | Security bridge | Rarely |
| index.html | UI & IDE logic | Yes, for features |
| package.json | Config & deps | Yes, for settings |
| README.md | Documentation | Yes, for info |
| assets/icon.png | App icon | Yes, for branding |

## 🔧 Configuration Files

### package.json - Key Sections

```json
{
  "name": "pc-py-compiler-ultra-pro",
  "version": "2.0.0",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder"
  }
}
```

### Window Settings (main.js)

```javascript
width: 1600,
height: 1000,
minWidth: 1200,
minHeight: 700
```

### Theme Colors (index.html CSS)

```css
--accent-cyan: #00f3ff;
--accent-pink: #ff006e;
--accent-purple: #8b5cf6;
```

## 🎨 Customization Points

### Change App Name
1. Edit `package.json` → `"name"` and `"productName"`
2. Edit `index.html` → `<h1>` tag
3. Edit `main.js` → `About` dialog

### Change Colors
1. Edit `index.html` → CSS `:root` variables
2. Update gradient definitions

### Change Window Size
1. Edit `main.js` → `createWindow()` function
2. Adjust `width`, `height`, `minWidth`, `minHeight`

### Add Menu Items
1. Edit `main.js` → `createMenu()` function
2. Add to template array

### Modify Shortcuts
1. Edit `main.js` → `accelerator` values in menu
2. Edit `index.html` → keyboard event listeners

## 📚 Dependencies

### Production
- **electron**: Desktop app framework
- None (Pyodide loads from CDN)

### Development
- **electron-builder**: Creates installers

### Runtime (CDN)
- **Pyodide**: Python WebAssembly runtime
- **NumPy**: Via Pyodide
- **Pandas**: Via Pyodide
- **Matplotlib**: Via Pyodide

## 🚀 Quick Commands

```bash
# Development
npm start                  # Run app in dev mode

# Building
npm run build             # Build for current platform
npm run build:win         # Build Windows installer
npm run build:mac         # Build macOS installer
npm run build:linux       # Build Linux packages
npm run build:all         # Build all platforms

# Scripts
./start.sh               # Quick start (Linux/Mac)
start.bat                # Quick start (Windows)
./build-all.sh          # Build all (Linux/Mac)
build-windows.bat       # Build Windows
```

## 📦 Installer Sizes

Approximate file sizes:

- **Windows .exe**: ~100-150 MB
- **macOS .dmg**: ~120-180 MB
- **Linux .AppImage**: ~110-160 MB
- **Linux .deb**: ~100-150 MB
- **Linux .rpm**: ~100-150 MB

Sizes include:
- Electron runtime (~50-70 MB)
- Chromium engine (~50-80 MB)
- Application code (~1-5 MB)

## 🔐 Security Notes

### preload.js
- Implements context isolation
- Only exposes necessary APIs
- Prevents direct Node.js access from renderer

### index.html
- No nodeIntegration
- Content Security Policy ready
- Safe IPC communication only

## 📝 License

MIT License - See LICENSE file for full text.

## 🎯 Next Steps

1. **Customize**: Edit colors, name, icon as needed
2. **Test**: Run with `npm start`
3. **Build**: Create installer with `npm run build`
4. **Distribute**: Share installers from `dist/` folder

---

**Your complete desktop Python IDE is ready!** 🎉

All files are organized and documented.
Everything is working and tested.
Ready to use, customize, and distribute!
