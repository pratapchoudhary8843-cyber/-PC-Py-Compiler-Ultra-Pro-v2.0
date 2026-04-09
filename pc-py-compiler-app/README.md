# PC Py Compiler Ultra Pro v2.0

![PC Py Compiler Ultra Pro](assets/icon.png)

## 🚀 Advanced Python IDE for Desktop

PC Py Compiler Ultra Pro is a powerful, browser-based Python IDE packaged as a standalone desktop application. Run Python code directly in your browser using Pyodide - no server required!

## ✨ Features

### 🎯 Core Features
- **Full Python 3.11 Support** - Powered by Pyodide
- **Instant Execution** - Run code directly in your browser
- **No Server Required** - Completely client-side execution
- **Cross-Platform** - Works on Windows, macOS, and Linux

### 📦 Pre-installed Packages
- NumPy - Numerical computing
- Pandas - Data analysis
- Matplotlib - Data visualization
- Scikit-learn - Machine learning

### 🎨 Advanced IDE Features
- **Tabbed Output System**
  - Console output
  - Matplotlib plot rendering
  - Error display with syntax highlighting
  
- **Code Samples Library**
  - Basic Python examples
  - NumPy array operations
  - Pandas DataFrames
  - Matplotlib visualizations
  - Seaborn advanced plots
  - Algorithm implementations
  - Machine learning demos

- **Professional Editor**
  - Syntax preservation
  - Tab support (4 spaces)
  - Copy/paste functionality
  - Keyboard shortcuts

- **Package Manager**
  - Install additional Pyodide packages
  - Visual package status indicators
  - One-click installation

### ⌨️ Keyboard Shortcuts
- `Ctrl/Cmd + Enter` - Run code
- `Ctrl/Cmd + N` - New file
- `Ctrl/Cmd + O` - Open file
- `Ctrl/Cmd + S` - Save file
- `Ctrl/Cmd + Shift + S` - Save as
- `F5` - Run code
- `Ctrl/Cmd + K` - Clear output
- `Ctrl/Cmd + Q` - Quit application

## 📥 Installation

### Prerequisites
- Node.js 16.x or higher
- npm or yarn

### Quick Start

1. **Clone or download this repository**
   ```bash
   cd pc-py-compiler-app
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the application**
   ```bash
   npm start
   ```

### Building Executables

Build standalone executables for your platform:

#### Windows
```bash
npm run build:win
```
Creates: `.exe` installer and portable version in `dist/`

#### macOS
```bash
npm run build:mac
```
Creates: `.dmg` installer and `.zip` in `dist/`

#### Linux
```bash
npm run build:linux
```
Creates: `.AppImage`, `.deb`, and `.rpm` packages in `dist/`

#### All Platforms
```bash
npm run build:all
```
Creates installers for Windows, macOS, and Linux

## 🎮 Usage

### Running Your First Program

1. Launch the application
2. Type your Python code in the editor:
   ```python
   print("Hello, PC Py Compiler Ultra Pro!")
   ```
3. Click **Run Code** or press `Ctrl/Cmd + Enter`
4. View output in the Console tab

### Using Code Samples

1. Click any sample button in the sidebar:
   - 🐍 Basic Python
   - 🔢 NumPy Arrays
   - 📊 Pandas DataFrame
   - 📈 Matplotlib Plot
   - 🎨 Seaborn Viz
   - ⚡ Algorithms
   - 🤖 Machine Learning

2. The sample code loads automatically
3. Click **Run Code** to execute

### Creating Visualizations

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.grid(True)
```

Click **Run Code** - the plot automatically appears in the **Plots** tab!

### Installing Additional Packages

1. Click **📦 Install Package** button
2. Enter package name (e.g., `scipy`, `seaborn`, `sympy`)
3. Click **Install**
4. Use the package in your code

## 📊 Supported Packages

Pre-installed:
- numpy
- pandas
- matplotlib
- scikit-learn

Available for installation:
- scipy
- sympy
- seaborn
- pillow
- beautifulsoup4
- And many more from Pyodide's package list

## 🔧 Configuration

### Custom Themes
Edit the CSS variables in `index.html`:
```css
:root {
    --accent-cyan: #00f3ff;
    --accent-pink: #ff006e;
    --accent-purple: #8b5cf6;
}
```

### Window Size
Edit `main.js`:
```javascript
width: 1600,
height: 1000,
```

## 🐛 Troubleshooting

### Python runtime fails to initialize
- Check your internet connection (Pyodide loads from CDN)
- Try restarting the application
- Clear browser cache (Ctrl+Shift+Delete)

### Package installation fails
- Verify the package is available in Pyodide
- Check package name spelling
- Some packages may not be compatible with Pyodide

### Plots don't appear
- Ensure you're using `matplotlib.pyplot` as `plt`
- Check that the Plots tab is selected
- Make sure to create the plot before calling `plt.show()`

## 📝 Development

### Project Structure
```
pc-py-compiler-app/
├── main.js          # Electron main process
├── preload.js       # Preload script for IPC
├── index.html       # Application UI
├── package.json     # Dependencies and build config
├── assets/          # Icons and resources
│   └── icon.png
└── README.md        # This file
```

### Technologies Used
- **Electron** - Desktop app framework
- **Pyodide** - Python runtime for WebAssembly
- **HTML/CSS/JS** - User interface
- **Matplotlib** - Visualization
- **NumPy/Pandas** - Data processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

MIT License - feel free to use this project for any purpose.

## 🎯 Roadmap

- [ ] Multi-file project support
- [ ] Code completion and IntelliSense
- [ ] Debugger integration
- [ ] Git integration
- [ ] Themes customization UI
- [ ] Plugin system
- [ ] Collaborative coding features

## 💬 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Consult Pyodide documentation for package compatibility

## 🙏 Acknowledgments

- Pyodide team for Python in the browser
- Electron team for the desktop framework
- All open-source contributors

---

**Made with ❤️ for Python developers**

Version 2.0 | © 2026 PC Py Compiler Team
