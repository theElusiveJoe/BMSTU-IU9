val loop: (List[Int], List[Int], List[Int], Int) => (List[Int], List[Int]) =
{
    case (Nil, a, b, n)                     => (a, b)
    case (num :: rest, a, b, n) if num < n    => loop(rest, a ::: List(num), b, n)
    case (num :: rest, a, b, n)             => loop(rest, a ,b ::: List(num), n)
}

val partition: (List[Int], Int) => (List[Int], List[Int]) =
   (nums, n) => loop(nums, Nil, Nil, n)
    
val res= partition(List(1,2,3,4,5,6,7,8,9), 5)
println(res.toString())
