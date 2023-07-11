// const url = "https://raw.githubusercontent.com/mojombo/grit/master/README.md";

// fetch(url)
//   .then((response) => {
//     if (response.ok) {
//       return response.text();
//     } else {
//       throw new Error("Failed to fetch the file.");
//     }
//   })
//   .then((data) => {
//     // Process the file data here
//     console.log(data);
//   })
//   .catch((error) => {
//     // Handle any errors that occurred during the fetch
//     console.error(error);
//   });

const fs = require("fs");

const url = "https://api.github.com/repositories";

fetch(url)
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("Failed to fetch the file.");
    }
  })
  .then((data) => {
    // Process the file data here
    console.log(data[0].description);
    fs.writeFile("./gitRepos/gitJSON.txt", JSON.stringify(data), (err) => {
      if (err) {
        console.error(err);
      }
      // file written successfully
    });
    for (let i = 0; i < data.length; i++) {
      fs.writeFile(
        `./gitRepos/descriptions/${i}`,
        JSON.stringify(data[i].description),
        (err) => {
          if (err) {
            console.error(err);
          }
          // file written successfully
        }
      );
    }
  })
  .catch((error) => {
    // Handle any errors that occurred during the fetch
    console.error(error);
  });

// const fs = require("fs");

// fs.readFile("./gitRepos/gitJSON.txt", "utf8", (err, data) => {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   let gitJSON = JSON.parse(data);
//   console.log(gitJSON);
// });
