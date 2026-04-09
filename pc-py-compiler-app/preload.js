const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
    // File operations
    saveFileDialog: (content) => ipcRenderer.invoke('save-file-dialog', content),
    
    // Listen to menu events
    onNewFile: (callback) => ipcRenderer.on('new-file', callback),
    onLoadFile: (callback) => ipcRenderer.on('load-file', (event, data) => callback(data)),
    onSaveFile: (callback) => ipcRenderer.on('save-file', callback),
    onSaveFileAs: (callback) => ipcRenderer.on('save-file-as', callback),
    onRunCode: (callback) => ipcRenderer.on('run-code', callback),
    onRunSelected: (callback) => ipcRenderer.on('run-selected', callback),
    onClearOutput: (callback) => ipcRenderer.on('clear-output', callback),
    onFind: (callback) => ipcRenderer.on('find', callback),
    
    // Cleanup
    removeAllListeners: (channel) => ipcRenderer.removeAllListeners(channel)
});
