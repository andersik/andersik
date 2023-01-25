Import-Module activedirectory
Get-ADGroup -Filter * -Properties Members | where {-not $_.members} | select Name,ManagedBy

