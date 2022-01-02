const fs = require('fs');


function man_dist(a: number[], b: number[]): number {
    return a.map((val, i) => Math.abs(val - b[i])).reduce((acc, v) => acc + v, 0);
}


var txt = fs.readFileSync('input.txt');

var lines: string[] = txt.toString().split('\n');
var points: number[][] = lines.map(y => y.split(',').map(x => parseInt(x))).filter(a => a.length == 4);

var constellations: number = 0;

while (points.length > 0) {
    constellations++;
    var queue: number[][] = [<number[]>points.pop()];
    while (queue.length > 0) {
        let pt = <number[]>queue.shift();
        points.filter(a => man_dist(pt, a) <= 3).forEach(p => queue.push(p));
        points = points.filter(a => man_dist(pt, a) > 3);
    }
}

console.log(constellations);