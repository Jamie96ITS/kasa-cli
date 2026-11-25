# kasa-cli
 A command-line application (standalone executable) for TP-Link Kasa Smarthome products like smart WiFi switches and more.

 Note: there's really not much to this project except for build scripts:

 - The code is simply a wrapper around the awesome [python-kasa](https://github.com/python-kasa/python-kasa) library.
 - The Windows executable is built with [Nuitka](https://github.com/Nuitka/Nuitka) and the latest pinned release of [python-kasa](https://github.com/python-kasa/python-kasa).
 
# Installation

- Download the EXE from the [latest successful Windows build](https://github.com/Jamie96ITS/kasa-cli/actions/workflows/windows-exe.yml)
- Call the EXE from the command line, as shown in the examples below 👇🏻

# Example Usage
Turn Switch OFF  
`.\kasa_cli.exe --host 192.168.1.118 off`

Turn Switch ON  
`.\kasa_cli.exe --host 192.168.1.118 on`  

See [python-kasa > Command-line usage](https://python-kasa.readthedocs.io/en/latest/cli.html) for more full details.

`.\kasa_cli.exe --help`

The Windows executable is built by the [Build-Windows-Exe workflow](.github/workflows/windows-exe.yml). Download it from that workflow run's artifacts.
