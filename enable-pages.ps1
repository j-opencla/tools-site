$token = & "D:\QClaw\resources\openclaw\config\skills\github-skill\get-token.ps1"
$body = @{
    source = @{ branch = "master" }
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "https://api.github.com/repos/j-opencla/tools-site/pages" -Method POST -Headers @{
    "Authorization" = "Bearer $token"
    "X-GitHub-Api-Version" = "2022-11-28"
    "Accept" = "application/vnd.github+json"
} -Body $body -ContentType "application/json"

$response