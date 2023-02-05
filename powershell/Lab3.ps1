function getIP{
    (get-netipaddress).IPv4Address | Select-String "192"
    }

function getVersion{
    $HOST.version
    }

function getDate{
    Get-Date -Format "dddd MM yyyy"
    }

function getHost{
    hostname}


$IP = getIP
$HOSTNAME = getHost
$GETDATE = getDate
$VERSION = getVersion
$BODY = "This machine's IP is $IP. User is $env:USERNAME. The host is $HOSTNAME. PowerShell version $VERSION, Todays date is, $GETDATE"


Send-MailMessage -To "leonardf@mail.uc.edu" -From "brownie.jakob123@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)