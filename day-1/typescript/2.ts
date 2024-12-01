let leftList = []
let rightList = []
let similaritySum = 0;

const text = await Deno.readTextFile("input-1.txt").then((text: string) => text.toString())

text.split("\n").forEach((line: string) => {
    const twoNumbers = line.split("   ");

    leftList.push(parseInt(twoNumbers[0]));
    rightList.push(parseInt(twoNumbers[1]));
});

for (let i = 0; i < leftList.length; i++) {
    let timesFound = 0;

    for (let j = 0; j < rightList.length; j++) {
        if (leftList[i] === rightList[j]) {
            timesFound++;
        }
    }

    similaritySum += leftList[i] * timesFound;
}

console.log(similaritySum)