$search = "snasite"
$replace = "snasite1"

Get-ChildItem -Recurse -Include *.py, *.html | ForEach-Object {
    $content = Get-Content $_.FullName
    $newContent = $content -replace $search, $replace
    Set-Content $_.FullName $newContent
}