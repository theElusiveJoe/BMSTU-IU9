object helper{
    private def get_all_pairs(x: List[Int]): List[(Int, Int)] = {
        if (x.length == 0 | x.length == 1) 
            return Nil 
        if (x.length == 2) 
            return List((x.head, x.tail.head))
        var first = x.head
        var xs = x.tail
        xs.map(y => (first, y))
    }

    def apply_permutations_to_idxs(perms: List[List[Int]], idxs: Seq[Int]) : Vector[Int] = {
        var transpositions =  perms.flatMap(get_all_pairs)
        var tmp = idxs.toBuffer
        for ((i,j) <- transpositions) {
            if ((i < tmp.length) & (j < tmp.length)){
                var (a, b) = (tmp(i), tmp(j))
                tmp(i) = b
                tmp(j) = a 
            }
        }
        tmp.toVector
    }

    def find_string_interseption(x: String, y: String): String = {
        (x,y) match {
            case ("", y) => y
            case (x, "") => x
            case (x,y) => fsil(x,y, x.length().min(y.length()))
        }
    }

    def fsil(x: String, y: String, pos: Int): String = {
        if (x.slice(x.length-pos, x.length) == y.slice(0, pos) )
            return x + y.slice(pos, y.length)
        fsil(x,y,pos-1)
    }

}
 

trait Stringer[T] {
    def sss(strings: Vector[T], idxs: Vector[Int]): Int
}

object Stringer{
    implicit object supstr extends Stringer[String] {
        override def sss(strings: Vector[String], idxs:Vector[Int]) = {
            var res = ""
            for (i <- Range(0, idxs.length)){
                var s = strings(idxs(i))
                res = helper.find_string_interseption(res, s)
            }
            println(res)
            res.length()
        }
    }
}


class Permutation[T](content: Vector[T], idxs: Vector[Int]){

    // вспомогательный конструктор для создания из любой последовательности и списка списков циклических перестановок
    def this(c: Seq[T], p: List[List[Int]]) = 
        this(c.toVector,  helper.apply_permutations_to_idxs(p, Range(0,c.length)))

    val length = content.length

    def apply(i: Int) : T = {
        this.content(this.idxs(i))
    }   

    def apply_permutations(ps: List[List[Int]]) : Permutation[T] = 
        new Permutation[T](content, helper.apply_permutations_to_idxs(ps, this.idxs)) 
    
    def superStringSize()(implicit stringer: Stringer[T]) : Int = stringer.sss(content, idxs)

}



object Main extends App {
    // var a = new Permutation[Char]("ABC", List(List(1,2,3)))
    // println(a.content mkString ", ")
    var my_perms = List(
        List(),
        List(1),
        List(1,2,3),
        List(5),
        List(7,6,8),
    )

    var my_perms2 = List(
            List(0,1),
            List(7,5,3)
        )

    // var t = new Permutation[Char]("0123456789", Nil)
    // var t = new Permutation[Double](List(0.0,1,2,3,4,5,6,7,8,9), Nil)
    var t = new Permutation[String](List("00","11", "22", "33", "44", "55", "66", "77", "88", "99"), Nil)
    
    for (i <- Range(0,10)){ print(t(i)); print(" ");}
    t = t.apply_permutations(my_perms)
    println()
    for (i <- Range(0,10)){ print(t(i)); print(" ");}
    println()
    t = t.apply_permutations(my_perms2)
    for (i <- Range(0,10)){ print(t(i)); print(" ");}
    t.superStringSize()
    println()
    
    var t2 = new Permutation[String](List("00","001", "1", "1", "", "55", "66", "55"), List(List(6,7)))
    println(t2.superStringSize())
}