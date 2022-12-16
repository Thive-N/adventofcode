use std::fs;
use std::time::Instant;

fn main() {
    let now = Instant::now();

    let input = fs::read_to_string("2022-15").unwrap();

    let mut sensors = Vec::new();
    let mut beacons = Vec::new();

    for line in input.lines() {
        let parts: Vec<_> = line.split(' ').collect();
        let lx = parts[2].split('=').last().unwrap();
        let lx = lx[0..lx.len() - 1].parse::<i64>().unwrap();

        let ly = parts[3].split('=').last().unwrap();
        let ly = ly[0..ly.len() - 1].parse::<i64>().unwrap();

        let bx = parts[8].split('=').last().unwrap();
        let bx = bx[0..bx.len() - 1].parse::<i64>().unwrap();

        let by = parts[9].split('=').last().unwrap().parse::<i64>().unwrap();

        sensors.push((lx, ly));
        beacons.push((bx, by));
    }

    let N = sensors.len();
    let mut dists = Vec::new();
    let mut pos_lines = Vec::new();
    let mut neg_lines = Vec::new();

    for i in 0..N - 1 {
        dists.push(dist(sensors[i], beacons[i]));
        neg_lines.push(sensors[i].0 + sensors[i].1 - dists[i]);
        neg_lines.push(sensors[i].0 + sensors[i].1 + dists[i]);

        pos_lines.push(sensors[i].0 - sensors[i].1 - dists[i]);
        pos_lines.push(sensors[i].0 - sensors[i].1 + dists[i]);
    }

    let mut pos: i64 = i64::MAX;
    let mut neg: i64 = i64::MAX;
    let mut a: i64;
    let mut b: i64;
    let mut c: i64;
    let mut d: i64;

    for i in 0..(N * 2) {
        for j in i + 1..(N * 2) - 2 {
            a = pos_lines[i];
            b = pos_lines[j];

            if (a - b).abs() == 2 {
                pos = i64::min(a, b) + 1
            }
            c = neg_lines[i];
            d = neg_lines[j];
            if (c - d).abs() == 2 {
                neg = i64::min(c, d) + 1
            }
        }
    }
    let ans = ((pos + neg) / 2) * 4000000 + ((neg - pos) / 2);
    let elapsed = now.elapsed();
    println!("total time Elapsed: {:.2?}", elapsed);
    println!("{}", ans);
}

fn dist(a: (i64, i64), b: (i64, i64)) -> i64 {
    (a.0 - b.0).abs() + (a.1 - b.1).abs()
}
