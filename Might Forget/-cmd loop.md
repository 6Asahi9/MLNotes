# Folder containing games
$gamesFolder = "C:\Users\Asahi\Documents\Work\Games"

# Get all .exe files recursively, ignoring zip files/folders
$exeFiles = Get-ChildItem -Path $gamesFolder -Recurse -Filter *.exe | Where-Object {
    $_.FullName -notmatch "\.zip"
}

foreach ($exe in $exeFiles) {
    # Create a unique firewall rule name for each .exe
    $ruleName = "BlockGame_" + ($exe.BaseName)

    # Check if a rule with the same name already exists
    if (-not (Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue)) {
        # Create the outbound rule to block all connections
        New-NetFirewallRule -DisplayName $ruleName `
                            -Direction Outbound `
                            -Program $exe.FullName `
                            -Action Block `
                            -Profile Any
        Write-Output "Blocked: $($exe.FullName)"
    } else {
        Write-Output "Rule already exists for: $($exe.FullName)"
    }
}
