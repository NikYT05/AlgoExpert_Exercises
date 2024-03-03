# algoExpert-Easy-Exercises
This is just mainly for my practice of programming languages repository.

//Two Number Sum Problem
export function twoNumberSum(array: number[], targetSum: number) {

  for (let i = 0; i < array.length - 1; i ++){
    let sum_so_far = 0;
    for (let j = i+1; j < array.length; j ++){
      sum_so_far = array[i] + array[j];
      if (targetSum === sum_so_far){
        return [array[i], array[j]];
      } else {
        continue;
      }
    }
  }
  return [];
}

