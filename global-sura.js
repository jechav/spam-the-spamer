const { faker, fakerES_MX } = require("@faker-js/faker");
const { exec } = require("child_process");

// Get the delay by reading the command line arguments
const args = process.argv.slice(2);
const delayInSeconds = parseInt(args[0], 10) || 3;
const delay = delayInSeconds * 1000; // Convert to milliseconds
console.log(`Delay between requests: ${delayInSeconds} seconds`);

const maxCount = parseInt(args[1], 10) || 100; // Default to 100 if not provided
console.log(`Maximum count of requests: ${maxCount}`);

// function to get the number of times the script has been run from a global counter
// using a file to store the counter
const getGlobalCounter = () => {
  const fs = require("fs");
  const counterFile = "counter.txt";
  let counter = 0;

  if (fs.existsSync(counterFile)) {
    const data = fs.readFileSync(counterFile, "utf8");
    counter = parseInt(data, 10);
  }

  counter++;
  fs.writeFileSync(counterFile, counter.toString(), "utf8");
  return counter;
};

const setGlobalCounter = (value) => {
  const fs = require("fs");
  const counterFile = "counter.txt";
  fs.writeFileSync(counterFile, value.toString(), "utf8");
};

function serialize(data) {
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(data)) {
    params.append(key, value);
  }
  return params.toString();
}

async function sendData(dataObject) {
  const res = await fetch("https://globalsura.com/cnr/post2.php", {
    headers: {
      accept:
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "accept-language": "en-US,en;q=0.9,es;q=0.8",
      "cache-control": "max-age=0",
      "content-type": "application/x-www-form-urlencoded",
      priority: "u=0, i",
      "sec-ch-ua": faker.helpers.arrayElement([
        '"Google Chrome";v="120", "Not)A;Brand";v="8", "Chromium";v="120"',
        '"Microsoft Edge";v="120", "Not)A;Brand";v="8", "Chromium";v="120"',
        '"Brave";v="120", "Not)A;Brand";v="8", "Chromium";v="120"',
      ]),
      "sec-ch-ua-mobile": faker.helpers.arrayElement(["?0", "?1"]),
      "sec-ch-ua-platform": faker.helpers.arrayElement([
        '"Windows"',
        '"macOS"',
        '"Linux"',
      ]),
      "sec-fetch-dest": "document",
      "sec-fetch-mode": "navigate",
      "sec-fetch-site": "same-origin",
      "sec-fetch-user": "?1",
      "upgrade-insecure-requests": "1",
      Referer: "https://globalsura.com/cnr/index1.php",
    },
    body: serialize(dataObject),
    method: "POST",
  });

  // const responseText = await res.text();
  // console.log("responseText", responseText);
  console.log("headers", res.headers);
  console.log("status", res.status);
  console.log("ok", res.ok);
  console.log("redirected", res.redirected);
  console.log("url", res.url);
  if (!res.ok) {
    console.error("Error sending data:", res.status, res.statusText);
  }
}

function generateRandomData() {
  const dataObject = {
    cardNumber: faker.finance.creditCardNumber(),
    expirationDate: faker.date.future().toLocaleDateString("en-US", {
      month: "2-digit",
      year: "2-digit",
    }),
    cvv: faker.finance.creditCardCVV(),
    fullName: fakerES_MX.person.fullName(),
  };

  return dataObject;
}

let currentCount = 0;
function startSendingData(counter) {
  let globalCounter = counter;
  setInterval(async () => {
    const dataObject = generateRandomData();
    console.log("Sending:", dataObject, `(Count: ${globalCounter})`);
    await sendData(dataObject);
    console.log("Waiting for 2 seconds before sending the next data...");
    console.log("--------------------------------------------------");
    globalCounter++;
    setGlobalCounter(globalCounter);
    currentCount++;
    if (currentCount >= maxCount) {
      console.log(
        `Reached the maximum count of ${maxCount}. Stopping the script.`,
      );
      process.exit(0);
    }
  }, delay);
}

const globalCounter = getGlobalCounter();
startSendingData(globalCounter);
