[Code]




#define MyAppName "LLG"
#define MyAppVersion "2.0"
#define MyAppExeName "llg_progam_leguage.exe"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\LLG
DefaultGroupName={#MyAppName}
OutputBaseFilename=LLG-Setup
Compression=lzma
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin

[Files]
; opcional: se ainda quiser incluir o .exe gerado
Source: "dist\llg.exe"; DestDir: "{app}"; Flags: ignoreversion
; incluir o script Python e o batch wrapper
Source: "llg.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "llg.bat"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\LLG"; Filename: "{app}\llg.bat"; WorkingDir: "{app}"

[Run]
Filename: "{app}\llg.bat"; Description: "Executar LLG"; Flags: nowait postinstall skipifsilent


