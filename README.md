# algoExpert-Easy-Exercises
This is just mainly for my practice of programming languages repository.

/*Two Number Sum Problem*/
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

/*nonConstructible Change - Given an array of integers "coins" return the minimum change that cannot be constructed. For example, given [1,2,5] the minimum change that cannot be formed is 4.*/
export function nonConstructibleChange(coins: number[]) {
  if (coins.length === 0){
    return 1;
  } else {
    coins.sort((a,b)=> a -b)
  }

  let sum_so_far: number = 0;

  for (let i = 0; i < coins.length; i ++){
    if (coins[0] > 1) {
      return 1;
    } else if (coins[i]-sum_so_far > 1){
      return sum_so_far + 1;
    } else {
      sum_so_far += coins[i];
    }
  }

  return sum_so_far + 1;
}

/*Depth First Seach*/
// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
export class Node {
  name: string;
  children: Node[];

  constructor(name: string) {
    this.name = name;
    this.children = [];
  }

  addChild(name: string) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array: string[]) {
    array.push(this.name)
    for (let child of this.children){
      child.depthFirstSearch(array);
    }
    return array;
  }
}
