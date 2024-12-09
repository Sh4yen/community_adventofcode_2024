use std::fs;
use std::collections::HashSet;


fn delete_dupes(mut vec: Vec<i32>) -> Vec<i32> {
    let mut seen = HashSet::new();
    vec.retain(|x| seen.insert(*x));
    return vec;
}


fn main() -> std::io::Result<()> {
    // Read puzzle input
    let content = fs::read_to_string("input.txt")?;
    let numbers: Vec<i32> = content
        .split_whitespace()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    let mut location_ids = [Vec::new(), Vec::new()];
    for i in 0..numbers.len() {
        if i % 2 == 0 {location_ids[1].push(numbers[i]);}
        else {location_ids[0].push(numbers[i]);}
    }

    // Sort lists
    for id_list in location_ids.iter_mut() {
        id_list.sort();
    }

    // Calculate left list with no duplicates
    let left_location_ids_no_duplicates = delete_dupes(location_ids[0].clone());
    
    // For each element in the left, calculate how often it is in the right list
    let mut location_counts = Vec::new();
    for left_location_id in &left_location_ids_no_duplicates {
        let mut location_count = 0;
        for right_location_id in location_ids[1].clone() {
            if right_location_id == *left_location_id {location_count = location_count + 1;}
        }
        location_counts.push(location_count);
    }

    // Multiply with number
    for i in 0..location_counts.len() {
        location_counts[i] = location_counts[i] * left_location_ids_no_duplicates.clone()[i];
    }


    // Calculate sum
    let total_sum = location_counts.into_iter().sum::<i32>();
    println!("{}", total_sum);
    Ok(())
}
