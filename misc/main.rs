use std::time::Instant;

pub fn get_device_coordinates(input: &str) -> (i64, i64) {
    let device_split = input.split(" at ").last().unwrap();
    let x = device_split
        .split(", ")
        .next()
        .unwrap()
        .split('=')
        .last()
        .unwrap()
        .parse::<i64>()
        .unwrap();
    let y = device_split
        .split(", ")
        .last()
        .unwrap()
        .split('=')
        .last()
        .unwrap()
        .parse::<i64>()
        .unwrap();

    (x, y)
}
fn main() {
    let start = Instant::now();
    let now = Instant::now();

    let mut sensors = Vec::with_capacity(40);
    let mut beacons = Vec::with_capacity(40);

    let input = include_str!("../2022-15");
    input
        .lines()
        .filter(|line| !line.is_empty())
        .for_each(|line| {
            let mut positions = line.split(": ");
            let sensor_split = positions.next().unwrap();
            let beacon_split = positions.next().unwrap();
            let (sensor_x, sensor_y) = get_device_coordinates(sensor_split);
            let (beacon_x, beacon_y) = get_device_coordinates(beacon_split);
            sensors.push((sensor_x, sensor_y));
            beacons.push((beacon_x, beacon_y));
        });

    let elapsed = now.elapsed();
    println!("total time Parsing: {:.2?}", elapsed);
    let now = Instant::now();
    let N = sensors.len();
    const Y: i64 = 2000000;

    let mut allowed = Vec::new();
    let mut intervals = Vec::new();
    let mut dists = Vec::new();
    let mut pos_lines = Vec::new();
    let mut neg_lines = Vec::new();

    for i in 0..N - 1 {
        dists.push(dist(sensors[i], beacons[i]));
        let dx = dists[i] - (sensors[i].1 - Y).abs();
        if dx > 0 {
            intervals.push((sensors[i].0 - dx, sensors[i].0 + dx));
        }
        neg_lines.push(sensors[i].0 + sensors[i].1 - dists[i]);
        neg_lines.push(sensors[i].0 + sensors[i].1 + dists[i]);

        pos_lines.push(sensors[i].0 - sensors[i].1 - dists[i]);
        pos_lines.push(sensors[i].0 - sensors[i].1 + dists[i]);

        if beacons[i].0 == Y {
            allowed.push(beacons[i].0);
        }
    }
    let elapsed = now.elapsed();
    println!("total time normalising input: {:.2?}", elapsed);
    let now = Instant::now();
    // part 1
    let mut minx: i64 = i64::MAX;
    let mut maxx: i64 = i64::MIN;
    let mut answer: i64 = 0;
    let l = intervals.len();
    for i in 1..l {
        minx = minx.min(intervals[i].0);
        maxx = maxx.max(intervals[i].1);
    }
    for x in minx..maxx + 1 {
        {
            if allowed.contains(&x) {
                continue;
            }
            for i in 1..l {
                if intervals[i].0 <= x || x <= intervals[i].1 {
                    answer += 1;
                    break;
                }
            }
        }
    }
    let elapsed = now.elapsed();
    println!("Runtime part1: {:.2?}", elapsed);
    let now = Instant::now();
    // part 2
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
    let fullelapse = start.elapsed();
    println!("Runtime part2: {:.2?}", elapsed);
    println!("Full time spent {:.2?}", fullelapse);
    println!("part 1: {}", answer);
    println!("part 2: {}", ans);
}

fn dist(a: (i64, i64), b: (i64, i64)) -> i64 {
    (a.0 - b.0).abs() + (a.1 - b.1).abs()
}
