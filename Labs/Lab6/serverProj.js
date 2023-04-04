const http = require("http");
const host = 'localhost';
const port = 8000;
const os = require('node:os');

const hostName = os.hostname();
var ip = require("ip");

const uptime = os.uptime();
var days = uptime / 86400;
var hours = (uptime - (uptime / 86400));
var minutes = hours / 60;
var seconds = minutes / 60;

const memory = os.totalmem();
var totalMemory = memory / 1000000000

const freeMemory = os.freemem();
var totalFreeMem = freeMemory / 1000000000

const roundToHundredth = (value) => {
    return Number(value.toFixed(2))
}

const cpuCount = os.cpus().length;

const IT3038CServer = function (req, res) {
    res.writeHead(200);
    res.end("My First Server!");
};

const server = http.createServer(IT3038CServer);
server.listen(port, host, () => {
    console.log("Hostname: ", hostName);
    console.log("IP: ", ip.address());
    console.log("Server Uptime: ", "Days: ", Math.floor(days), "Hours: ", Math.floor(hours), "Minutes: ", Math.floor(minutes), "Seconds: ", Math.floor(seconds))
    console.log("Total Memory: ", roundToHundredth(totalMemory));
    console.log("Free Memory: ", roundToHundredth(totalFreeMem));
    console.log("CPU's :", cpuCount);
});
