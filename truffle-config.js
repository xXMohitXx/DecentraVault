const path = require("path");
const fs = require("fs");
const solc = require("solc");

module.exports = {
    networks: {
        development: {
            host: "127.0.0.1",
            port: 7545, // Replace with your Ganache port if different
            network_id: "*", // Match any network id
        },
    },
    compilers: {
        solc: {
            version: "0.8.0", // Specify the compiler version
        },
    },
};
