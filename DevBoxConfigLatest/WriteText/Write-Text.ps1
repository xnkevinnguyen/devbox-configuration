param(
    [Parameter()]
    [double]$DoubleParam,

    [Parameter()]
    [string]$StringParam,

    [Parameter()]
    [bool]$BoolParam,

    [Parameter()]
    [array]$ArrayParam
)

Write-Output "DoubleParam value is $DoubleParam"
Write-Output "StringParam value is $StringParam"
Write-Output "BoolParam value is $BoolParam"
Write-Output "ArrayParam value is $ArrayParam"