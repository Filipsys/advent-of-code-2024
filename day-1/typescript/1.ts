let leftList = []
let rightList = []
let diffSum = 0;

const text = await Deno.readTextFile("input-1.txt").then((text: string) => text.toString())

text.split("\n").forEach((line: string) => {
    const twoNumbers = line.split("   ");

    leftList.push(parseInt(twoNumbers[0]));
    rightList.push(parseInt(twoNumbers[1]));
});

leftList.sort((a, b) => a - b);
rightList.sort((a, b) => a - b);

for (let i = 0; i < leftList.length; i++) {
    diffSum += Math.abs(leftList[i] - rightList[i]);
}

console.log(diffSum)