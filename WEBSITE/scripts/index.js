const API_URL = "https://jeuxgratuits-api.herokuapp.com/";

console.log("hello world");

async function fetchGames() {
  const reply = await fetch(API_URL);
  const data = await reply.json();
  return data;
}

function buildGameHtml(game) {
  return `
        <a class="game" href="${game.gameLink}">
          <img
            src="${game.imageURL}"
            alt=""
          />
          <h2>${game.name}</h2>
        </a>
    `;
}

async function loadGames() {
  console.log("loading games");
  const games = await fetchGames();

  const steamContainer = document.querySelector("#steam-container");
  const epicGamesContainer = document.querySelector("#epic-games-container");

  for (const game of games) {
    if (game.platform === "steam") {
      steamContainer.innerHTML += buildGameHtml(game);
    } else if (game.platform === "epic games") {
      epicGamesContainer.innerHTML += buildGameHtml(game);
    }
  }
}

loadGames();
