// List(
//     "0", 
//     "1",
//     "2", 
//     "10",
//     // "422",
//     // "423" ,
//     // "1000",
//     "1001",
//     "131072", // 2^17
//     "6619136", // 101*2^16
//     "111050674405376", // 101*2^40
//     "604462909808414098980864" // 2**79 + 2**40
// ).foreach(
//     x => {
//         println("-------")
//         println(x)

//         var digits = str_to_ints(x)
//         // println(digits)

//         // var devided = devide_by_2(digits)
//         // println(devided).fivess map(represent_short)

//         var bindigits = dec_digits_to_binary(digits)
//         println(bindigits mkString "")

//         var five_shorts = binary_short_digits_to_five_shorts(bindigits)
//         println(five_shorts map represent_short mkString "")
//     }
// )