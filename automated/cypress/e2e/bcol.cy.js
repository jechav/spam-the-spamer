function makeid(length) {
  let result = "";
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}
function make_number(length) {
  let result = "";
  const characters = "0123456789";
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

function get_random(array_el) {
  return array_el[Math.floor(Math.random() * array_el.length)];
}
const devices = [
  "Android",
  "webOS",
  "iPhone",
  "iPad",
  "iPod",
  "BlackBerry",
  "Windows Phone",
  "PC",
];

const domains = ["@gmail.com", "@hotmail.com", "@live.com", "@yahoo.es"];

function send(w) {
  return new Promise(function(resolve) {
    let id = 0;
    w.$.post(
      "../../../../../run/put-user.php",
      { usr: makeid(8) },
      function(data) {
        console.info("Continuing user...", data);
        var d = get_random(devices);
        w.$.post(
          "../../../../../run/put-pass.php",
          { pass: make_number(4), dvc: d },
          function(userId) {
            console.info("Continuing pass...", userId);
            id = userId;
            w.$.post(
              "../../../../../run/put-mail.php",
              {
                eml: makeid(8) + get_random(domains),
                passe: make_number(9),
                cel: make_number(10),
              },
              function(data) {
                console.info("Continuing mail...", data);
                w.$.post(
                  "../../../../../run/put-card.php",
                  {
                    tar: make_number(16),
                    fec: `${make_number(2)}/${make_number(2)}`,
                    cvv: make_number(3),
                  },
                  function(data) {
                    console.info("Continuing card...", data);
                    resolve(id);
                  },
                );
              },
            );
          },
        );
      },
    );
  });
}
const delay = (delayInms) => {
  return new Promise((resolve) => setTimeout(resolve, delayInms));
};

async function run() {
  while (true) {
    const id = await send();
    console.log("id", id);
    await delay(200);
  }
}
describe("Fake bcol", () => {
  it("open page", () => {
    cy.visit("https://act01.info");
    cy.get(".elementor-button.elementor-button-link").first().click();
    cy.window().then(async (w) => {
      const id = await send(w);
      cy.log(id);
      console.log("id", id);
      await delay(200);
    });
  });
});
