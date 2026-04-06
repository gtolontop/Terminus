const fs = require("fs");
const vm = require("vm");

function extractDialog(html) {
  const marker = "var dialog={";
  const start = html.indexOf(marker);
  if (start < 0) {
    throw new Error("dialog object not found");
  }

  let index = start + "var dialog=".length;
  let depth = 0;
  let inString = false;
  let quote = "";
  let escaped = false;

  for (; index < html.length; index += 1) {
    const char = html[index];

    if (inString) {
      if (escaped) {
        escaped = false;
        continue;
      }
      if (char === "\\") {
        escaped = true;
        continue;
      }
      if (char === quote) {
        inString = false;
        quote = "";
      }
      continue;
    }

    if (char === '"' || char === "'") {
      inString = true;
      quote = char;
      continue;
    }

    if (char === "{") {
      depth += 1;
      continue;
    }

    if (char === "}") {
      depth -= 1;
      if (depth === 0) {
        index += 1;
        break;
      }
    }
  }

  const source = html.slice(start + "var dialog=".length, index);
  return vm.runInNewContext("(" + source + ")");
}

function main() {
  const inputPath = process.argv[2] || "Terminus.html";
  const outputPath = process.argv[3];
  const html = fs.readFileSync(inputPath, "utf8");
  const dialog = extractDialog(html);

  if (outputPath) {
    fs.writeFileSync(outputPath, JSON.stringify(dialog, null, 2));
    console.log("dialog extracted to " + outputPath);
    return;
  }

  const keys = Object.keys(dialog).sort();
  console.log("entries:", keys.length);
  for (const key of keys) {
    console.log(key);
  }
}

main();
