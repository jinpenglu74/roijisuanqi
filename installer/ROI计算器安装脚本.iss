[Setup]
AppName=ROI智能计算器
AppVersion=1.1.0
DefaultDirName={autopf}\ROI智能计算器
OutputBaseFilename=ROI智能计算器_Setup_V1.1.0

[Files]
Source: "..\release\ROI智能计算器.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\ROI智能计算器"; Filename: "{app}\ROI智能计算器.exe"
Name: "{commondesktop}\ROI智能计算器"; Filename: "{app}\ROI智能计算器.exe"

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
