#Requires -Version 5.1

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repository = 'Sulflower314/sulflower-web-design'
$archiveUri = "https://github.com/$repository/archive/refs/heads/main.zip"
$temporaryRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("sulflower-web-design-" + [Guid]::NewGuid().ToString('N'))
$archivePath = Join-Path $temporaryRoot 'repository.zip'
$extractPath = Join-Path $temporaryRoot 'extracted'
$sourcePath = Join-Path $extractPath 'sulflower-web-design-main\skill\sulflower-web-design'
$targetPath = Join-Path $env:USERPROFILE '.codex\skills\sulflower-web-design'

try {
    New-Item -ItemType Directory -Path $temporaryRoot, $extractPath -Force | Out-Null

    Write-Host 'Downloading Sulflower Web Design...' -ForegroundColor Cyan
    Invoke-WebRequest -Uri $archiveUri -OutFile $archivePath

    Expand-Archive -LiteralPath $archivePath -DestinationPath $extractPath -Force

    if (-not (Test-Path -LiteralPath $sourcePath -PathType Container)) {
        throw 'The downloaded archive does not contain the expected skill directory.'
    }

    New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
    Copy-Item -Path (Join-Path $sourcePath '*') -Destination $targetPath -Recurse -Force

    Write-Host "Installed to $targetPath" -ForegroundColor Green
    Write-Host 'Restart Codex or reload your skills before using $sulflower-web-design.' -ForegroundColor Yellow
}
finally {
    if (Test-Path -LiteralPath $temporaryRoot) {
        Remove-Item -LiteralPath $temporaryRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
